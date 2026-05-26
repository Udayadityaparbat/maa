import json
import os

languages = [
    "as", "bn", "brx", "doi", "en", "gom", "gu", "hi", "kn", "ks", "mai", "ml", "mni",
    "mr", "ne", "or", "pa", "sa", "sat", "sd", "ta", "te", "ur"
]

data_dir = "/Users/udayaditya/Documents/MAA/data"

# Human translations for en, hi, bn
translations_detail = {
    "en": {
        "generate_report_btn": "Generate Doctor Report",
        "clinical_report_title": "Maa Menstrual Health Clinical Report",
        "clinical_report_subtitle": "Prepared confidentially on device for medical consultation",
        "confidential_badge": "Patient Confidential",
        "patient_info": "Patient Information",
        "age": "Age",
        "height": "Height",
        "weight": "Weight",
        "bmi": "Calculated BMI",
        "generated_on": "Generated On",
        "cycle_stats": "Cycle Baseline Statistics",
        "avg_cycle_len": "Average Cycle Length",
        "avg_flow_len": "Average Period Flow",
        "cycle_regularity": "Cycle Regularity Score",
        "symptom_frequency_distribution": "Symptom Phase Frequency Distribution",
        "heatmap_print_desc": "Shows symptom distribution across menstrual cycle phases (normalized percentage within each symptom category).",
        "last_six_cycles": "Cycle Duration History",
        "three_month_forecast": "Three-Month Clinical Forecast",
        "print_footer_note": "Maa Menstrual Health Tracker is a client-side health tool. All data remains strictly local and private. Sharing this report with your healthcare provider can assist in clinical consultations.",
        "days": "days",
        "regularity_highly_regular": "Highly Regular",
        "regularity_regular": "Regular",
        "regularity_irregular": "Highly Irregular",
        "symptom_cramps": "Cramps",
        "symptom_headache": "Headache",
        "symptom_bloating": "Bloating",
        "symptom_fatigue": "Fatigue",
        "symptom_happy": "Happy",
        "symptom_sad": "Sad"
    },
    "hi": {
        "generate_report_btn": "डॉक्टर रिपोर्ट बनाएं",
        "clinical_report_title": "माँ मासिक धर्म स्वास्थ्य क्लिनिकल रिपोर्ट",
        "clinical_report_subtitle": "चिकित्सीय परामर्श के लिए डिवाइस पर गोपनीय रूप से तैयार",
        "confidential_badge": "मरीज का विवरण गोपनीय",
        "patient_info": "मरीज की जानकारी",
        "age": "उम्र",
        "height": "ऊंचाई",
        "weight": "वजन",
        "bmi": "गणना की गई बीएमआई (BMI)",
        "generated_on": "तैयार होने की तिथि",
        "cycle_stats": "मासिक चक्र के मूल आंकड़े",
        "avg_cycle_len": "औसत चक्र की लंबाई",
        "avg_flow_len": "औसत स्राव की अवधि",
        "cycle_regularity": "चक्र की नियमितता स्कोर",
        "symptom_frequency_distribution": "लक्षण चरण आवृत्ति वितरण",
        "heatmap_print_desc": "मासिक धर्म चक्र के विभिन्न चरणों में लक्षणों के वितरण को दिखाता है (प्रत्येक लक्षण श्रेणी में सामान्यीकृत प्रतिशत)।",
        "last_six_cycles": "चक्र अवधि इतिहास",
        "three_month_forecast": "तीन महीने का चिकित्सीय पूर्वानुमान",
        "print_footer_note": "माँ मासिक धर्म स्वास्थ्य ट्रैकर एक क्लाइंट-साइड स्वास्थ्य उपकरण है। सभी डेटा पूरी तरह से स्थानीय और गोपनीय रहते हैं। इस रिपोर्ट को अपने डॉक्टर के साथ साझा करने से चिकित्सीय परामर्श में मदद मिल सकती है।",
        "days": "दिन",
        "regularity_highly_regular": "अत्यधिक नियमित",
        "regularity_regular": "नियमित",
        "regularity_irregular": "अत्यधिक अनियमित",
        "symptom_cramps": "ऐंठन (Cramps)",
        "symptom_headache": "सिरदर्द",
        "symptom_bloating": "पेट फूलना (Bloating)",
        "symptom_fatigue": "थकान",
        "symptom_happy": "खुश",
        "symptom_sad": "उदास"
    },
    "bn": {
        "generate_report_btn": "ডাক্তার রিপোর্ট তৈরি করুন",
        "clinical_report_title": "মা ঋতুস্রাব স্বাস্থ্য ক্লিনিক্যাল রিপোর্ট",
        "clinical_report_subtitle": "চিকিৎসকের পরামর্শের জন্য ডিভাইসে গোপনীয়ভাবে প্রস্তুত",
        "confidential_badge": "রোগীর তথ্য গোপনীয়",
        "patient_info": "রোগীর তথ্য",
        "age": "বয়স",
        "height": "উচ্চতা",
        "weight": "ওজন",
        "bmi": "হিসাবকৃত বিএমআই (BMI)",
        "generated_on": "তৈরির তারিখ",
        "cycle_stats": "ঋতুচক্রের মূল পরিসংখ্যান",
        "avg_cycle_len": "গড় ঋতুচক্রের দৈর্ঘ্য",
        "avg_flow_len": "গড় ঋতুস্রাবের সময়কাল",
        "cycle_regularity": "ঋতুচক্রের নিয়মিততার স্কোর",
        "symptom_frequency_distribution": "লক্ষণ পর্যায় ফ্রিকোয়েন্সি বিন্যাস",
        "heatmap_print_desc": "ঋতুচক্রের বিভিন্ন পর্যায়ে লক্ষণের উপস্থিতি প্রদর্শন করে (প্রতিটি লক্ষণ বিভাগের মধ্যে স্বাভাবিক শতাংশ)।",
        "last_six_cycles": "ঋতুচক্রের সময়কালের ইতিহাস",
        "three_month_forecast": "তিন মাসের ক্লিনিক্যাল পূর্বাভাস",
        "print_footer_note": "মা ঋতুস্রাব স্বাস্থ্য ট্র্যাকার একটি ক্লায়েন্ট-সাইড স্বাস্থ্য সরঞ্জাম। সমস্ত তথ্য সম্পূর্ণরূপে স্থানীয় এবং গোপনীয় থাকে। এই রিপোর্টটি আপনার ডাক্তারের সাথে শেয়ার করা চিকিৎসকের পরামর্শে সহায়ক হতে পারে।" ,
        "days": "দিন",
        "regularity_highly_regular": "অত্যন্ত নিয়মিত",
        "regularity_regular": "নিয়মিত",
        "regularity_irregular": "অত্যন্ত অনিয়মিত",
        "symptom_cramps": "পেটে টান (Cramps)",
        "symptom_headache": "মাথাব্যথা",
        "symptom_bloating": "পেট ফাঁপা (Bloating)",
        "symptom_fatigue": "ক্লান্তি",
        "symptom_happy": "খুশি",
        "symptom_sad": "বিষণ্ণ"
    }
}

# Run through all 23 language files
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

    # Get localizations (or fallback to English)
    lang_translations = translations_detail.get(lang, translations_detail["en"])

    # Update tracker namespace
    for k, v in lang_translations.items():
        content["tracker"][k] = v

    # Write back keeping clean formatted layout
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully backfilled report translations for: {lang}")

print("Translation backfilling complete!")
