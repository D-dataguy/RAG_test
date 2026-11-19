"""Explore the chat interaction with the RAG UI."""
from playwright.sync_api import sync_playwright
import time

URL = "https://rahulshettyacademy.com/rag-ui/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(3000)

    # Click the first example question
    print("=== Clicking first example button ===")
    first_example = page.query_selector_all("button")[2]  # First example button
    first_example.click()
    page.wait_for_timeout(5000)

    print("=== After clicking example ===")
    text = page.inner_text("body")
    print(text[:3000])

    # Now try typing a custom question
    print("\n=== Typing custom question ===")
    textarea = page.query_selector("textarea")
    if textarea:
        textarea.fill("What is RAG?")
        page.wait_for_timeout(1000)
        send_btn = page.query_selector("[aria-label='send_button']")
        if send_btn:
            send_btn.click()
        page.wait_for_timeout(5000)
        text2 = page.inner_text("body")
        print(text2[:3000])

    page.screenshot(path="C:\\Users\\HP\\Desktop\\RAG_testing\\chat_test.png", full_page=True)
    browser.close()