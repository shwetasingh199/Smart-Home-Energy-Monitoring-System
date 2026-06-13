import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Smart Home Energy Monitoring System",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------------------------
# AUTO REFRESH
# --------------------------------------------------

st_autorefresh(
    interval=5000,
    key="refresh"
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

DB_PATH = "./database/energy.db"

@st.cache_data(ttl=5)
def load_data():

    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT *
    FROM energy
    ORDER BY timestamp DESC
    LIMIT 300
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:

    df = load_data()

except Exception as e:

    st.error(f"Database Error: {e}")
    st.stop()

# --------------------------------------------------
# CHECK DATA
# --------------------------------------------------

if df.empty:

    st.warning("No Energy Data Available Yet")
    st.stop()

# --------------------------------------------------
# DATA PREPROCESSING
# --------------------------------------------------

df["timestamp"] = pd.to_datetime(df["timestamp"])

df = df.sort_values("timestamp")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("⚙ Dashboard Controls")

# --------------------------------------------------
# ADD NEW APPLIANCE
# --------------------------------------------------

st.sidebar.markdown("---")
st.sidebar.subheader("➕ Add Appliance")

new_appliance = st.sidebar.text_input(
    "Appliance Name"
)

new_room = st.sidebar.text_input(
    "Room Name"
)

new_power = st.sidebar.number_input(
    "Rated Power (W)",
    min_value=1.0,
    value=100.0
)

if st.sidebar.button(
    "Add Appliance"
):

    if new_appliance and new_room:

        conn = sqlite3.connect(
            DB_PATH
        )

        cursor = conn.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO appliances
                (
                name,
                room,
                rated_power
                )
                VALUES(?,?,?)
                """,
                (
                    new_appliance,
                    new_room,
                    new_power
                )
            )

            conn.commit()

            st.sidebar.success(
                f"{new_appliance} Added"
            )

            st.cache_data.clear()

        except Exception as e:

            st.sidebar.error(
                str(e)
            )

        conn.close()


conn = sqlite3.connect(
    "database/energy.db"
)

appliance_master = pd.read_sql(
    """
    SELECT *
    FROM appliances
    """,
    conn
)

conn.close()

all_appliances = list(
    set(
        df["appliance"].unique()
    ).union(
        appliance_master["name"].tolist()
    )
)

selected_appliance = st.sidebar.multiselect(
    "Select Appliance",
    all_appliances,
    default=all_appliances[:3]
)

filtered_df = df[
    df["appliance"].isin(selected_appliance)
]

# --------------------------------------------------
# ENERGY CALCULATIONS
# --------------------------------------------------

RATE_PER_KWH = 8.5

avg_power = filtered_df["power"].mean()

total_power = filtered_df["power"].sum()

estimated_energy_kwh = total_power / 1000

estimated_cost = estimated_energy_kwh * RATE_PER_KWH

carbon_emission = estimated_energy_kwh * 0.82

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("⚡ Smart Home Energy Monitoring System")

st.markdown(
    """
    Real-Time Energy Analytics Dashboard
    """
)

# --------------------------------------------------
# ENERGY ANALYTICS
# --------------------------------------------------

total_energy = filtered_df[
    "energy"
].sum()

total_cost = filtered_df[
    "cost"
].sum()

avg_voltage = filtered_df[
    "voltage"
].mean()

active_devices = len(
    filtered_df[
        filtered_df["status"]=="ON"
    ]["appliance"].unique()
)

if not filtered_df.empty:

    peak_data = (
        filtered_df
        .groupby("appliance")["power"]
        .sum()
    )

    peak_appliance = (
        peak_data.idxmax()
        if not peak_data.empty
        else "N/A"
    )

else:

    peak_appliance = "N/A"

carbon_emission = (
    total_energy * 0.82
)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

c1,c2,c3,c4,c5,c6 = st.columns(6)

with c1:

    st.metric(
        "⚡ Energy",
        f"{total_energy:.2f} kWh"
    )

with c2:

    st.metric(
        "💰 Cost",
        f"₹{total_cost:.2f}"
    )

with c3:

    st.metric(
        "🔌 Avg Voltage",
        f"{avg_voltage:.1f} V"
    )

with c4:

    st.metric(
        "🏠 Active Devices",
        active_devices
    )

with c5:

    st.metric(
        "🔥 Peak Appliance",
        peak_appliance
    )

with c6:

    st.metric(
        "🌍 CO₂",
        f"{carbon_emission:.2f} kg"
    )

st.subheader(
    "📅 Daily Energy Consumption"
)

daily_energy = (
    filtered_df
    .groupby(
        filtered_df[
            "timestamp"
        ].dt.date
    )
    [
        "energy"
    ]
    .sum()
    .reset_index()
)

fig_daily = px.bar(
    daily_energy,
    x="timestamp",
    y="energy",
    title="Daily Energy Usage"
)

st.plotly_chart(
    fig_daily,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# ALERT SYSTEM
# --------------------------------------------------

latest_power = filtered_df.iloc[-1]["power"]

if latest_power > 2000:

    st.error(
        f"⚠ High Power Consumption Alert : {latest_power:.2f} W"
    )

elif latest_power > 1500:

    st.warning(
        f"⚠ Moderate Power Usage : {latest_power:.2f} W"
    )

else:

    st.success(
        f"✅ Normal Consumption : {latest_power:.2f} W"
    )

# --------------------------------------------------
# POWER TREND
# --------------------------------------------------

st.subheader("📈 Power Consumption Trend")

power_trend = (
    filtered_df
    .groupby(
        [
            pd.Grouper(
                key="timestamp",
                freq="30s"
            ),
            "appliance"
        ]
    )["power"]
    .mean()
    .reset_index()
)

fig_power = px.line(
    power_trend,
    x="timestamp",
    y="power",
    color="appliance",
    title="Average Power Consumption"
)

fig_power.update_traces(
    line=dict(width=3)
)

st.plotly_chart(
    fig_power,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# VOLTAGE TREND
# --------------------------------------------------

voltage_trend = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="timestamp",
            freq="30s"
        )
    )["voltage"]
    .mean()
    .reset_index()
)

fig_voltage = px.line(
    voltage_trend,
    x="timestamp",
    y="voltage",
    title="Average Voltage"
)

fig_voltage.update_traces(
    line=dict(width=3)
)

st.plotly_chart(
    fig_voltage,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# CURRENT TREND
# --------------------------------------------------

st.subheader("⚡ Current Trend")

current_trend = (
    filtered_df
    .groupby(
        [
            pd.Grouper(
                key="timestamp",
                freq="30s"
            ),
            "appliance"
        ]
    )["current"]
    .mean()
    .reset_index()
)

fig_current = px.line(
    current_trend,
    x="timestamp",
    y="current",
    color="appliance",
    title="Average Current Consumption"
)

fig_current.update_traces(
    line=dict(width=3)
)

st.plotly_chart(
    fig_current,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# APPLIANCE DISTRIBUTION
# --------------------------------------------------

st.subheader("🏠 Appliance Power Distribution")

appliance_power_df = (
    filtered_df
    .groupby("appliance")["power"]
    .sum()
    .reset_index()
)

if not appliance_power_df.empty:

    fig_pie = px.pie(
        appliance_power_df,
        names="appliance",
        values="power",
        hole=0.45,
        title="Power Distribution by Appliance"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

else:

    st.info(
        "No appliance data available."
    )
    
# --------------------------------------------------
# APPLIANCE RANKING
# --------------------------------------------------

st.subheader("🏆 Appliance Ranking")

ranking = (
    filtered_df
    .groupby("appliance")["power"]
    .sum()
    .reset_index()
)

ranking = ranking.sort_values(
    "power",
    ascending=False
)

st.dataframe(
    ranking,
    use_container_width=True
)

# --------------------------------------------------
# AI RECOMMENDATIONS
# --------------------------------------------------

st.subheader("💡 Smart Energy Recommendations")

if not ranking.empty:

    top_appliance = ranking.iloc[0]

    estimated_saving = top_appliance["power"] * 0.20

    st.success(
        f"""
🔹 Highest Consumer: {top_appliance['appliance']}

🔹 Total Usage: {top_appliance['power']:.2f} W

🔹 Potential Saving: {estimated_saving:.2f} W

🔹 Recommendation:
• Schedule usage during off-peak hours.
• Enable automatic shutoff.
• Monitor standby consumption.
• Reduce daily runtime by 15–20%.
"""
    )

# --------------------------------------------------
# TOP CONSUMING APPLIANCES
# --------------------------------------------------
appliance_power = (
    filtered_df
    .groupby("appliance")["power"]
    .sum()
    .reset_index()
)

st.subheader("🔥 Top Energy Consuming Appliances")

fig_bar = px.bar(
    appliance_power.sort_values(
        "power",
        ascending=False
    ),
    x="appliance",
    y="power",
    text_auto=True
)

st.plotly_chart(
    fig_bar,
    use_container_width=True,
    config={
        "displayModeBar": False
    }
)

# --------------------------------------------------
# DIGITAL TWIN SECTION
# --------------------------------------------------

st.subheader("🏡 Smart Home Digital Twin")

try:

    conn = sqlite3.connect(
        "database/energy.db"
    )

    appliance_master = pd.read_sql_query(
        """
        SELECT *
        FROM appliances
        """,
        conn
    )

    conn.close()

    if appliance_master.empty:

        st.warning(
            "No appliances registered."
        )

    else:

        room_power = []

        for _, row in appliance_master.iterrows():

            appliance_name = row["name"]

            room_name = row["room"]

            device_power = float(
                filtered_df.loc[
                    filtered_df["appliance"] == appliance_name,
                    "power"
                ].sum()
            )

            room_power.append(
                {
                    "Room": room_name,
                    "Appliance": appliance_name,
                    "Power": device_power
                }
            )

        room_power_df = pd.DataFrame(
            room_power
        )

        if (
            not room_power_df.empty
            and room_power_df["Power"].sum() > 0
        ):

            fig_room = px.sunburst(
                room_power_df,
                path=[
                    "Room",
                    "Appliance"
                ],
                values="Power"
            )

            st.plotly_chart(
                fig_room,
                use_container_width=True,
                config={
                    "displayModeBar": False
                }
            )

        else:

            st.info(
                "Waiting for appliance power data..."
            )

except Exception as e:

    st.error(
        f"Digital Twin Error: {e}"
    )

# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

st.subheader("📋 Energy Logs")

st.dataframe(
    filtered_df.sort_values(
        "timestamp",
        ascending=False
    ).head(100),
    use_container_width=True
)

# --------------------------------------------------
# DOWNLOAD CSV
# --------------------------------------------------

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Energy Logs",
    data=csv,
    file_name="energy_logs.csv",
    mime="text/csv"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    ### Smart Home Energy Monitoring System
    
    Features:
    - Real-Time Monitoring
    - Energy Analytics
    - Cost Estimation
    - Carbon Footprint Tracking
    - Appliance Wise Insights
    - Alert Generation
    - CSV Export
    """
)