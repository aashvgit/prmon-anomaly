import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

df = pd.read_csv("monitoring_data.csv")

# IQR anomaly detection
Q1 = df["pss"].quantile(0.25)
Q3 = df["pss"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df["iqr_anomaly"] = (df["pss"] < lower) | (df["pss"] > upper)

# Isolation Forest
model = IsolationForest(contamination=0.05)
df["if_anomaly"] = model.fit_predict(df[["pss"]])

plt.figure(figsize=(10,5))
plt.plot(df["Time"], df["pss"], label="PSS memory")

anoms = df[df["iqr_anomaly"]]
plt.scatter(anoms["Time"], anoms["pss"], color="red", label="IQR anomaly")

plt.xlabel("Time")
plt.ylabel("PSS")
plt.title("Memory Monitoring with Anomaly Detection")
plt.legend()

plt.savefig("anomaly_plot.png")
