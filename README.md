# UAV-Based NDVI Analysis, Weed Detection and GPS Hotspot Mapping Using Multispectral Images

## Project Overview

This project presents a UAV-based crop monitoring system using multispectral images for weed detection and field analysis. The system generates NDVI images, detects weed-infested regions using mask images, calculates weed coverage percentage, identifies weed hotspots, and maps their GPS locations. The proposed approach helps analyze crop fields efficiently and supports precision agriculture through automated image analysis.

---

## Objectives

- Generate NDVI from UAV multispectral images.
- Detect weed-infested regions using mask images.
- Calculate weed percentage for each image.
- Generate field information and weed statistics.
- Identify the top weed hotspot regions.
- Map weed hotspots using GPS coordinates.

---

## Methodology

1. Collect UAV multispectral images.
2. Generate NDVI using the Red and NIR bands.
3. Detect weeds from mask images.
4. Calculate weed percentage.
5. Generate field information.
6. Identify weed hotspot regions.
7. Extract GPS coordinates for hotspot mapping.

---

## Software and Tools

- Python
- OpenCV
- Rasterio
- NumPy
- Pandas
- QGIS
- PyCharm

---

## Results

The proposed system successfully:

- Generated NDVI maps from UAV multispectral images.
- Detected weed-infested regions using mask images.
- Calculated weed percentage for each image.
- Generated field information reports.
- Identified the top weed hotspot regions.
- Mapped hotspot locations using GPS coordinates.

### Field Statistics

| Parameter | Result |
|-----------|-------:|
| Images Analyzed | 434 |
| Average Weed Percentage | 18.28% |
| Maximum Weed Percentage | 56.89% |
| Minimum Weed Percentage | 0.27% |
| Low Weed Images | 61 |
| Moderate Weed Images | 167 |
| High Weed Images | 206 |

---

## Validation

To verify the correctness of the weed percentage calculation, three sample mask images with known weed coverage were tested.

| Validation Image | Expected Weed % | Calculated Weed % | Status |
|-----------------|----------------:|------------------:|--------|
| Mask test 1 | 0.01% | 0.01% | ✅ Passed |
| Mask test 2 | 0.03% | 0.03% | ✅ Passed |
| Mask test 3 | 0.06% | 0.06% |✅ Passed |

The validation results confirm that the weed percentage calculation accurately reflects the weed pixels present in the mask images.

---

## Future Work

- Crop disease detection
- Water stress analysis
- Nutrient deficiency assessment
- Real-time UAV monitoring
- Automated decision support for precision agriculture

---

## Author

**N LATHIKA CHEZHIAN, JAFFRINE REFINA R, HARINI S

Department of Electronics and Communication 

---

## License

This repository is intended for academic and research purposes.
