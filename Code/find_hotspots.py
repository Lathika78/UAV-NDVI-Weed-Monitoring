import pandas as pd

df = pd.read_csv("weed_report.csv")

top5 = df.sort_values("Weed %", ascending=False).head(5)

print("TOP 5 WEED HOTSPOTS")
print(top5[["Image", "Weed %"]])