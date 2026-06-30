import cv2
import os
import pandas as pd

# Path to your Masks folder
mask_folder = r"C:\Users\gobik\Downloads\A Dataset of Aligned RGB and Multispectral UAV Ima\A Dataset of Aligned RGB and Multispectral UAV Ima\WeedyRice-RGBMS-DB\WeedyRice-RGBMS-DB\Masks"

results = []

for file in os.listdir(mask_folder):
    if file.endswith(".png"):
        path = os.path.join(mask_folder, file)

        mask = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        total_pixels = mask.size
        weed_pixels = (mask == 255).sum()

        weed_percent = (weed_pixels / total_pixels) * 100
        healthy_percent = 100 - weed_percent

        results.append([
            file,
            weed_pixels,
            total_pixels,
            round(weed_percent, 2),
            round(healthy_percent, 2)
        ])

df = pd.DataFrame(
    results,
    columns=[
        "Image",
        "Weed Pixels",
        "Total Pixels",
        "Weed %",
        "Healthy %"
    ]
)

df.to_csv("weed_report.csv", index=False)

print("Finished!")
print("weed_report.csv created")