"""Deep exploration of the RAG UI - understand structure and API calls."""
from playwright.sync_api import sync_playwright
import json

URL = "https://rahulshettyacademy.com/rag-ui/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Capture network requests
    network_requests = []
    page.on("request", lambda req: network_requests.append({
        "url": req.url,
        "method": req.method,
        "post_data": req.post_data
    }))

    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(3000)

    print("=== ALL BUTTONS ===")
    buttons = page.query_selector_all("button")
    for i, btn in enumerate(buttons):
        text = btn.inner_text()
        aria = btn.get_attribute("aria-label")
        class_name = btn.get_attribute("class")
        print(f"  Button {i}: text='{text[:60]}' aria='{aria}' class='{class_name[:60]}'")

    print("\n=== ALL INPUTS/TEXTAREA ===")
    inputs = page.query_selector_all("input, textarea")
    for i, inp in enumerate(inputs):
        tag = inp.evaluate("el => el.tagName")
        placeholder = inp.get_attribute("placeholder")
        aria = inp.get_attribute("aria-label")
        class_name = inp.get_attribute("class")
        print(f"  {tag} {i}: placeholder='{placeholder}' aria='{aria}' class='{class_name[:60]}'")

    print("\n=== ALL LINKS ===")
    links = page.query_selector_all("a")
    for i, link in enumerate(links):
        href = link.get_attribute("href")
        text = link.inner_text()
        print(f"  Link {i}: href='{href}' text='{text[:60]}'")

    # Try clicking the first example button more carefully
    print("\n=== Trying to click first example ===")
    # The examples are buttons with course names
    example_buttons = page.query_selector_all("button")
    # Find buttons that contain course-related text
    for btn in example_buttons:
        text = btn.inner_text()
        if "Postman" in text or "Selenium" in text or "Java" in text:
            print(f"Found example button: {text[:80]}")
            btn.click()
            page.wait_for_timeout(5000)
            break

    print("\n=== After click - page text ===")
    text = page.inner_text("body")
    print(text[:2000])

    print("\n=== NETWORK REQUESTS ===")
    for req in network_requests:
        if "api" in req["url"].lower() or "chat" in req["url"].lower() or "rag" in req["url"].lower():
            print(f"  {req['method']} {req['url']}")
            if req["post_data"]:
                print(f"    POST data: {req['post_data'][:200]}")

    page.screenshot(path="C:\\Users\\HP\\Desktop\\RAG_testing\\deep_explore.png", full_page=True)
    browser.close()