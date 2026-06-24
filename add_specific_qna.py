import json

filepaths = [
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\qna.json",
    r"c:\Users\KIIT\Downloads\MAA (1)\MAA\data\qna.json"
]

new_entries = [
    {
        "questions": [
            "can you suggest some yoga postures during menstruation",
            "which yoga is best for periods",
            "yoga for period cramps",
            "yoga asanas during periods"
        ],
        "answer": "Yes, gentle yoga can significantly relieve period cramps and lower back pain. Some highly recommended postures include:\n\n1. **Child's Pose (Balasana):** Relaxes the lower back and pelvic muscles.\n2. **Cat-Cow Pose (Marjaryasana-Bitilasana):** Massages the abdominal organs and improves blood flow.\n3. **Knees-to-Chest (Apanasana):** Relieves lower back tension and bloating.\n4. **Corpse Pose (Savasana):** Calms the nervous system and helps manage stress and pain.\n\nAvoid strenuous poses, deep twists, or inversions (like headstands) if you feel uncomfortable.",
        "keywords": ["yoga", "postures", "asanas", "exercises", "cramps", "stretching", "childs pose", "cat cow"],
        "category": "Exercise & Lifestyle",
        "is_direct": True
    },
    {
        "questions": [
            "is there any particular sleep posture during period",
            "how to sleep during periods",
            "best sleeping position for period cramps",
            "sleep posture"
        ],
        "answer": "The best sleeping posture during your period is the **Fetal Position** (sleeping on your side with your legs tucked near your chest). \n\nThis position takes pressure off your abdominal muscles, which helps relieve cramps. Additionally, keeping your legs squeezed together can help prevent period leaks at night. Sleeping on your back with a pillow under your knees can also help reduce lower back pain.",
        "keywords": ["sleep", "posture", "position", "fetal", "sleeping", "night", "leaks"],
        "category": "Exercise & Lifestyle",
        "is_direct": True
    },
    {
        "questions": [
            "can diabetes have an effect on my menstrual flow",
            "periods and diabetes",
            "does blood sugar affect periods"
        ],
        "answer": "Yes, diabetes can have a significant effect on your menstrual flow. Women with diabetes (especially type 1 or uncontrolled type 2) are more likely to experience:\n\n1. **Irregular periods** or unpredictable cycles.\n2. **Heavier or longer periods** due to hormonal imbalances.\n3. **Increased risk of infections**, like yeast infections, especially just before a period.\n4. **Changes in blood sugar:** Hormone fluctuations during your period can make your blood sugar levels harder to control. It is very important to monitor your blood sugar closely during your cycle.",
        "keywords": ["diabetes", "sugar", "blood sugar", "diabetic", "flow", "irregular"],
        "category": "Health & Medical",
        "is_direct": True
    },
    {
        "questions": [
            "can high sugar be taken during menstruation",
            "can ice cream be taken during menstruation",
            "eating sweets during period",
            "sugar cravings"
        ],
        "answer": "While it's normal to crave sweets and ice cream during your period due to hormonal changes, consuming **high sugar or heavily processed sweets can actually worsen your symptoms**.\n\nHigh sugar intake causes spikes and crashes in your blood sugar, which worsens mood swings, fatigue, and can increase inflammation and cramps. Dairy (like in ice cream) can also trigger bloating and cramping in some women.\n\n**Better Alternatives:** Satisfy your cravings with natural sugars like dark chocolate (which helps cramps!), fruits (berries, bananas), or jaggery.",
        "keywords": ["sugar", "ice cream", "sweet", "sweets", "cravings", "chocolate"],
        "category": "Nutrition",
        "is_direct": True
    },
    {
        "questions": [
            "can indian spicy food be taken during menstruation",
            "eating spicy food during periods",
            "is spicy food bad for periods"
        ],
        "answer": "It is generally recommended to **avoid or limit highly spicy Indian food** during your period. \n\nSpicy foods can irritate your stomach lining and intestines, which are already sensitive due to the hormones (prostaglandins) released during your period. Eating overly spicy food can cause or worsen period diarrhea, stomach pain, acid reflux, and nausea. Opt for milder, warm, and easily digestible foods instead.",
        "keywords": ["spicy", "indian food", "spice", "chili", "stomach", "diarrhea"],
        "category": "Nutrition",
        "is_direct": True
    },
    {
        "questions": [
            "can coffee be taken during menstruation",
            "can too much caffeine be taken during menstruation",
            "drinking coffee on period",
            "caffeine during period"
        ],
        "answer": "You should limit your coffee and caffeine intake during your period. **Too much caffeine can make your symptoms worse.**\n\nCaffeine constricts your blood vessels, which can tighten the muscles in your uterus, leading to **worse cramps**. It can also increase anxiety, breast tenderness, and disrupt your sleep. If you need a warm drink, try switching to decaf coffee, green tea, or herbal teas like chamomile or ginger tea, which actually soothe cramps.",
        "keywords": ["coffee", "caffeine", "tea", "cramps", "anxiety", "drink"],
        "category": "Nutrition",
        "is_direct": True
    },
    {
        "questions": [
            "can pineapple be eaten during periods as it causes uterine wall contraction",
            "eating pineapple during periods",
            "does pineapple cause heavy bleeding"
        ],
        "answer": "Yes, you can eat pineapple during your period! In fact, it is very beneficial. \n\nPineapple contains an enzyme called **bromelain**, which actually helps to relax muscles and shed the uterine lining smoothly, **reducing period cramps**. While large amounts of bromelain might slightly increase your flow, eating normal portions of pineapple will not cause harmful uterine contractions. It is also rich in water and vitamins, which helps with bloating.",
        "keywords": ["pineapple", "bromelain", "contraction", "uterus", "fruits", "flow"],
        "category": "Nutrition",
        "is_direct": True
    },
    {
        "questions": [
            "during the second day of my period cycle I've to change the pad seven times in a day",
            "during the second day of my period cycle I've to change the pad five times in a day",
            "changing pad very frequently",
            "soaking pads fast"
        ],
        "answer": "Having to change your pad 5 to 7 times a day (especially if the pads are completely soaked) is a sign of **Menorrhagia (extremely heavy bleeding)**.\n\nWhile the first and second days are normally the heaviest, soaking through a regular pad or tampon every 1-2 hours is not normal. It can lead to severe fatigue and anemia (low iron). This heavy flow could be caused by hormonal imbalances, fibroids, polyps, or conditions like Adenomyosis. Please consult a gynecologist for a checkup.",
        "keywords": ["pad", "seven times", "five times", "change pad", "heavy bleeding", "menorrhagia", "soaking"],
        "category": "Health & Medical",
        "is_direct": True
    },
    {
        "questions": [
            "bloody lumps during the period",
            "during regular pad change i'm observing some bloody lumps in the pad",
            "blood clots during period",
            "large lumps of blood"
        ],
        "answer": "Those bloody lumps are called **blood clots**, and they are a normal part of the body's defense mechanism to control bleeding. \n\n**When it is normal:** Small clots (the size of a pea or a coin) are very common on the heaviest days of your period.\n**When to see a doctor:** If you are passing blood clots that are consistently larger than a large coin (like a quarter or a 10-rupee coin), or if they are accompanied by extremely heavy bleeding and severe pain, you should consult a gynecologist, as it could indicate an underlying issue like fibroids or hormonal imbalance.",
        "keywords": ["bloody lumps", "blood clots", "lumps", "clots", "heavy bleeding", "coin"],
        "category": "Health & Medical",
        "is_direct": True
    },
    {
        "questions": [
            "menstruating women shouldn't be allowed into temples",
            "taboos about periods and temples",
            "can i enter temple during period",
            "is period blood impure"
        ],
        "answer": "The belief that menstruating women shouldn't enter temples, kitchens, or religious spaces is a **cultural myth and taboo, not a scientific or religious fact**.\n\nMenstruation is a completely normal, healthy biological process that enables human reproduction. Period blood is not \"impure\" or \"dirty\"—it is just tissue and blood from the uterus. These ancient rules were often created before modern sanitary products existed. Medically and logically, there is absolutely no reason a menstruating woman should be restricted from any space.",
        "keywords": ["temples", "temple", "taboo", "myth", "impure", "dirty", "religious", "allowed"],
        "category": "Myths & Facts",
        "is_direct": True
    },
    {
        "questions": [
            "can muskmellon be eaten during menstruation",
            "can cucumber be eaten during menstruation",
            "should watermelon and cucumber be eaten during menstruation",
            "melons during period"
        ],
        "answer": "Yes, absolutely! Fruits with high water content like **watermelon, muskmelon, and cucumber are excellent to eat during your period.**\n\nDuring your period, your body retains water, causing you to feel bloated and puffy. Eating water-rich foods helps hydrate your body and signals it to release the retained water, significantly **reducing bloating**. They also provide natural sugars that satisfy cravings healthily.",
        "keywords": ["muskmelon", "cucumber", "watermelon", "melon", "fruits", "bloating", "hydration"],
        "category": "Nutrition",
        "is_direct": True
    },
    {
        "questions": [
            "frequent watery stool during menstruation",
            "diarrhea during period",
            "poop changes during period",
            "loose motion during periods"
        ],
        "answer": "Experiencing frequent watery stool (diarrhea) or loose motions during your period is **very common and completely normal**.\n\nRight before your period starts, your body releases chemicals called **prostaglandins**. These chemicals make your uterus contract (which causes cramps) to shed its lining. However, if your body produces too many prostaglandins, they can enter your bloodstream and cause your intestines to contract as well, leading to diarrhea. Staying hydrated and taking anti-inflammatory pain relief (like Ibuprofen) can help reduce this.",
        "keywords": ["watery stool", "diarrhea", "loose motion", "poop", "bowel", "prostaglandins", "stomach"],
        "category": "Health & Medical",
        "is_direct": True
    },
    {
        "questions": [
            "cloudy discharge during menstrual flow",
            "white discharge during periods",
            "cloudy fluid from vagina"
        ],
        "answer": "Vaginal discharge naturally changes throughout your menstrual cycle. \n\nSeeing **cloudy or white discharge** right before or just after your period is completely normal (it is called leukorrhea) and is just your body cleaning the vagina.\n\nHowever, if the cloudy discharge is accompanied by a foul (fishy) odor, itching, burning, or a cottage-cheese-like texture, it could be a sign of a vaginal infection (like Bacterial Vaginosis or a yeast infection). In that case, please consult a doctor.",
        "keywords": ["cloudy discharge", "white discharge", "fluid", "infection", "odor", "itching", "vagina"],
        "category": "Health & Medical",
        "is_direct": True
    }
]

for filepath in filepaths:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Append new entries
        for new_entry in new_entries:
            data.append(new_entry)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Added new specific Q&A entries to {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")
