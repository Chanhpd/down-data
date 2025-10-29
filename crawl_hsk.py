#!/usr/bin/env python3
"""
crawl_hsk.py

Advanced scraper to extract structured HSK exam data with parts, questions, images, and answers.

Usage:
    python crawl_hsk.py --url "https://mandarinbean.com/h10901-listening/"

Outputs: output.json with structured format for API consumption
"""
import argparse
import json
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString


def is_media_url(u: str) -> bool:
    if not u:
        return False
    u = u.split('?')[0].lower()
    return any(u.endswith(ext) for ext in ('.mp3', '.wav', '.m4a', '.ogg'))


def get_audio_links(soup: BeautifulSoup, base: str):
    links = set()
    for src in soup.select('audio source'):
        s = src.get('src')
        if s:
            links.add(urljoin(base, s))
    for audio in soup.find_all('audio'):
        s = audio.get('src')
        if s:
            links.add(urljoin(base, s))
    for a in soup.find_all('a', href=True):
        href = a['href']
        if is_media_url(href):
            links.add(urljoin(base, href))
    for tag in soup.find_all(True):
        for k, v in tag.attrs.items():
            if isinstance(v, str) and is_media_url(v):
                links.add(urljoin(base, v))
    return sorted(links)


def extract_questions_structured(soup: BeautifulSoup, base_url: str):
    """
    Extract questions organized by parts with proper structure for API
    """
    content = soup.find('div', class_='entry-content') or soup.find('article') or soup
    
    parts = []
    current_part = None
    current_part_num = 0
    question_counter = 1
    
    # Find all elements in order
    for elem in content.find_all(['p', 'h3', 'h4', 'strong', 'img']):
        text = elem.get_text(strip=True) if not elem.name == 'img' else ''
        
        # Detect part headers (第一部分, 第二部分, etc. or Part 1, Part 2)
        part_match = re.search(r'第\s*[一二三四五]\s*部\s*分', text) or re.search(r'Part\s+(\d+)', text, re.I)
        
        if part_match:
            # Save previous part if exists
            if current_part:
                parts.append(current_part)
            
            current_part_num += 1
            # Extract part description (next few lines)
            part_desc = text
            next_elem = elem.find_next_sibling()
            if next_elem:
                part_desc += ' ' + next_elem.get_text(strip=True)
            
            current_part = {
                'part_number': current_part_num,
                'part_title': text,
                'description': part_desc,
                'questions': []
            }
            continue
        
        # Skip if no part started yet
        if not current_part:
            continue
        
        # Detect questions with numbers (like "16   A. 他的...")
        # Pattern: number followed by options
        question_pattern = r'^\s*(\d+)\s+'
        question_match = re.match(question_pattern, text)
        
        if question_match and len(text) > 5:
            q_num = int(question_match.group(1))
            q_text = text[question_match.end():]
            
            # Find associated image (look backwards)
            img = None
            prev = elem.find_previous('img')
            if prev:
                img_src = prev.get('src')
                # Only include if image is close (within ~3 elements)
                distance = 0
                check_elem = elem.find_previous_sibling()
                while check_elem and distance < 5:
                    if check_elem == prev.parent or check_elem == prev:
                        img = urljoin(base_url, img_src) if img_src else None
                        break
                    distance += 1
                    check_elem = check_elem.find_previous_sibling()
            
            # Extract options (A. xxx B. xxx C. xxx)
            options = []
            option_pattern = r'([A-F])[.\s]*([^A-F]+?)(?=[A-F][.\s]|$)'
            for match in re.finditer(option_pattern, q_text):
                option_letter = match.group(1)
                option_text = match.group(2).strip()
                if option_text:
                    options.append({
                        'option': option_letter,
                        'text': option_text
                    })
            
            # If no options found with letters, try TRUE/FALSE
            if not options and ('TRUE' in text or 'FALSE' in text):
                options = [
                    {'option': 'TRUE', 'text': 'TRUE'},
                    {'option': 'FALSE', 'text': 'FALSE'}
                ]
                q_text = f"Question {q_num}"
            
            question = {
                'question_number': q_num,
                'question_text': q_text if options else text,
                'image': img,
                'options': options,
                'correct_answer': None  # Will be filled if answer key is found
            }
            
            current_part['questions'].append(question)
    
    # Add last part
    if current_part:
        parts.append(current_part)
    
    return parts


def fetch(url: str, timeout=15):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.text


def main():
    p = argparse.ArgumentParser(description='Crawl HSK page for structured exam data')
    p.add_argument('--url', required=True, help='Page URL to crawl')
    p.add_argument('--output', default='output.json', help='Output JSON file')
    args = p.parse_args()

    try:
        html = fetch(args.url)
    except Exception as e:
        print(f'Error fetching {args.url}: {e}')
        return

    soup = BeautifulSoup(html, 'html.parser')

    # Get audio file
    audio_links = get_audio_links(soup, args.url)
    
    # Get structured questions by parts
    parts = extract_questions_structured(soup, args.url)
    
    # Count total questions
    total_questions = sum(len(part['questions']) for part in parts)
    
    result = {
        'exam_url': args.url,
        'exam_title': soup.find('h1').get_text(strip=True) if soup.find('h1') else 'HSK Listening Test',
        'audio_file': audio_links[0] if audio_links else None,
        'total_parts': len(parts),
        'total_questions': total_questions,
        'parts': parts
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f'✓ Done! Extracted {len(parts)} parts with {total_questions} questions.')
    print(f'✓ Audio file: {audio_links[0] if audio_links else "None"}')
    print(f'✓ Saved to {args.output}')


if __name__ == '__main__':
    main()
