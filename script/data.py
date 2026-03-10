import pandas as pd

files = [
    "runnormal1.txt",
    "runnormal2.txt",
    "runnormal3.txt",
    "runanomalymem.txt",
    "runanomalyio.txt"
]

dfs = []

for f in files:
    df = pd.read_csv(f, sep="\t")
    df["source"] = f
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

print(data.head())

data.to_csv("combined_prmon_data.csv", index=False)
