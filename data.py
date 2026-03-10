import pandas as pd

files = [
    "run_normal_1.txt",
    "run_normal_2.txt",
    "run_normal_3.txt",
    "run_anomaly_mem_3.txt",
    "run_anomaly_io.txt"
]

dfs = []

for f in files:
    df = pd.read_csv(f, sep="\t")
    df["source"] = f
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

print(data.head())

data.to_csv("combined_prmon_data.csv", index=False)
