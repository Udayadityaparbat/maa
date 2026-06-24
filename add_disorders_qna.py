import json

filepaths = [
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\qna.json",
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\data\qna.json"
]

new_entries = [
    {
        "questions": [
            "What is PMOS?",
            "Polyendocrine Metabolic Ovarian Syndrome",
            "What is Polycystic Ovary Syndrome (PCOS)?",
            "PMOS definition",
            "Symptoms of PMOS or PCOS",
            "What does PMOS mean?"
        ],
        "answer": "**Polyendocrine Metabolic Ovarian Syndrome (PMOS) / Polycystic Ovary Syndrome (PCOS)** is a hormonal disorder causing enlarged ovaries with small cysts on the outer edges. It leads to irregular periods, excess hair growth, weight gain, acne, and sometimes fertility issues. It is one of the most common hormonal disorders in young women.",
        "keywords": ["pmos", "pcos", "syndrome", "hormonal", "cysts", "ovaries", "irregular periods", "weight gain"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Endometriosis?",
            "Definition of Endometriosis",
            "Symptoms of Endometriosis",
            "Why do I have chronic pelvic pain?",
            "What causes extremely painful periods?"
        ],
        "answer": "**Endometriosis** is a painful condition where tissue similar to the lining inside the uterus grows outside it, often on the ovaries or fallopian tubes. Symptoms include extremely painful periods, chronic pelvic pain, pain during bowel movements, heavy bleeding, and potentially infertility. Diagnosis often takes years because pain is frequently dismissed as 'normal'.",
        "keywords": ["endometriosis", "pelvic pain", "chronic pain", "painful periods", "heavy bleeding", "infertility"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Dysmenorrhea?",
            "Definition of Dysmenorrhea",
            "What does Dysmenorrhea mean?",
            "Severe cramps during periods",
            "Why are my cramps so bad?"
        ],
        "answer": "**Dysmenorrhea** refers to severe and frequent menstrual cramps and pelvic pain associated with menstruation that significantly interferes with daily activities. Symptoms include severe cramps, nausea, vomiting, fainting, and missing school or work. Many girls suffer silently thinking debilitating pain is completely normal.",
        "keywords": ["dysmenorrhea", "cramps", "severe cramps", "pain", "nausea", "fainting"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Menorrhagia?",
            "Definition of Menorrhagia",
            "What is heavy bleeding?",
            "Why is my period so heavy?",
            "Bleeding for more than 7 days"
        ],
        "answer": "**Menorrhagia** is characterized by menstrual periods with abnormally heavy or prolonged bleeding that can lead to fatigue, anemia, and disruption of normal life. Symptoms include bleeding for more than 7 days, soaking pads rapidly, passing blood clots, fatigue, and anemia. It can severely affect daily life and physical health.",
        "keywords": ["menorrhagia", "heavy bleeding", "prolonged bleeding", "blood clots", "anemia", "fatigue"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Amenorrhea?",
            "Definition of Amenorrhea",
            "Why did my periods stop?",
            "Never getting periods",
            "Absence of menstruation"
        ],
        "answer": "**Amenorrhea** is the absence of menstruation. It can be primary (never starting periods by age 15) or secondary (missing three or more periods in a row). It can be caused by stress, malnutrition, hormonal imbalance, excessive exercise, or PMOS. Absence of menstruation is a critical health indicator that requires medical attention.",
        "keywords": ["amenorrhea", "absence", "no period", "stopped period", "missing periods", "stress"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Adenomyosis?",
            "Definition of Adenomyosis",
            "Uterine Disorder definition",
            "What causes an enlarged uterus?"
        ],
        "answer": "**Adenomyosis** is a condition where the inner lining of the uterus breaks through the muscle wall of the uterus. It causes heavy bleeding, severe cramps, an enlarged uterus, and lower abdominal pressure/pelvic pressure. It is often confused with normal period pain, leading to delayed diagnosis.",
        "keywords": ["adenomyosis", "uterus", "enlarged uterus", "pelvic pressure", "heavy bleeding", "cramps"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Premenstrual Syndrome?",
            "What is PMS?",
            "Definition of PMS",
            "Symptoms of PMS"
        ],
        "answer": "**Premenstrual Syndrome (PMS)** is a common combination of physical and emotional symptoms that occur 1 to 2 weeks before menstruation. Symptoms include mood swings, irritability, tender breasts, bloating, food cravings, fatigue, and depression. It is very common but often misunderstood or trivialized by society.",
        "keywords": ["pms", "premenstrual syndrome", "mood swings", "irritability", "bloating", "tender breasts"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What is Premenstrual Dysphoric Disorder?",
            "What is PMDD?",
            "Definition of PMDD",
            "Severe depression before periods",
            "Extreme mood swings before periods"
        ],
        "answer": "**Premenstrual Dysphoric Disorder (PMDD)** is a severe, sometimes disabling extension of premenstrual syndrome (PMS). It causes extreme mood shifts that can disrupt work and damage relationships. Symptoms include severe depression, extreme anxiety, anger, irritability, and emotional instability. It is a serious condition that affects mental health significantly and requires support.",
        "keywords": ["pmdd", "premenstrual dysphoric disorder", "depression", "anxiety", "mood shifts", "mental health"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What are Uterine Fibroids?",
            "Definition of Uterine Fibroids",
            "Growths in uterus",
            "Are fibroids cancerous?"
        ],
        "answer": "**Uterine Fibroids** are noncancerous growths of the uterus that often appear during childbearing years. They aren't associated with an increased risk of uterine cancer and almost never develop into cancer. Symptoms include heavy bleeding, pelvic pain, frequent urination, and unusually long periods.",
        "keywords": ["fibroids", "uterine fibroids", "growths", "pelvic pain", "heavy bleeding", "noncancerous"],
        "category": "Disorders",
        "is_direct": True
    },
    {
        "questions": [
            "What are Irregular Menstrual Cycles?",
            "Irregular periods",
            "Why is my cycle length different every month?",
            "Causes of irregular periods"
        ],
        "answer": "**Irregular Menstrual Cycles** occur when the length of the cycle varies significantly from month to month. This can be caused by various factors including stress, diet, extreme exercise, or underlying conditions like PMOS/PCOS or thyroid issues.",
        "keywords": ["irregular", "irregular cycles", "irregular periods", "cycle length", "stress", "thyroid"],
        "category": "Disorders",
        "is_direct": True
    }
]

for filepath in filepaths:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Append only if not already present based on category/first question
        for new_entry in new_entries:
            data.append(new_entry)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Added Q&A entries successfully to {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")
