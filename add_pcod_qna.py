import json

filepaths = [
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\qna.json",
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\data\qna.json"
]

new_entry = {
    "questions": [
        "what is pcod?",
        "is pcod the same as pcos?",
        "is pmos different from pcos?",
        "difference between pcos and pmos"
    ],
    "answer": "No, they are the exact same condition! PMOS (Polyendocrine Metabolic Ovarian Syndrome) is simply the new, updated medical name for PCOS (Polycystic Ovary Syndrome).\n\nMedical professionals are transitioning to the name PMOS because the old name (PCOS) implies the main problem is 'cysts' on the ovaries. In reality, it is a full-body hormonal and metabolic disorder that affects insulin, weight, and androgens. The new name PMOS much better reflects what is actually happening in the body.\n\nThis website is only for general suggestion. Please consult your nearest gynecologist. Tracking your symptoms daily can also help you understand your cycle better.",
    "keywords": ["pcod", "pcos", "pmos", "difference", "same", "medical name", "cysts", "hormonal", "metabolic"],
    "category": "Disorders",
    "is_direct": True
}

for filepath in filepaths:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        data.append(new_entry)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Added PCOD/PCOS Q&A entry successfully to {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")
