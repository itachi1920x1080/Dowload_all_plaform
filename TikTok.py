import os
import requests
from Path import get_save_path # ហៅចេញពី file Path.py ដែលយើងកែមុននេះ

def download_tiktok(url, mode="video", quality="hd"):
    api_url = "https://www.tikwm.com/api/"
    params = {"url": url, "hd": 1 if quality == "hd" else 0}
    
    try:
        response = requests.get(api_url, params=params).json()
        if response.get('code') != 0:
            print(f"❌ Error: {response.get('msg')}")
            return

        data = response['data']
        title = data.get('title', 'tiktok_content').replace(" ", "_")[:50]
        clean_title = "".join([c for c in title if c.isalnum() or c in ('_', '-')]).rstrip()

        # --- ករណីទាញយកជាវីដេអូ ---
        if mode == "video":
            save_dir = get_save_path("TikTok", "video")
            
            # ជ្រើសរើស Link តាមគុណភាព
            if quality == "hd" and 'hdplay' in data:
                video_url, suffix = data['hdplay'], "_HD"
            else:
                video_url, suffix = data['play'], "_SD"

            filename = f"{clean_title}{suffix}.mp4"
            full_path = os.path.join(save_dir, filename)

            print(f"🚀 កំពុងទាញយកវីដេអូ: {filename}...")
            r = requests.get(video_url, stream=True)
            with open(full_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk: f.write(chunk)
            print(f"✅ រក្សាទុកនៅ: {full_path}")

        # --- ករណីទាញយករូបភាព (Slideshow) ---
        elif mode == "photo":
            if 'images' not in data:
                print("ℹ️ Link នេះមិនមែនជារូបភាព Slideshow ទេ។")
                return

            save_dir = get_save_path("TikTok", "image")
            # បង្កើត Folder ដាច់ដោយឡែកសម្រាប់រូបភាពនីមួយៗ
            photo_folder = os.path.join(save_dir, clean_title)
            os.makedirs(photo_folder, exist_ok=True)

            images = data['images']
            print(f"📸 រកឃើញរូបភាព {len(images)} សន្លឹក...")
            for i, img_url in enumerate(images):
                img_data = requests.get(img_url).content
                with open(os.path.join(photo_folder, f"img_{i+1}.jpg"), "wb") as f:
                    f.write(img_data)
            print(f"✅ រូបភាពទាំងអស់រក្សាទុកក្នុង: {photo_folder}")

    except Exception as e:
        print(f"❌ កំហុសបច្ចេកទេស: {e}")