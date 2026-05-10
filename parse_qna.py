import json
import re

files = [
    'media/menstrual_health_QnA_dataset.txt',
    'media/menstrual_health_ADVANCED_dataset.txt'
]

questions = []

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Match blocks of Q, ANSWER, KEYWORDS
    blocks = re.findall(r'Q\d+:\s*(.*?)\nANSWER:\s*(.*?)\nKEYWORDS:\s*(.*?)\nSOURCE:', text, re.DOTALL)

    for q, a, kw in blocks:
        keywords = [k.strip() for k in kw.split(',')]
        questions.append({
            'question': q.strip(),
            'answer': a.strip(),
            'keywords': keywords
        })

with open('data/qna.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Parsed {len(questions)} questions in total")
