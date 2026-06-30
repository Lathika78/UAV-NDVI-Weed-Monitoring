import pandas as pd
import re

# Read weed report
df = pd.read_csv("weed_report.csv")

# Take top 10 highest weed images
top = df.sort_values("Weed %", ascending=False).head(10)

locations = []

for _, row in top.iterrows():

    image = row["Image"]

    lat_match = re.search(r'lat_([0-9.]+)', image)
    lon_match = re.search(r'lon_([0-9.]+)', image)

    lat = lat_match.group(1) if lat_match else "Not Found"
    lon = lon_match.group(1) if lon_match else "Not Found"

    locations.append([
        image,
        lat,
        lon,
        row["Weed %"]
    ])

gps_df = pd.DataFrame(
    locations,
    columns=[
        "Image",
        "Latitude",
        "Longitude",
        "Weed %"
    ]
)

gps_df.to_csv("gps_hotspots.csv", index=False)

print("GPS hotspot report generated!")
print(gps_df)