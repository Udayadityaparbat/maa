import os
import re

file_path = r"c:\Users\KIIT\Downloads\MAA (1)\MAA\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update PDF links
content = content.replace("insights%20details/Many%20girls%20lack%20prior%20menstrual%20education%20before%20their%20first%20period..pdf", "insights-details/menstrual-education-gap.pdf")
content = content.replace("insights%20details/period_poverty_access.pdf", "insights-details/period-poverty-access.pdf")
content = content.replace("insights%20details/stigma_menstrual_silence.pdf", "insights-details/stigma-menstrual-silence.pdf")

# 2. Update Razorpay links
content = content.replace('href="https://rzp.io/rzp/maa-donation"', 'href="https://rzp.io/rzp/maa-donation?utm_source=maa_website&utm_medium=hero_cta&utm_campaign=donate_2026" rel="noopener noreferrer nofollow"')

# 3. Update external rel attributes
content = content.replace('rel="noopener"', 'rel="noopener noreferrer"')

# 4. Add lazy loading to images
images_to_lazy_load = [
    "BOARD1.JPG", "BOARD2.JPG", "BOARD3.JPG", "BOARD4.JPG",
    "Udayaditya.png", "Suvaiyu%20Saha.png", "Suraj%20Kumar%20Midya.png", "Anushka%20Chanda.png",
    "Rigel%20Logo.png"
]
for img in images_to_lazy_load:
    # Only replace if not already lazy loaded
    if f'src="media/{img}" alt=' in content:
        content = content.replace(f'src="media/{img}" alt=', f'src="media/{img}" loading="lazy" alt=')
    elif f'src="media/{img}"' in content:
        content = content.replace(f'src="media/{img}"', f'src="media/{img}" loading="lazy"')

# 5. Add aria labels to nav links
aria_mapping = {
    'href="#home"': 'href="#home" aria-label="Go to Home"',
    'href="#learn"': 'href="#learn" aria-label="Learn about menstrual health"',
    'href="#insights-pdf"': 'href="#insights-pdf" aria-label="View Research Insights"',
    'href="#tracker"': 'href="#tracker" aria-label="Free private period tracker tool"',
    'href="#qa"': 'href="#qa" aria-label="Anonymous Q&A"',
    'href="#schemes"': 'href="#schemes" aria-label="Government Schemes for Women"',
    'href="#impact"': 'href="#impact" aria-label="View our Impact"',
    'href="#research"': 'href="#research" aria-label="Data and Reports"',
    'href="#team"': 'href="#team" aria-label="Meet our Team"',
    'href="#community"': 'href="#community" aria-label="Join our Community"',
}
for k, v in aria_mapping.items():
    content = content.replace(k, v)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updates applied to index.html successfully.")
