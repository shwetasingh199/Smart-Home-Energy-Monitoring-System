# ai/energy_forecasting.py

import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv(
    "data/energy_logs.csv"
)

X = df.index.values.reshape(-1,1)

y = df["power"]

model = LinearRegression()

model.fit(X,y)

future = model.predict(
    [[len(df)+24]]
)

print(
"Predicted Consumption:",
future[0]
)