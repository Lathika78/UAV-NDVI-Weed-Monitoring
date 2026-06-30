import pandas as pd

df = pd.read_csv("weed_report.csv")

avg_weed = df["Weed %"].mean()
max_weed = df["Weed %"].max()
min_weed = df["Weed %"].min()

low = len(df[df["Weed %"] < 5])
moderate = len(df[(df["Weed %"] >= 5) & (df["Weed %"] <= 15)])
high = len(df[df["Weed %"] > 15])

print("FIELD SUMMARY")
print("-" * 30)
print(f"Images analyzed: {len(df)}")
print(f"Average weed percentage: {avg_weed:.2f}%")
print(f"Maximum weed percentage: {max_weed:.2f}%")
print(f"Minimum weed percentage: {min_weed:.2f}%")
print()
print(f"Low severity images (<5%): {low}")
print(f"Moderate severity images (5-15%): {moderate}")
print(f"High severity images (>15%): {high}")