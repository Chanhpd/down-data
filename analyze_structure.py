#!/usr/bin/env python3
"""Analyze the page structure to understand question format"""
import requests
from bs4 import BeautifulSoup
import json

url = "https://mandarinbean.com/h10901-listening/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

# Find the form with questions
form = soup.find('form', {'name': 'watupro_form'})
if not form:
    print("No watupro form found, searching for alternatives...")
    form = soup.find('form')

if form:
    print("=== FORM FOUND ===")
    
    # Look for parts (Part 1, Part 2, etc.)
    parts = []
    for elem in form.find_all(['h3', 'h4', 'strong', 'p']):
        text = elem.get_text(strip=True)
        if 'part' in text.lower() and any(str(i) in text for i in range(1, 6)):
            parts.append((elem.name, text))
            print(f"Part found: {text}")
    
    # Look for questions - typically in <p> or <div> with radio/checkbox inputs
    questions = []
    for p in form.find_all(['p', 'div']):
        # Check if this element contains input elements (radio or checkbox)
        inputs = p.find_all('input', {'type': ['radio', 'checkbox']})
        if inputs:
            # Get question text
            q_text = p.get_text(separator=' ', strip=True)[:200]
            
            # Get associated image if any
            img = p.find_previous('img') or p.find('img') or p.find_next('img')
            img_src = img.get('src') if img else None
            
            # Get answer options
            labels = p.find_all('label')
            options = []
            for label in labels:
                opt_text = label.get_text(strip=True)
                opt_input = label.find('input')
                if opt_input:
                    options.append({
                        'value': opt_input.get('value', ''),
                        'text': opt_text
                    })
            
            questions.append({
                'text': q_text,
                'image': img_src,
                'options': options,
                'input_name': inputs[0].get('name', '') if inputs else ''
            })
    
    print(f"\n=== Found {len(questions)} questions ===\n")
    
    # Show first 3 questions as examples
    for i, q in enumerate(questions[:3], 1):
        print(f"\nQuestion {i}:")
        print(f"  Input name: {q['input_name']}")
        print(f"  Text: {q['text'][:100]}...")
        print(f"  Image: {q['image']}")
        print(f"  Options: {len(q['options'])}")
        for opt in q['options'][:3]:
            print(f"    - {opt['value']}: {opt['text'][:50]}")
    
    # Save to JSON for inspection
    with open('questions_structure.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Saved all {len(questions)} questions to questions_structure.json")
else:
    print("No form found on page!")
