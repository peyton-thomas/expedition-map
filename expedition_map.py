import folium
import pandas as pd
import gpxpy

# -------------------------------
# 1. Load site data from CSV
# -------------------------------
csv_file = "anticosti25_map.csv"  # make sure this is in the same folder
sites = pd.read_csv(csv_file, encoding="latin1")  # works for most Western accented characters

# Standardize column names: lowercase + strip spaces
sites.columns = sites.columns.str.strip().str.lower()

# Ensure we have a 'name' column
if "name" not in sites.columns:
    # Try to find alternatives
    for alt in ["site_name", "site", "location"]:
        if alt in sites.columns:
            sites = sites.rename(columns={alt: "name"})
            break
    else:
        # If no suitable column found, fill with default names
        sites["name"] = [f"Site {i+1}" for i in range(len(sites))]

# Rename variations so code is flexible
if "longitude" in sites.columns:
    sites = sites.rename(columns={"longitude": "lon"})
if "latitude" in sites.columns:
    sites = sites.rename(columns={"latitude": "lat"})

# -------------------------------
# 2. Create base map
# -------------------------------
# Center on mean of site coordinates
m = folium.Map(
    location=[sites["lat"].mean(), sites["lon"].mean()],
    zoom_start=10
)

# -------------------------------
# 3. Add GPX routes (tracks, routes, waypoints)
# -------------------------------
gpx_files = [
    "day1-2025-06-26.gpx", "day2-2025-06-27.gpx", "day3-2025-06-28.gpx",
    "day4-2025-06-29.gpx", "day5-2025-06-30.gpx", "day6-2025-07-01.gpx",
    "day7-2025-07-02.gpx", "day8-2025-07-03.gpx", "SE_day1.gpx", "SE_day1_2.gpx", "SE_day2.gpx", "SE_day3.gpx", "SE_day4.gpx", "SE_day5.gpx", "SE_day6.gpx", "SE_day7.gpx", "SE_day8.gpx", "SE_day9.gpx"
]

for gpx_file in gpx_files:
    try:
        with open(gpx_file, "r", encoding="utf-8") as f:
            gpx = gpxpy.parse(f)
 # Choose line color based on filename
        line_color = "black" if "SE" in gpx_file else "blue"

        # Tracks + segments
        for track in gpx.tracks:
            for segment in track.segments:
                coords = [(pt.latitude, pt.longitude) for pt in segment.points]
                if coords:
                    folium.PolyLine(coords, color="blue", weight=3, opacity=0.7).add_to(m)

        # Routes (sometimes GPX only stores these instead of tracks)
        for route in gpx.routes:
            coords = [(pt.latitude, pt.longitude) for pt in route.points]
            if coords:
                folium.PolyLine(coords, color="green", weight=3, opacity=0.7).add_to(m)

        # Waypoints (individual points)
        for wp in gpx.waypoints:
            folium.Marker(
                location=[wp.latitude, wp.longitude],
                popup=wp.name or "Waypoint",
                icon=folium.Icon(color="red", icon="flag")
            ).add_to(m)

    except FileNotFoundError:
        print(f"⚠️ Could not find {gpx_file}, skipping...")
    except Exception as e:
        print(f"⚠️ Error loading {gpx_file}: {e}")


# -------------------------------
# 4. Add site markers
# -------------------------------
for _, row in sites.iterrows():
# Determine marker color based on year
    marker_color = "gray"  # default
    if "date" in row and isinstance(row["date"], str):
        if "2024" in row["date"]:
            marker_color = "orange"
        elif "2025" in row["date"]:
            marker_color = "cadetblue"
    # Handle multiple photos (split by comma/semicolon)
    photos_html = ""
    if "photos" in row and isinstance(row["photos"], str) and row["photos"].strip():
        for p in row["photos"].replace(";", ",").split(","):
            p = p.strip()
            if p:  # only add if not empty
                photos_html += f'<img src="{p}" width="200" style="display:block; margin-bottom:5px;"><br>'

    # Build popup HTML
    html = f"""
    <h4>{row.get('name', 'Site')}</h4>
    <b>Lat:</b> {row['lat']}<br>
    <b>Lon:</b> {row['lon']}<br>
    """
    if "temperature" in row: html += f"<b>Temperature:</b> {row['temperature']} °C<br>"
    if "conductivity" in row: html += f"<b>Conductivity:</b> {row['conductivity']} µS/cm<br>"
    if "team" in row: html += f"<b>Team:</b> {row['team']}<br>"
    if "fish_caught" in row: html += f"<b>Fish caught:</b> {row['fish_caught']}<br>"
    if "type" in row: html += f"<b>Type:</b> {row['type']}<br>"
    if "salmon_river" in row: html += f"<b>Salmon River:</b> {row['salmon_river']}<br>"
    if "date" in row: html += f"<b>Date:</b> {row['date']}<br>"
    if "time" in row: html += f"<b>Time:</b> {row['time']}<br>"
    if photos_html: html += photos_html

    popup = folium.Popup(html, max_width=300)
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=popup,
        tooltip=row.get("name", "site"),
	icon=folium.Icon(color=marker_color, icon="info-sign")
    ).add_to(m)

# -------------------------------
# 5. Add legend
# -------------------------------
legend_html = """
<div style="
    position: fixed;
    bottom: 30px;
    left: 30px;
    width: 200px;
    background-color: white;
    border: 2px solid gray;
    padding: 10px;
    z-index: 1000;
    font-size: 14px;
    box-shadow: 2px 2px 4px rgba(0,0,0,0.3);
">
<b>Legend</b><br>
<hr style="margin: 5px 0;">
<div><span style="background-color: blue; width: 20px; height: 4px; display: inline-block; margin-right: 5px;"></span> 2025 Route</div>
<div><span style="background-color: black; width: 20px; height: 4px; display: inline-block; margin-right: 5px;"></span> Sud-Est Route</div>
<br>
<div><span style="background-color: orange; width: 12px; height: 12px; display: inline-block; border-radius: 50%; margin-right: 5px;"></span> 2024 Site</div>
<div><span style="background-color: cadetblue; width: 12px; height: 12px; display: inline-block; border-radius: 50%; margin-right: 5px;"></span> 2025 Site</div>
<div><span style="background-color: gray; width: 12px; height: 12px; display: inline-block; border-radius: 50%; margin-right: 5px;"></span> Other Site</div>
</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))
# -------------------------------
# 6. Save map
# -------------------------------
m.save("expedition_map.html")
print("✅ Map saved as expedition_map.html")

