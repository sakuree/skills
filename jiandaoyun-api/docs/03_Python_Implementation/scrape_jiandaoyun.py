import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import json
import os
import re
import time
from urllib.parse import urljoin, urlparse

BASE_URL = "https://hc.jiandaoyun.com/open/"
START_URL = "https://hc.jiandaoyun.com/open/10992"
OUTPUT_DIR = ".trae/skills/jiandaoyun-api"

# Ensure output directories exist
os.makedirs(os.path.join(OUTPUT_DIR, "docs"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "examples"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "schemas"), exist_ok=True)

visited = set()
pages_data = []

THEMES = {
    "auth": ["身份认证", "鉴权", "Token", "登录"],
    "form": ["表单", "数据", "记录", "字段"],
    "data": ["数据管理", "导入", "导出"],
    "webhook": ["Webhook", "回调", "推送"],
    "frontend": ["前端", "组件", "UI", "插件"],
    "error": ["错误", "异常", "状态码"]
}

def normalize_text(text):
    return text.strip() if text else ""

def get_theme(title, content):
    title_lower = title.lower()
    for theme, keywords in THEMES.items():
        for keyword in keywords:
            if keyword.lower() in title_lower:
                return theme
    return "other"

def extract_api_info(soup, title, url):
    # Heuristic to find API definitions
    # Look for HTTP methods and URLs in code blocks or headers
    api_info = []
    
    # Try to find method and url
    # Pattern: GET /v1/app/{app_id}/entry/{entry_id}/data
    # Or in tables
    
    # Simplified extraction for demo: look for code blocks starting with curl
    code_blocks = soup.find_all("code")
    for block in code_blocks:
        text = block.get_text()
        if text.strip().startswith("curl"):
            # Extract basic info
            method = "GET"
            if "-X POST" in text: method = "POST"
            elif "-X PUT" in text: method = "PUT"
            elif "-X DELETE" in text: method = "DELETE"
            
            # Extract URL from curl
            url_match = re.search(r'https?://[^\s"\']+', text)
            api_url = url_match.group(0) if url_match else ""
            
            if api_url:
                api_info.append({
                    "name": title,
                    "method": method,
                    "url": api_url,
                    "example": text
                })
    return api_info

def scrape_page(url):
    if url in visited:
        return
    visited.add(url)
    
    print(f"Scraping {url}...")
    try:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract title
        title_tag = soup.find('h1')
        title = title_tag.get_text().strip() if title_tag else "Untitled"
        
        # Extract content
        article = soup.find('article') or soup.find(class_='article-content') or soup.find(class_='markdown-body')
        if not article:
            print(f"No content found for {url}")
            return

        # Convert to markdown
        markdown_content = md(str(article), heading_style="atx")
        
        # Extract API info
        apis = extract_api_info(soup, title, url)
        
        # Determine theme
        theme = get_theme(title, markdown_content)
        
        page_data = {
            "title": title,
            "url": url,
            "content": markdown_content,
            "apis": apis,
            "theme": theme,
            "last_updated": time.strftime("%Y-%m-%d") # Mock, real timestamp requires parsing specific meta
        }
        pages_data.append(page_data)
        
        # Save markdown
        safe_title = re.sub(r'[\\/*?:"<>|]', "", title).replace(" ", "_")
        filename = f"{theme}_{safe_title}.md"
        with open(os.path.join(OUTPUT_DIR, "docs", filename), "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\nURL: {url}\n\n{markdown_content}")
            
        # Save schemas/examples if APIs found
        for i, api in enumerate(apis):
            # Schema
            schema = {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "const": api['url']},
                    "method": {"type": "string", "const": api['method']}
                },
                "description": f"API definition for {title}"
            }
            schema_name = f"{safe_title}_api_{i}.json"
            with open(os.path.join(OUTPUT_DIR, "schemas", schema_name), "w", encoding="utf-8") as f:
                json.dump(schema, f, indent=2, ensure_ascii=False)
            
            # Example
            example_name = f"{safe_title}_example_{i}.sh"
            with open(os.path.join(OUTPUT_DIR, "examples", example_name), "w", encoding="utf-8") as f:
                f.write(api['example'])

        # Find child links
        # Heuristic: look for links in sidebar or content that share the same base path
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            full_url = urljoin(url, href)
            if full_url.startswith(BASE_URL) and full_url not in visited:
                 # Limit recursion depth/scope if needed, but here we just follow open/*
                 # Avoid infinite loops or going out of scope
                 if "open/" in full_url:
                     scrape_page(full_url)
                     
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Start scraping
scrape_page(START_URL)

# Generate Manifest
manifest = {
    "name": "jiandaoyun-api",
    "version": "1.0.0",
    "description": "Jiandaoyun API Knowledge Base",
    "author": "Trae Assistant",
    "index": [p['title'] for p in pages_data],
    "themes": {k: [] for k in THEMES.keys()}
}
manifest["themes"]["other"] = []

for p in pages_data:
    manifest["themes"][p['theme']].append(p['title'])

with open(os.path.join(OUTPUT_DIR, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"Scraping complete. Processed {len(pages_data)} pages.")
