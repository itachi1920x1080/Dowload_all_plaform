import os

def get_save_path(platform="General", file_type="video"):
    """
    កំណត់ផ្លូវសម្រាប់រក្សាទុកឯកសារតាមប្រភេទ និង Platform
    platform: 'YouTube', 'TikTok', 'Facebook', etc.
    file_type: 'video', 'image', 'audio'
    """
    
    # បង្កើតឈ្មោះ Folder ជាមូលដ្ឋាន (ឧទាហរណ៍៖ TikTok_Videos)
    folder_name = f"{platform}_{file_type.capitalize()}s"
    
    # កំណត់ផ្លូវ (Path) នៅក្នុង Folder បច្ចុប្បន្ននៃកម្មវិធី
    path = os.path.join(os.getcwd(), folder_name)
    
    # បង្កើត Folder បើមិនទាន់មាន
    os.makedirs(path, exist_ok=True)
    
    return path

# --- ឧទាហរណ៍នៃការរក្សាទុកកូដចាស់របស់អ្នក (បើអ្នកនៅតែចង់ប្រើឈ្មោះ function ដើម) ---

def get_path_youtube():
    return get_save_path("YouTube", "video")

def get_path_tiktok():
    return get_save_path("TikTok", "video")

def get_path_tiktok_images():
    return get_save_path("TikTok", "image")
