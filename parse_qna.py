import json
import re

files = [
    'media/menstrual_health_QnA_dataset.txt',
    'media/menstrual_health_ADVANCED_dataset.txt',
    'media/dataset3.txt',
    'media/dataset4.txt',
    'media/direct_answers_dataset.txt'
]

questions = []

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Match standard QnA blocks
    blocks = re.findall(r'Q\d+:\s*(.*?)\nANSWER:\s*(.*?)\nKEYWORDS:\s*(.*?)\nSOURCE:', text, re.DOTALL)

    for q, a, kw in blocks:
        keywords = [k.strip() for k in kw.split(',')]
        questions.append({
            'question': q.strip(),
            'answer': a.strip(),
            'keywords': keywords
        })

    # Match DIRECT ANSWER blocks
    direct_blocks = re.findall(r'TRIGGER:\s*(.*?)\nCATEGORY:\s*(.*?)\nQUESTION:\s*(.*?)\nDIRECT ANSWER:\s*(.*?)\nDISCLAIMER:\s*(.*?)\nSOURCE:', text, re.DOTALL)
    
    for triggers, category, q, a, disclaimer in direct_blocks:
        keywords = [k.strip() for k in triggers.split(',')]
        full_answer = f"{a.strip()}\n\n{disclaimer.strip()}"
        questions.append({
            'question': q.strip(),
            'answer': full_answer,
            'keywords': keywords,
            'category': category.strip(),
            'is_direct': True
        })

with open('data/qna.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print(f"Parsed {len(questions)} questions in total")
