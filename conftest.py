"""Pytest configuration and fixtures for RAG UI testing."""
import pytest
from playwright.sync_api import sync_playwright, Page, BrowserContext

BASE_URL = "https://rahulshettyacademy.com/rag-ui/"


@pytest.fixture(scope="session")
def playwright_browser():
    """Create a shared browser instance for the test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(playwright_browser) -> Page:
    """Create a fresh page for each test."""
    context = playwright_browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def rag_page(page: Page) -> Page:
    """Navigate to the RAG UI page and wait for it to load."""
    page.goto(BASE_URL, wait_until="networkidle")
    page.wait_for_timeout(2000)  # Wait for React to render
    return page