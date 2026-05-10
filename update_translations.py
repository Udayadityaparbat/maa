import json
import glob
import os

missing_keys = {
  "hygiene_kit": {
    "title": "What's in a Hygiene Kit?",
    "subtitle": "Essential items distributed in rural schools to support menstrual health."
  },
  "teacher_corner": {
    "title": "School & Teacher Corner",
    "subtitle": "Resources and guidelines for educators to support students."
  },
  "myth_quiz": {
    "title": "Myth vs Fact",
    "subtitle": "Click to flip and reveal the truth."
  },
  "ministry": {
    "title": "Ministry of Women & Child Development",
    "subtitle": "Official Government of India schemes for women's health, safety, and empowerment. Access support, subsidised products, and crisis helplines."
  },
  "research": {
    "title": "Research Insights",
    "subtitle": "Key findings from our published public health reports on menstrual equity."
  }
}

for filepath in glob.glob("data/content_*.json"):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    changed = False
    for section, keys in missing_keys.items():
        if section not in data:
            data[section] = {}
        for k, v in keys.items():
            if k not in data[section]:
                data[section][k] = v
                changed = True
                
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {filepath}")
    else:
        print(f"No changes needed for {filepath}")
