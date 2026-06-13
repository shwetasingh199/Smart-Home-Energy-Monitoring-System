# ai/anomaly_detection.py

import pandas as pd

from sklearn.ensemble import IsolationForest

df = pd.read_csv(
    "data/energy_logs.csv"
)

model = IsolationForest(
    contamination=0.02
)

df["anomaly"] = model.fit_predict(
    df[["power"]]
)

print(
df[df["anomaly"]==-1]
)