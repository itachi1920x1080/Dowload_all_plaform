import json
import os
from datetime import datetime

# កំណត់ឈ្មោះហ្វាយសម្រាប់ទុកទិន្នន័យ
HISTORY_FILE = "download_history.json"

def save_to_history(platform, title, url, save_path):
    """រក្សាទុកព័ត៌មាននៃការទាញយកចូលក្នុង JSON"""
    history_data = []
    
    # ១. ឆែកមើលបើមានហ្វាយស្រាប់ ត្រូវទាញទិន្នន័យចាស់មកសិន
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            try:
                history_data = json.load(f)
            except:
                history_data = []

    # ២. បង្កើតទិន្នន័យថ្មី
    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "platform": platform,
        "title": str(title),
        "url": url,
        "path": save_path
    }
    
    # ៣. បន្ថែមចូលទៅក្នុងបញ្ជី (List)
    history_data.append(new_entry)

    # ៤. សរសេរចូលក្នុងហ្វាយវិញ
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history_data, f, ensure_ascii=False, indent=4)

def show_history():
    """បង្ហាញប្រវត្តិទាញយក ១០ ចុងក្រោយលើ Screen"""
    if not os.path.exists(HISTORY_FILE):
        print("\n📂 មិនទាន់មានប្រវត្តិទាញយកនៅឡើយទេ។")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            print(f"\n{'កាលបរិច្ឆេទ':<20} | {'Platform':<10} | {'ចំណងជើង':<30}")
            print("-" * 75)
            # បង្ហាញតែ ១០ វីដេអូចុងក្រោយ
            for entry in data[-10:]:
                print(f"{entry['date']:<20} | {entry['platform']:<10} | {str(entry['title'])[:30]:<30}")
        except:
            print("❌ មានបញ្ហាក្នុងការអានហ្វាយ History។")

def search_history(keyword):
    """ស្វែងរកវីដេអូដែលធ្លាប់ទាញយកតាមរយៈឈ្មោះ"""
    if not os.path.exists(HISTORY_FILE):
        print("📂 មិនទាន់មានទិន្នន័យទេ។")
        return

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        results = [e for e in data if keyword.lower() in e['title'].lower()]
        
        if results:
            print(f"\n🔍 រកឃើញលទ្ធផលចំនួន {len(results)}៖")
            for r in results:
                print(f"📌 {r['date']} - {r['platform']}: {r['title']}")
                print(f"   📍 Path: {r['path']}\n")
        else:
            print(f"❓ រកមិនឃើញអ្វីដែលទាក់ទងនឹង '{keyword}' ទេ។")