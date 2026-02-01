import os
from YOUTUBE import download as yt_download
from TikTok import download_tiktok
from SOCIAL import download_social_video, download_fb_story
from History import show_history, search_history
from cls import clear

def main():
    while True:
        clear()
        print("==========================================")
        print("    🌟 កម្មវិធីទាញយកវីដេអូពហុប្រព័ន្ធ V3.0   ")
        print("==========================================")
        print(" [1]. YouTube (វីដេអូ/ចម្រៀង)")
        print(" [2]. TikTok (វីដេអូ/រូបភាព Slideshow)")
        print(" [3]. Facebook & X (Reels/Post/Video)")
        print(" [4]. Facebook Story (ត្រូវការ Cookies)")
        print(" [5]. មើលប្រវត្តិទាញយក (History)")
        print("------------------------------------------")
        print(" [8]. សម្អាត Screen | [9]. ចាកចេញ")
        print("==========================================")

        choice = input("👉 សូមជ្រើសរើសជម្រើសរបស់អ្នក: ").strip()

        if choice == "1":
            clear()
            print("📺 DOWNLOAD YOUTUBE")
            u = input("🔗 ដាក់ Link YouTube: ").strip()
            print(" 1. កម្រិតខ្ពស់ (Best) | 2. 720p | 3. 480p")
            q = input("👉 រើសកម្រិតច្បាស់: ").strip()
            if u: yt_download(u, q)
            input("\nចុច Enter ដើម្បីបន្ត...")

        elif choice == "2":
            clear()
            print("🚀 DOWNLOAD TIKTOK")
            print(" [1]. វីដេអូ (Video) | [2]. រូបភាព (Slideshow)")
            tk_mode = input("👉 រើសប្រភេទ: ").strip()
            url = input("🔗 ដាក់ Link TikTok: ").strip()
            
            if tk_mode == "1":
                q = input("🎥 រើសគុណភាព (1. HD / 2. SD): ").strip()
                download_tiktok(url, mode="video", quality="hd" if q=="1" else "sd")
            else:
                download_tiktok(url, mode="photo")
            input("\nចុច Enter ដើម្បីបន្ត...")

        elif choice == "3":
            clear()
            print("🔵 DOWNLOAD FACEBOOK & X")
            url = input("🔗 ដាក់ Link វីដេអូ: ").strip()
            platform = "Facebook" if "facebook" in url or "fb" in url else "X/Twitter"
            download_social_video(url, platform)
            input("\nចុច Enter ដើម្បីបន្ត...")

        elif choice == "4":
            clear()
            print("🎬 DOWNLOAD FACEBOOK STORY")
            print("⚠️ បញ្ជាក់៖ សូមបិទ Chrome ជាមុនសិន!")
            url = input("🔗 ដាក់ Link Story: ").strip()
            download_fb_story(url)
            input("\nចុច Enter ដើម្បីបន្ត...")

        elif choice == "5":
            clear()
            print("📜 ប្រវត្តិការទាញយក")
            show_history()
            print("\n[S]. ស្វែងរកតាមឈ្មោះ | [Any]. ត្រឡប់ក្រោយ")
            cmd = input("👉 ជ្រើសរើស: ").strip().lower()
            if cmd == 's':
                key = input("🔍 បញ្ចូលពាក្យគន្លឹះ: ")
                search_history(key)
                input("\nចុច Enter ដើម្បីបន្ត...")

        elif choice == "8":
            clear()
        
        elif choice == "9":
            print("\n🙏 អរគុណ! សូមជម្រាបលា។")
            break
if __name__ == "__main__":
    main()