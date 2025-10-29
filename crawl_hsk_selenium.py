#!/usr/bin/env python3
"""
crawl_hsk_selenium.py

Advanced scraper using Selenium to extract structured HSK exam data with parts, questions, images, and answers.
This version renders JavaScript to get the complete page content.

Usage:
    python crawl_hsk_selenium.py --url "https://mandarinbean.com/h10901-listening/"

Outputs: output.json with structured format for API consumption
"""
import argparse
import json
import re
import time
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def get_rendered_html(url: str):
    """Use Selenium to get fully rendered HTML"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        # Wait for content to load
        time.sleep(3)
        
        # Wait for specific elements to ensure page is loaded
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "form"))
            )
        except:
            pass
        
        html = driver.page_source
        return html
    finally:
        driver.quit()


def extract_structured_data(soup: BeautifulSoup, base_url: str):
    """
    Extract questions organized by parts with proper structure for API
    """
    # Find the main content area
    content = soup.find('div', class_='entry-content') or soup.find('article') or soup.body
    
    # Get audio file
    audio_file = None
    for audio_tag in soup.find_all('audio'):
        src = audio_tag.get('src')
        if src:
            audio_file = urljoin(base_url, src)
            break
    if not audio_file:
        for source in soup.find_all('source'):
            src = source.get('src')
            if src and any(ext in src.lower() for ext in ['.mp3', '.wav', '.m4a']):
                audio_file = urljoin(base_url, src)
                break
    if not audio_file:
        for a in soup.find_all('a', href=True):
            if any(ext in a['href'].lower() for ext in ['.mp3', '.wav', '.m4a']):
                audio_file = urljoin(base_url, a['href'])
                break
    
    parts = []
    current_part = None
    
    # Get all text content
    all_text = content.get_text(separator='\n') if content else soup.get_text(separator='\n')
    lines = [l.strip() for l in all_text.split('\n') if l.strip()]
    
    # Find images in content
    images = {}
    if content:
        for img in content.find_all('img'):
            src = img.get('src')
            if src and 'H1_' in src:  # Question images typically have H1_ in name
                # Extract question number from image name if possible
                match = re.search(r'H1_(\d+)', src)
                if match:
                    q_num = int(match.group(1))
                    images[q_num] = urljoin(base_url, src)
    
    # Parse the content line by line
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect part headers
        part_match = re.search(r'第\s*([一二三四五])\s*部\s*分', line)
        if part_match:
            if current_part:
                parts.append(current_part)
            
            part_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5}
            part_num = part_map.get(part_match.group(1), len(parts) + 1)
            
            # Get part description (next line usually has question range)
            desc = line
            if i + 1 < len(lines):
                desc += ' ' + lines[i + 1]
            
            current_part = {
                'part_number': part_num,
                'part_title': line,
                'description': desc,
                'questions': []
            }
            i += 1
            continue
        
        # Detect questions (format: "16   A. 他的( tā de)  B. 我的...")
        question_match = re.match(r'^(\d+)\s+(.+)', line)
        if question_match and current_part:
            q_num = int(question_match.group(1))
            q_content = question_match.group(2)
            
            # Parse options
            options = []
            
            # Check for TRUE/FALSE format
            if 'TRUE' in q_content and 'FALSE' in q_content:
                options = [
                    {'option': 'TRUE', 'text': 'TRUE'},
                    {'option': 'FALSE', 'text': 'FALSE'}
                ]
                q_text = f"Question {q_num}"
            else:
                # Parse A/B/C/D/E/F options
                # Pattern: A. text  B. text  C. text
                option_pattern = r'([A-F])[.\s]+([^A-F]+?)(?=\s+[A-F][.\s]|$)'
                for match in re.finditer(option_pattern, q_content):
                    opt_letter = match.group(1)
                    opt_text = match.group(2).strip()
                    if opt_text:
                        options.append({
                            'option': opt_letter,
                            'text': opt_text
                        })
                
                # Extract question text (text before first option)
                q_text_match = re.match(r'^(.+?)(?=[A-F][.\s])', q_content)
                q_text = q_text_match.group(1).strip() if q_text_match else q_content
            
            # Get associated image
            img_url = images.get(q_num)
            
            question = {
                'question_number': q_num,
                'question_text': q_text,
                'image': img_url,
                'options': options,
                'correct_answer': None
            }
            
            current_part['questions'].append(question)
        
        i += 1
    
    # Add last part
    if current_part:
        parts.append(current_part)
    
    return parts, audio_file


def main():
    p = argparse.ArgumentParser(description='Crawl HSK page for structured exam data using Selenium')
    p.add_argument('--url', required=True, help='Page URL to crawl')
    p.add_argument('--output', default='output.json', help='Output JSON file')
    args = p.parse_args()

    print(f'⏳ Fetching and rendering page...')
    try:
        html = get_rendered_html(args.url)
    except Exception as e:
        print(f'❌ Error fetching {args.url}: {e}')
        print('\nNote: Make sure you have Chrome/Chromium installed and chromedriver available.')
        print('Install chromedriver: https://chromedriver.chromium.org/')
        return

    print(f'⏳ Parsing HTML...')
    soup = BeautifulSoup(html, 'html.parser')

    # Get structured questions by parts
    parts, audio_file = extract_structured_data(soup, args.url)
    
    # Count total questions
    total_questions = sum(len(part['questions']) for part in parts)
    
    # Get exam title
    title_tag = soup.find('h1')
    exam_title = title_tag.get_text(strip=True) if title_tag else 'HSK Listening Test'
    
    result = {
        'exam_url': args.url,
        'exam_title': exam_title,
        'audio_file': audio_file,
        'total_parts': len(parts),
        'total_questions': total_questions,
        'parts': parts
    }

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f'\n✅ Done! Extracted {len(parts)} parts with {total_questions} questions.')
    print(f'🎵 Audio file: {audio_file or "Not found"}')
    for part in parts:
        print(f'   Part {part["part_number"]}: {len(part["questions"])} questions')
    print(f'💾 Saved to {args.output}')


if __name__ == '__main__':
    main()
