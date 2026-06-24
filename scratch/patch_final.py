import os

file_path = r'c:\Users\KIIT\Downloads\MAA (1)\MAA\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'google-site-verification' not in content:
    content = content.replace('</head>', '  <!-- Google Search Console -->\n  <meta name="google-site-verification" content="PASTE_YOUR_CODE_HERE" />\n</head>')

replacements = {
    'href="#learn" aria-label="Learn about menstrual health"': 'href="#learn" aria-label="Learn about menstrual health" title="Menstrual health education in 22 Indian languages"',
    'href="#tracker" aria-label="Free private period tracker tool"': 'href="#tracker" aria-label="Free private period tracker tool" title="Free private period tracker — no login required"',
    'href="#qa" aria-label="Anonymous Q&A"': 'href="#qa" aria-label="Anonymous Q&A" title="Ask menstrual health questions anonymously"',
    'href="#schemes" aria-label="Government Schemes for Women"': 'href="#schemes" aria-label="Government Schemes for Women" title="Government of India schemes for women\'s health"'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated nav titles and meta tag")
