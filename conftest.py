"""Pytest configuration and fixtures for professional RAG UI testing."""
import pytest
from playwright.sync_api import sync_playwright, Page
from pages.rag_page import RAGPage

BASE_URL = "https://rahulshettyacademy.com/rag-ui/"


@pytest.fixture(scope="session")
def browser_instance():
    """Create a shared browser instance for the test session."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser_instance) -> Page:
    """Create a fresh browser context and page for each test."""
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def rag_page(page: Page) -> RAGPage:
    """Initialize and return the RAGPage Page Object."""
    rag = RAGPage(page)
    rag.navigate()
    return rag
