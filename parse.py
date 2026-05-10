data_str1 = """CONDITION: PCOD / PCOS

KEYWORDS: pcod, pcos, irregular periods
DESCRIPTION: Hormonal disorder affecting ovulation
SYMPTOMS: irregular periods, acne, weight gain
CAUSES: insulin resistance, hormones
RECOMMENDATION: exercise, diet, doctor
RISK_LEVEL: medium
DOCTOR_REQUIRED: yes

CONDITION: IRREGULAR PERIODS

KEYWORDS: delayed periods
DESCRIPTION: Inconsistent cycle timing
SYMPTOMS: late or missed periods
CAUSES: stress, hormones
RECOMMENDATION: track cycle
RISK_LEVEL: medium

CONDITION: DYSMENORRHEA

KEYWORDS: period pain
DESCRIPTION: Painful menstruation
SYMPTOMS: cramps, nausea
CAUSES: prostaglandins
RECOMMENDATION: heat therapy
RISK_LEVEL: low

CONDITION: PMS

KEYWORDS: mood swings
DESCRIPTION: Pre-period symptoms
SYMPTOMS: irritability, bloating
CAUSES: hormones
RECOMMENDATION: rest, exercise
RISK_LEVEL: low

CONDITION: PMDD

KEYWORDS: severe pms
DESCRIPTION: Severe emotional symptoms
SYMPTOMS: depression, anxiety
CAUSES: hormone sensitivity
RECOMMENDATION: doctor
RISK_LEVEL: high

CONDITION: HEAVY BLEEDING

KEYWORDS: heavy flow
DESCRIPTION: Excessive menstrual bleeding
SYMPTOMS: long periods
CAUSES: fibroids
RECOMMENDATION: iron, doctor
RISK_LEVEL: high

CONDITION: LIGHT PERIODS

KEYWORDS: low flow
DESCRIPTION: Reduced bleeding
SYMPTOMS: short periods
CAUSES: hormones
RECOMMENDATION: monitor
RISK_LEVEL: low

CONDITION: AMENORRHEA

KEYWORDS: no periods
DESCRIPTION: Absence of menstruation
SYMPTOMS: missed cycles
CAUSES: stress, weight
RECOMMENDATION: doctor
RISK_LEVEL: high

CONDITION: ENDOMETRIOSIS

KEYWORDS: severe cramps
DESCRIPTION: Tissue outside uterus
SYMPTOMS: pain, infertility
CAUSES: unknown
RECOMMENDATION: treatment
RISK_LEVEL: high

CONDITION: FIBROIDS

KEYWORDS: uterine growth
DESCRIPTION: Non-cancerous tumors
SYMPTOMS: heavy bleeding
CAUSES: hormones
RECOMMENDATION: doctor
RISK_LEVEL: medium

CONDITION: OVARIAN CYST

KEYWORDS: cyst
DESCRIPTION: Fluid-filled sacs
SYMPTOMS: pain
CAUSES: hormones
RECOMMENDATION: monitor
RISK_LEVEL: medium

CONDITION: THYROID ISSUE

KEYWORDS: thyroid
DESCRIPTION: Hormone imbalance
SYMPTOMS: fatigue, irregular cycle
CAUSES: thyroid dysfunction
RECOMMENDATION: test
RISK_LEVEL: medium

CONDITION: ANEMIA

KEYWORDS: low iron
DESCRIPTION: Low hemoglobin
SYMPTOMS: fatigue
CAUSES: blood loss
RECOMMENDATION: iron
RISK_LEVEL: medium

CONDITION: INFERTILITY

KEYWORDS: cannot conceive
DESCRIPTION: Difficulty pregnancy
SYMPTOMS: irregular ovulation
CAUSES: PCOS
RECOMMENDATION: specialist
RISK_LEVEL: high

CONDITION: VAGINAL INFECTION

KEYWORDS: itching
DESCRIPTION: Infection
SYMPTOMS: discharge
CAUSES: bacteria
RECOMMENDATION: hygiene
RISK_LEVEL: medium

CONDITION: YEAST INFECTION

KEYWORDS: fungal
DESCRIPTION: Fungal infection
SYMPTOMS: itching
CAUSES: imbalance
RECOMMENDATION: antifungal
RISK_LEVEL: low

CONDITION: BACTERIAL VAGINOSIS

KEYWORDS: odor
DESCRIPTION: Bacterial imbalance
SYMPTOMS: smell
CAUSES: bacteria
RECOMMENDATION: antibiotics
RISK_LEVEL: medium

CONDITION: PELVIC PAIN

KEYWORDS: lower pain
DESCRIPTION: Pain in pelvis
SYMPTOMS: discomfort
CAUSES: infection
RECOMMENDATION: diagnosis
RISK_LEVEL: medium

CONDITION: STRESS EFFECT

KEYWORDS: stress delay
DESCRIPTION: Stress affects cycle
SYMPTOMS: late period
CAUSES: cortisol
RECOMMENDATION: relax
RISK_LEVEL: low

CONDITION: WEIGHT GAIN

KEYWORDS: weight increase
DESCRIPTION: Hormonal weight gain
SYMPTOMS: fat gain
CAUSES: PCOS
RECOMMENDATION: diet
RISK_LEVEL: medium

CONDITION: ACNE

KEYWORDS: pimples
DESCRIPTION: Hormonal acne
SYMPTOMS: breakouts
CAUSES: hormones
RECOMMENDATION: skincare
RISK_LEVEL: low

CONDITION: HAIR LOSS

KEYWORDS: hair fall
DESCRIPTION: Hair thinning
SYMPTOMS: hair loss
CAUSES: hormones
RECOMMENDATION: nutrition
RISK_LEVEL: low

CONDITION: MOOD SWINGS

KEYWORDS: emotional
DESCRIPTION: Emotional fluctuation
SYMPTOMS: irritability
CAUSES: hormones
RECOMMENDATION: rest
RISK_LEVEL: low

CONDITION: FATIGUE

KEYWORDS: tired
DESCRIPTION: Low energy
SYMPTOMS: weakness
CAUSES: blood loss
RECOMMENDATION: rest
RISK_LEVEL: low

CONDITION: SLEEP ISSUES

KEYWORDS: insomnia
DESCRIPTION: Sleep disturbance
SYMPTOMS: poor sleep
CAUSES: hormones
RECOMMENDATION: routine
RISK_LEVEL: low

CONDITION: BLOATING

KEYWORDS: swelling
DESCRIPTION: Fluid retention
SYMPTOMS: stomach swelling
CAUSES: hormones
RECOMMENDATION: reduce salt
RISK_LEVEL: low

CONDITION: BREAST PAIN

KEYWORDS: tenderness
DESCRIPTION: Breast soreness
SYMPTOMS: pain
CAUSES: hormones
RECOMMENDATION: support
RISK_LEVEL: low

CONDITION: BACK PAIN

KEYWORDS: back ache
DESCRIPTION: Pain during cycle
SYMPTOMS: lower back pain
CAUSES: cramps
RECOMMENDATION: heat
RISK_LEVEL: low

CONDITION: NAUSEA

KEYWORDS: vomiting
DESCRIPTION: Nausea during period
SYMPTOMS: vomiting
CAUSES: hormones
RECOMMENDATION: light diet
RISK_LEVEL: low

CONDITION: DIARRHEA

KEYWORDS: loose motion
DESCRIPTION: Digestive change
SYMPTOMS: diarrhea
CAUSES: prostaglandins
RECOMMENDATION: hydration
RISK_LEVEL: low

CONDITION: CONSTIPATION

KEYWORDS: hard stool
DESCRIPTION: Slow digestion
SYMPTOMS: constipation
CAUSES: hormones
RECOMMENDATION: fiber
RISK_LEVEL: low"""

data_str2 = """SPOTTING — light bleeding — hormones — monitor — low
EARLY PERIOD — early cycle — stress — monitor — low
LATE PERIOD — delayed — stress — monitor — medium
OVULATION PAIN — mid pain — ovulation — rest — low
LOW LIBIDO — low sex drive — hormones — lifestyle — low
HIGH LIBIDO — high drive — hormones — normal — low
NIGHT SWEATS — sweating — hormones — monitor — low
HOT FLASHES — heat waves — hormones — lifestyle — low
CHILLS — cold feeling — hormones — rest — low
HEADACHE — pain — hormones — rest — low
MIGRAINE — severe headache — hormones — doctor — medium
DIZZINESS — lightheaded — low iron — nutrition — medium
CRAVINGS — food craving — hormones — diet — low
LOSS OF APPETITE — low hunger — stress — monitor — low
WATER RETENTION — swelling — hormones — hydration — low
SKIN DARKENING — pigmentation — hormones — care — low
BODY ODOR — smell change — hormones — hygiene — low
SWEATING — excess sweat — hormones — care — low
ANXIETY — nervousness — hormones — relax — medium
DEPRESSION — sadness — hormones — doctor — high
IRRITABILITY — anger — hormones — rest — low
LOW FOCUS — distraction — hormones — sleep — low
MEMORY ISSUES — forgetfulness — hormones — rest — low
JOINT PAIN — pain — hormones — exercise — low
MUSCLE PAIN — soreness — hormones — rest — low
LOW IMMUNITY — weak immune — stress — nutrition — medium
FREQUENT URINATION — urination — infection — doctor — medium
URINARY INFECTION — UTI — bacteria — antibiotics — medium
PELVIC INFLAMMATION — inflammation — infection — doctor — high
CERVICAL ISSUES — cervix problem — infection — doctor — high
HORMONAL IMBALANCE — imbalance — endocrine — doctor — medium
DELAYED OVULATION — late ovulation — hormones — monitor — medium
NO OVULATION — anovulation — PCOS — doctor — high
SHORT CYCLE — <21 days — hormones — monitor — low
LONG CYCLE — >35 days — hormones — doctor — medium
BLEEDING BETWEEN PERIODS — spotting — hormones — doctor — medium
POST PERIOD PAIN — pain after — inflammation — monitor — low
PRE PERIOD PAIN — pain before — PMS — rest — low
LOW ESTROGEN — hormone low — fatigue — doctor — medium
HIGH ESTROGEN — hormone high — weight — doctor — medium
LOW PROGESTERONE — hormone low — irregular — doctor — medium
HIGH PROGESTERONE — hormone high — mood — monitor — low
HIGH LH — ovulation issue — hormones — monitor — medium
LOW LH — ovulation issue — hormones — monitor — medium
INSULIN RESISTANCE — metabolism — PCOS — diet — high
METABOLIC ISSUE — metabolism — hormones — doctor — high
OBESITY — weight — lifestyle — exercise — medium
UNDERWEIGHT — low weight — nutrition — diet — medium
EATING DISORDER — unhealthy eating — stress — doctor — high
DEHYDRATION — low water — fatigue — hydrate — low
OVEREXERCISE — too much workout — hormones — rest — low
NO EXERCISE — inactivity — health — exercise — low
POOR DIET — junk food — health — improve — low
LOW IRON — deficiency — anemia — iron — medium
VITAMIN DEFICIENCY — lack nutrients — fatigue — supplements — medium
SLEEP DEPRIVATION — less sleep — fatigue — sleep — low
SHIFT WORK IMPACT — irregular routine — hormones — adjust — low
TRAVEL IMPACT — jet lag — cycle shift — adjust — low
MEDICATION EFFECT — drug impact — hormones — consult — medium
CONTRACEPTIVE EFFECT — pills impact — hormones — monitor — medium
POST PILL EFFECT — after pills — irregular — monitor — medium
PREGNANCY POSSIBILITY — missed period — test — doctor — high
MISCARRIAGE RISK — bleeding — pregnancy — doctor — high
POST PREGNANCY IRREGULARITY — after birth — hormones — monitor — medium
BREASTFEEDING IMPACT — cycle delay — hormones — normal — low
MENOPAUSE START — end of cycle — hormones — doctor — medium
PERIMENOPAUSE — transition — hormones — monitor — medium
LOW AWARENESS — lack knowledge — education — improve — low
HYGIENE ISSUE — poor hygiene — infection — improve — medium
SOCIAL STIGMA — taboo — mental impact — awareness — low"""

import json

items = []
current_item = {}
for line in data_str1.split('\n'):
    line = line.strip()
    if not line: continue
    if line.startswith('CONDITION:'):
        if current_item: items.append(current_item)
        current_item = {'condition': line.replace('CONDITION:', '').strip()}
    elif ':' in line:
        k, v = line.split(':', 1)
        k = k.lower().strip()
        v = v.strip()
        if k == 'keywords': v = [x.strip() for x in v.split(',')]
        if k == 'doctor_required': v = v.lower() == 'yes'
        current_item[k] = v
if current_item: items.append(current_item)

for line in data_str2.split('\n'):
    line = line.strip()
    if not line: continue
    parts = [p.strip() for p in line.split('—')]
    if len(parts) >= 5:
        items.append({
            'condition': parts[0],
            'keywords': [x.strip() for x in parts[1].split(',')],
            'causes': parts[2],
            'recommendation': parts[3],
            'risk_level': parts[4],
            'description': parts[0]
        })

print(json.dumps(items, indent=2))
