import re
import sys
import requests
import subprocess

def extract_video_info(msn_url):
    match = re.search(r'msn\.com/([a-z]{2}-[a-z]{2})/.+?(?:video|news).*/vi-([A-Za-z0-9]+)', msn_url)
    if not match:
        print("Error: Could not extract locale and page_id from the URL.")
        return None, None
    return match.groups()

def get_video_json(locale, page_id):
    json_url = f"https://assets.msn.com/content/view/v2/Detail/{locale}/{page_id}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(json_url, headers=headers)
    if response.status_code != 200:
        print(f"Error: Failed to fetch JSON (HTTP {response.status_code})")
        return None
    return response.json()

def get_available_mp4s(video_json):
    try:
        video_files = video_json.get("videoMetadata", {}).get("externalVideoFiles", [])
        mp4_files = {v.get("format", "Unknown"): v["url"] for v in video_files if v.get("contentType") == "video/mp4"}
        return mp4_files
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return {}

def choose_video_quality(mp4_files):
    if not mp4_files:
        return None
    print("\nAvailable video qualities:")
    for key, url in sorted(mp4_files.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 0, reverse=True):
        print(f"[{key}] {url}")
    choice = input("\nEnter preferred format code (or Enter for best): ").strip()
    return mp4_files.get(choice, next(iter(mp4_files.values())))

def download_video(video_url, title="video"):
    if video_url:
        print(f"\nDownloading: {video_url}")
        try:
            subprocess.run(["yt-dlp", "--no-check-certificate", "-o", f"{title}.%(ext)s", video_url], check=True)
        except FileNotFoundError:
            print("yt-dlp not found! Using curl...")
            subprocess.run(["curl", "-L", "-O", video_url], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Download failed: {e}")
    else:
        print("Error: No MP4 file found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python msn_video_downloader.py <msn_video_url>")
        sys.exit(1)
    msn_url = sys.argv[1]
    locale, page_id = extract_video_info(msn_url)
    if locale and page_id:
        video_json = get_video_json(locale, page_id)
        if video_json:
            mp4_files = get_available_mp4s(video_json)
            if mp4_files:
                title = video_json.get("title", "msn_video")  # Use JSON title or fallback to "msn_video"
                video_url = choose_video_quality(mp4_files)
                download_video(video_url, title)
            else:
                print("No MP4 videos found in metadata.")
