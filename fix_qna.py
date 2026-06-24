import json
import os

filepath = "data/qna.json"
with open(filepath, "r", encoding="utf-8") as f:
    qna = json.load(f)

# Find the item with answer starting with "Menstruation, also called a \"period,\""
target_idx = -1
for i, item in enumerate(qna):
    if "also called a \"period,\"" in item.get("answer", "") or "What is menstruation?" in item.get("questions", [""])[0]:
        target_idx = i
        break

if target_idx != -1:
    target_item = qna.pop(target_idx)
    qna.insert(0, target_item)
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(qna, f, indent=2, ensure_ascii=False)
    print("Successfully moved the definition of period to the top of qna.json")
else:
    print("Could not find the definition of period in qna.json")
