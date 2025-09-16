import pandas as pd
import re

# Load your CSV
csv_file = "anticosti2025_map.csv"
sites = pd.read_csv(csv_file)

# Function to convert a Google Drive share link to a direct link
def gdrive_to_direct(url):
    """
    Converts a Google Drive sharing URL into a direct download URL for images.
    Handles multiple links separated by commas.
    """
    if not isinstance(url, str) or not url.strip():
        return ""
    
    links = url.split(",")
    direct_links = []
    for link in links:
        link = link.strip()
        match = re.search(r"/d/([a-zA-Z0-9_-]+)", link)
        if match:
            file_id = match.group(1)
            direct_links.append(f"https://drive.google.com/uc?id={file_id}")
        else:
            print(f"⚠ Could not convert link: {link}")
            direct_links.append(link)  # fallback: keep original link
    return ",".join(direct_links)

# Apply the conversion to the 'photos' column
if "photos" in sites.columns:
    sites["photos"] = sites["photos"].apply(gdrive_to_direct)

# Optional: save to a new CSV
sites.to_csv("anticosti2025_map_direct_photos.csv", index=False)
print("✅ CSV updated with direct Google Drive image links.")
