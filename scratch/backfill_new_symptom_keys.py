import json
import os

languages = [
    "as", "bn", "brx", "doi", "en", "gom", "gu", "hi", "kn", "ks", "mai", "ml", "mni",
    "mr", "ne", "or", "pa", "sa", "sat", "sd", "ta", "te", "ur"
]

data_dir = "/Users/udayaditya/Documents/MAA/data"

translations_detail = {
    "en": {
        "quick_log_title": "Quick Log Today",
        "save_symptoms": "Save Symptoms",
        "symptoms_saved_msg": "Symptom logs saved successfully!"
    },
    "hi": {
        "quick_log_title": "आज का त्वरित लॉग",
        "save_symptoms": "लक्षण सहेजें",
        "symptoms_saved_msg": "लक्षण सफलतापूर्वक सहेजे गए!"
    },
    "bn": {
        "quick_log_title": "আজকের দ্রুত লগ",
        "save_symptoms": "লক্ষণ সংরক্ষণ করুন",
        "symptoms_saved_msg": "লক্ষণ সফলভাবে সংরক্ষিত হয়েছে!"
    }
}

for lang in languages:
    filepath = os.path.join(data_dir, f"content_{lang}.json")
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found!")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        try:
            content = json.load(f)
        except Exception as e:
            print(f"Error parsing {filepath}: {e}")
            continue

    if "tracker" not in content:
        content["tracker"] = {}

    lang_translations = translations_detail.get(lang, translations_detail["en"])

    for k, v in lang_translations.items():
        content["tracker"][k] = v

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully backfilled symptom keys for: {lang}")

print("All done!")
