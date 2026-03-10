import numpy as np
import pandas as pd

np.random.seed(42)

time = np.arange(0, 200)

# baseline memory usage
pss = 200 + np.random.normal(0, 5, size=200)

# injected anomalies
pss[80:90] += 80
pss[150:155] += 120

df = pd.DataFrame({
    "Time": time,
    "pss": pss
})

df.to_csv("monitoring_data.csv", index=False)

print("Generated monitoring_data.csv")
