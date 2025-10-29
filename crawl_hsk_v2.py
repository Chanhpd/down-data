#!/usr/bin/env python3
"""
crawl_hsk_v2.py

HSK exam scraper that parses text content directly.
Based on the actual structure found on mandarinbean.com

Usage:
    python crawl_hsk_v2.py --url "https://mandarinbean.com/h10901-listening/"

Outputs: output.json with structured format for API consumption
"""
import argparse
import json
import re
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def fetch_page(url: str):
    """Fetch page with proper headers"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    return r.text


def get_audio_file(soup: BeautifulSoup, base_url: str):
    """Extract audio file URL"""
    # Look in audio tags
    for audio in soup.find_all('audio'):
        src = audio.get('src')
        if src:
            return urljoin(base_url, src)
    
    # Look in source tags
    for source in soup.find_all('source'):
        src = source.get('src')
        if src and ('.mp3' in src.lower() or '.wav' in src.lower()):
            return urljoin(base_url, src)
    
    # Look in links
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '.mp3' in href.lower() or '.wav' in href.lower():
            return urljoin(base_url, href)
    
    return None


def get_all_images(soup: BeautifulSoup, base_url: str):
    """Get all images with their URLs"""
    images = {}
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            abs_url = urljoin(base_url, src)
            # Extract potential question number from filename
            match = re.search(r'H1_(\d+)\.(png|jpg|jpeg)', src, re.I)
            if match:
                q_num = int(match.group(1))
                images[q_num] = abs_url
            else:
                # Store by URL for later matching
                images[src] = abs_url
    return images


def parse_exam_structure(html: str, images_dict: dict, base_url: str):
    """
    Parse the exam structure from HTML text content.
    Based on actual format from mandarinbean.com
    """
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get full text content
    text = soup.get_text(separator='\n')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    parts = []
    current_part = None
    
    # Chinese number mapping
    cn_nums = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect part headers: "第 一 部 分" or "第一部分"
        part_match = re.search(r'第\s*([一二三四五])\s*部\s*分', line)
        if part_match:
            # Save previous part
            if current_part:
                parts.append(current_part)
            
            part_cn = part_match.group(1)
            part_num = cn_nums.get(part_cn, len(parts) + 1)
            
            # Get description from next lines
            description = line
            if i + 1 < len(lines) and '题' in lines[i + 1]:
                description += ' ' + lines[i + 1]
            
            current_part = {
                'part_number': part_num,
                'part_title': line,
                'description': description,
                'questions': []
            }
            i += 1
            continue
        
        # Skip if no current part
        if not current_part:
            i += 1
            continue
        
        # Detect questions - various formats:
        # Format 1: "1   TRUE  FALSE"
        # Format 2: "16   A. 他的( tā de)  B. 我的( wǒ de)  C. 同学的( tóngxué de)"
        # Format 3: "6   A  B  C"
        
        # Match: number at start, followed by options
        q_match = re.match(r'^(\d+)\s+(.+)', line)
        
        if q_match:
            q_num = int(q_match.group(1))
            content = q_match.group(2).strip()
            
            question = {
                'question_number': q_num,
                'question_text': '',
                'image': images_dict.get(q_num),
                'options': [],
                'correct_answer': None
            }
            
            # Parse TRUE/FALSE format
            if re.search(r'\bTRUE\b.*\bFALSE\b', content, re.I):
                question['question_text'] = f"Question {q_num}"
                question['options'] = [
                    {'option': 'TRUE', 'text': 'TRUE'},
                    {'option': 'FALSE', 'text': 'FALSE'}
                ]
            
            # Parse single letter format: "A  B  C"
            elif re.match(r'^[A-F]\s+[A-F]\s+[A-F]', content):
                question['question_text'] = f"Question {q_num}"
                # Extract letters
                letters = re.findall(r'\b([A-F])\b', content)
                for letter in letters:
                    question['options'].append({
                        'option': letter,
                        'text': letter
                    })
            
            # Parse detailed format: "A. text  B. text  C. text"
            elif re.search(r'[A-F][.\s]+', content):
                # Extract question text (before first option)
                q_text_match = re.match(r'^(.*?)(?=[A-F][.\s])', content)
                if q_text_match:
                    question['question_text'] = q_text_match.group(1).strip()
                
                if not question['question_text']:
                    question['question_text'] = f"Question {q_num}"
                
                # Extract options: "A. text"
                option_pattern = r'([A-F])[.\s]+([^A-F]+?)(?=\s+[A-F][.\s]|$)'
                for match in re.finditer(option_pattern, content):
                    opt_letter = match.group(1)
                    opt_text = match.group(2).strip()
                    if opt_text:
                        question['options'].append({
                            'option': opt_letter,
                            'text': opt_text
                        })
            
            # Only add if we found options
            if question['options']:
                current_part['questions'].append(question)
        
        i += 1
    
    # Add last part
    if current_part:
        parts.append(current_part)
    
    return parts


def main():
    parser = argparse.ArgumentParser(description='Crawl HSK exam page for structured data')
    parser.add_argument('--url', required=True, help='Page URL to crawl')
    parser.add_argument('--output', default='output.json', help='Output JSON file')
    args = parser.parse_args()

    print(f'⏳ Fetching page...')
    try:
        html = fetch_page(args.url)
    except Exception as e:
        print(f'❌ Error fetching page: {e}')
        return

    print(f'⏳ Parsing content...')
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get audio file
    audio_file = get_audio_file(soup, args.url)
    
    # Get images
    images = get_all_images(soup, args.url)
    
    # Parse structure
    parts = parse_exam_structure(html, images, args.url)
    
    # Get title
    title_tag = soup.find('h1')
    exam_title = title_tag.get_text(strip=True) if title_tag else 'HSK Listening Test'
    
    # Count questions
    total_questions = sum(len(part['questions']) for part in parts)
    
    # Build result
    result = {
        'exam_url': args.url,
        'exam_title': exam_title,
        'audio_file': audio_file,
        'total_parts': len(parts),
        'total_questions': total_questions,
        'parts': parts,
        'metadata': {
            'images_found': len(images),
            'crawler_version': '2.0'
        }
    }

    # Save to file
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f'\n✅ Done!')
    print(f'📊 Extracted: {len(parts)} parts, {total_questions} questions')
    print(f'🎵 Audio: {audio_file or "Not found"}')
    print(f'🖼️  Images: {len(images)}')
    for part in parts:
        print(f'   📝 Part {part["part_number"]}: {len(part["questions"])} questions')
    print(f'💾 Saved to: {args.output}')


if __name__ == '__main__':
    main()
