import pandas as pd

# =========================
# READ REPORTS
# =========================

weed_df = pd.read_csv("weed_report.csv")
gps_df = pd.read_csv("gps_hotspots.csv")

# =========================
# FIELD INFORMATION
# =========================

avg_weed = weed_df["Weed %"].mean()
max_weed = weed_df["Weed %"].max()
min_weed = weed_df["Weed %"].min()

print("\n" + "=" * 60)
print("UAV-BASED WEED MONITORING REPORT")
print("=" * 60)

print("\nFIELD INFORMATION")
print("-" * 30)
print(f"Images Analyzed      : {len(weed_df)}")
print(f"Average Weed %       : {avg_weed:.2f}%")
print(f"Maximum Weed %       : {max_weed:.2f}%")
print(f"Minimum Weed %       : {min_weed:.2f}%")

# =========================
# WEED DETECTION
# =========================

low = len(weed_df[weed_df["Weed %"] < 5])
moderate = len(
    weed_df[
        (weed_df["Weed %"] >= 5) &
        (weed_df["Weed %"] <= 15)
    ]
)
high = len(weed_df[weed_df["Weed %"] > 15])

print("\nWEED DETECTION SUMMARY")
print("-" * 30)
print(f"Low Weed Images      : {low}")
print(f"Moderate Weed Images : {moderate}")
print(f"High Weed Images     : {high}")

# =========================
# WEED HOTSPOTS
# =========================

print("\nTOP 10 WEED HOTSPOTS")
print("-" * 30)

top10 = weed_df.sort_values("Weed %", ascending=False).head(10)

for i, row in top10.iterrows():
    print(
        f"{i+1}. {row['Image'][:50]}... "
        f"-> {row['Weed %']:.2f}%"
    )

# =========================
# GPS HOTSPOTS
# =========================

print("\nGPS HOTSPOT LOCATIONS")
print("-" * 30)

for i, row in gps_df.head(10).iterrows():
    print(
        f"{i+1}. "
        f"Lat: {row['Latitude']} | "
        f"Lon: {row['Longitude']} | "
        f"Weed: {row['Weed %']}%"
    )

print("\nREPORT GENERATED SUCCESSFULLY")