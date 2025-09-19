# Anticosti Expedition Map (2025)

This repository contains an interactive map of the Anticosti Island field expedition, along with the data and code used to generate it.

## View the Map
The live interactive map is hosted on GitHub Pages:

👉 [View Map](https://peyton-thomas.github.io/expedition-map/)

---

## Repository Contents
expedition-map/
├── index.html # Interactive map (open in browser)
├── expedition_map.py # Python script used to generate the map
├── anticosti25_map.csv # Expedition site data (lat/lon, metadata, photos)
├── gpx/ # GPS track files
│ ├── day1-2025-06-26.gpx
│ ├── day2-2025-06-27.gpx
│ └── ...
├── images/ # Field photos (linked in the CSV)
│ ├── site1_photo1.jpg
│ ├── site2_photo1.jpg
│ └── ...
└── README.md # Documentation

---

## How to Regenerate the Map

1. Clone this repository:
   ```bash
   git clone https://github.com/peyton-thomas/expedition-map.git
   cd expedition-map
## Install folium
pip install folium pandas gpxpy

## Run Python script
python expedition-map.py

## Rename map file
mv expedition_map.html index.html

## Commit and refresh changes
git add .
git commit -m "update expedition map"
git push

