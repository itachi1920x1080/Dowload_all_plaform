import yt_dlp
import os
from Path import get_save_path
from History import save_to_history

# ១. មុខងារទាញយកវីដេអូទូទៅ (FB Reels/Post, X, IG)
def download_social_video(url, platform_name="Social"):
    save_path = get_save_path(platform_name, "video")
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': False,
        'no_warnings': True,
        # បន្ថែម cookies ក្នុងករណីវីដេអូខ្លះត្រូវការ Log in (ដូចជា Facebook Private)
        'cookiesfrombrowser': ('chrome',), 
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"🚀 កំពុងទាញយកវីដេអូពី {platform_name}...")
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Social_Video')
            
            # កត់ត្រាចូល History
            save_to_history(platform_name, title, url, save_path)
            
            print(f"✅ រួចរាល់! រក្សាទុកក្នុង: {platform_name}_Videos")
    except Exception as e:
        print(f"❌ កំហុសបច្ចេកទេស: {e}")

# ២. មុខងារទាញយក Facebook Story (ត្រូវការការប្រយ័ត្នខ្ពស់លើ Cookies)
def download_fb_story(url):
    save_path = get_save_path("Facebook", "Story")
    cookie_file = "cookies.txt"  # ឈ្មោះហ្វាយដែលអ្នកបានដាក់ក្នុង Folder
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(save_path, 'FB_Story_%(id)s.%(ext)s'),
        'cookiefile': 'cookies.txt',
        'quiet': False,
        'no_warnings': True,
        # បន្ថែម User-Agent ដើម្បីបន្លំខ្លួនជា Chrome ពិតៗ
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'nocheckcertificate': True,
    }

    if not os.path.exists(cookie_file):
        print("\n❌ រកមិនឃើញហ្វាយ cookies.txt ទេ!")
        print("💡 សូម Export cookies ពី Browser រួចដាក់ក្នុង Folder នេះសិន។")
        return

    try:
        print("🔐 កំពុងប្រើ Cookies ពីហ្វាយដើម្បីទាញយក Story...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            save_to_history("Facebook", "Story Video", url, save_path)
            print(f"✅ ទាញយកបានជោគជ័យ!")
    except Exception as e:
        print(f"❌ នៅតែមិនអាចទាញយកបាន៖ {e}")