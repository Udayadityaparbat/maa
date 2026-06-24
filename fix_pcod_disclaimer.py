import json

filepaths = [
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\qna.json",
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\data\qna.json"
]

disclaimer = "\n\nThis website is only for general suggestion. Please consult your nearest gynecologist. Tracking your symptoms daily can also help you understand your cycle better."

for filepath in filepaths:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = False
        for entry in data:
            if "No, they are the exact same condition! PMOS" in entry.get("answer", ""):
                if entry["answer"].endswith(disclaimer):
                    entry["answer"] = entry["answer"].replace(disclaimer, "")
                    updated = True
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Fixed duplicate disclaimer in {filepath}")
        else:
            print(f"Disclaimer not found or already fixed in {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")
