import os
import re
import requests
from yt_dlp import YoutubeDL

# ===========================
SEARCH_QUERY = "EDIT/AMV"
MAX_RESULTS = 1000
OUTPUT_DIR = "thumbnails"
# ===========================

os.makedirs(OUTPUT_DIR, exist_ok=True)

ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "skip_download": True,
}

with YoutubeDL(ydl_opts) as ydl:
    results = ydl.extract_info(
        f"ytsearch{MAX_RESULTS}:{SEARCH_QUERY}",
        download=False,
    )

entries = results.get("entries", [])

print(f"Found {len(entries)} videos")

for i, video in enumerate(entries, 1):
    video_id = video["id"]
    title = video.get("title", "Untitled")

    safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)

    thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"

    response = requests.get(thumbnail_url)

    if response.status_code != 200:
        thumbnail_url = f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        response = requests.get(thumbnail_url)

    if response.status_code == 200:
        filename = os.path.join(
            OUTPUT_DIR,
            f"{i:03d}_{safe_title}.jpg"
        )

        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Downloaded: {title}")
    else:
        print(f"Failed: {title}")