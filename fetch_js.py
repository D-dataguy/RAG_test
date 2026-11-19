"""Fetch and analyze the JS bundle for API endpoints."""
from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/rag-ui/assets/index-4c232a95.js")
    js = page.content()

    # Save JS to file
    with open("bundle.js", "w", encoding="utf-8") as f:
        f.write(js)

    # Find all URLs
    urls = set(re.findall(r'https?://[^\s"\'`]+', js))
    for u in sorted(urls):
        print(u)

    # Find fetch/axios calls
    fetch_calls = re.findall(r'(fetch|axios|axios\.\w+)\s*\([^)]+\)', js)
    print("\n=== FETCH CALLS ===")
    for call in fetch_calls[:20]:
        print(call[:200])

    # Look for API paths
    api_paths = re.findall(r'["\'](/[^"\' ]*(?:api|chat|rag|completion|generate)[^"\' ]*)["\']', js, re.IGNORECASE)
    print("\n=== API PATHS ===")
    for path in set(api_paths):
        print(path)

    # Look for environment variables or config
    env_vars = re.findall(r'(?:VITE_|REACT_APP_|NEXT_PUBLIC_|process\.env\.)(\w+)', js)
    print("\n=== ENV VARS ===")
    for v in set(env_vars):
        print(v)

    browser.close()