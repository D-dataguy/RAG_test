"""Quick exploration script to understand the RAG UI page."""
from playwright.sync_api import sync_playwright
import time

URL = "https://rahulshettyacademy.com/rag-ui/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(3000)  # Wait for React to render

    print("=== PAGE TITLE ===")
    print(page.title())

    print("\n=== PAGE HTML (first 3000 chars) ===")
    html = page.content()
    print(html[:3000])

    print("\n=== ALL VISIBLE TEXT ===")
    text = page.inner_text("body")
    print(text[:2000])

    print("\n=== INTERACTIVE ELEMENTS ===")
    # Find all buttons, inputs, textareas, links
    for selector in ["button", "input", "textarea", "a"]:
        elements = page.query_selector_all(selector)
        for el in elements:
            try:
                tag = el.evaluate("el => el.tagName")
                text = el.inner_text() or el.get_attribute("value") or ""
                placeholder = el.get_attribute("placeholder") or ""
                aria_label = el.get_attribute("aria-label") or ""
                print(f"  {tag}: text='{text[:80]}' placeholder='{placeholder}' aria-label='{aria_label}'")
            except:
                pass

    # Screenshot
    page.screenshot(path="C:\\Users\\HP\\Desktop\\RAG_testing\\screenshot.png", full_page=True)
    print("\nScreenshot saved to screenshot.png")

    browser.close()