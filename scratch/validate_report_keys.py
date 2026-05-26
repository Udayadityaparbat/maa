import os
import json

data_dir = '/Users/udayaditya/Documents/MAA/data'
languages_path = os.path.join(data_dir, 'languages.json')

with open(languages_path, 'r', encoding='utf-8') as f:
    languages_data = json.load(f)

languages = [lang['code'] for lang in languages_data['languages']]

new_report_keys = [
    "generate_report_btn",
    "clinical_report_title",
    "clinical_report_subtitle",
    "confidential_badge",
    "patient_info",
    "age",
    "height",
    "weight",
    "bmi",
    "generated_on",
    "cycle_stats",
    "avg_cycle_len",
    "avg_flow_len",
    "cycle_regularity",
    "symptom_frequency_distribution",
    "heatmap_print_desc",
    "last_six_cycles",
    "three_month_forecast",
    "print_footer_note",
    "days",
    "regularity_highly_regular",
    "regularity_regular",
    "regularity_irregular",
    "symptom_cramps",
    "symptom_headache",
    "symptom_bloating",
    "symptom_fatigue",
    "symptom_happy",
    "symptom_sad"
]

print(f"Validating {len(languages)} languages for new clinical report keys...")
success = True

for lang in languages:
    content_file = os.path.join(data_dir, f'content_{lang}.json')
    if not os.path.exists(content_file):
        print(f"ERROR: {content_file} does not exist!")
        success = False
        continue
    
    try:
        with open(content_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR parsing {content_file}: {e}")
        success = False
        continue
        
    if 'tracker' not in data:
        print(f"ERROR: 'tracker' namespace missing in {lang}")
        success = False
    else:
        for k in new_report_keys:
            if k not in data['tracker']:
                print(f"ERROR: missing clinical report key '{k}' in {lang}")
                success = False

if success:
    print("ALL 23 LANGUAGE JSON FILES HAVE ALL CLINICAL REPORT KEYS PROPERLY SET!")
else:
    print("VALIDATION FAILED - MISSING KEYS FOUND.")
