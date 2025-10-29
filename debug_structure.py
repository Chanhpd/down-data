import requests
from bs4 import BeautifulSoup
import re

url = "https://mandarinbean.com/h10901-listening/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

content = soup.find('div', class_='entry-content')
if content:
    # Get all paragraphs
    paras = content.find_all('p')
    print(f"Total paragraphs: {len(paras)}\n")
    
    print("=== Searching for patterns ===\n")
    for i, p in enumerate(paras[:50]):  # Check first 50
        text = p.get_text(strip=True)
        
        # Look for questions with numbers
        if re.match(r'^\s*\d+\s+', text) and len(text) > 10:
            print(f"Para {i}: {text[:150]}")
            print(f"  HTML: {str(p)[:200]}\n")
