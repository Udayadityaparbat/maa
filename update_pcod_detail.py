import json

filepaths = [
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\qna.json",
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\data\qna.json"
]

detailed_answer = "**PCOD (Polycystic Ovarian Disease)**, also known as PCOS (Polycystic Ovary Syndrome) or PMOS, is a hormonal condition where the ovaries produce excess male hormones (androgens), which disrupts normal egg development and menstruation.\n\n**WHAT IS HAPPENING:**\nNormally, one egg matures and is released each month. In PCOD, the eggs do not fully mature \u2014 they remain as small cysts in the ovaries. This causes hormonal imbalance.\n\n**SYMPTOMS:**\n\u2022 Irregular periods or no periods\n\u2022 Acne and excessive facial or body hair (hirsutism)\n\u2022 Weight gain around the belly\n\u2022 Hair thinning\n\n**CAUSES & MANAGEMENT:**\nIt is mainly caused by insulin resistance and lifestyle factors. It cannot be cured but can be controlled through a low-glycemic diet, regular exercise, weight management, and medication prescribed by a doctor."

for filepath in filepaths:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        updated = False
        for entry in data:
            if "what is pcod?" in entry.get("questions", []):
                entry["answer"] = detailed_answer
                updated = True
                
        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Updated PCOD detailed answer in {filepath}")
        else:
            print(f"PCOD entry not found in {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")
