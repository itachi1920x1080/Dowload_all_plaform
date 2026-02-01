import yt_dlp
import os
from cls import clear
from Path import get_path_youtube
path = get_path_youtube()

def download(url, mode):
    if mode == "tiktok":
        fmt = "best"
    elif mode == "1":
        fmt = "bestvideo+bestaudio/best"
    elif mode == "2":
        fmt = "bestvideo[height<=720]+bestaudio/best"
    elif mode == "3":
        fmt = "bestvideo[height<=480]+bestaudio/best"
    else:
        fmt = "bestvideo+bestaudio/best"

    ydl_opts = {
        'format': fmt,
        'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    # ydl_opts = {
    #     'format': fmt,
    #     'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
    #     'quiet': False,
    #     'no_warnings': True,
    #     'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    #     'writethumbnail': True,       # Download thumbnail
    #     'writeinfojson': True,        # Download info.json metadata
    # }

    try:
        print(f"🚀 Processing... (Mode: {mode})")
        
        info = yt_dlp.YoutubeDL(ydl_opts).extract_info(url, download=True)
        
        clear()
        print("==========================================")
        print("✅ DOWNLOAD SUCCESSFUL!")
        print("==========================================")
        print(f"🎥 Title:    {info.get('title')}")
        print(f"👤 Uploader: {info.get('uploader')}")
        print(f"📂 Saved to: {path}")
        print("==========================================")

    except Exception as e:
        print(f"\n❌ Error: {e}")