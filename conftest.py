"""Pytest configuration using pytest-playwright's built-in fixtures."""
import os
import pytest
from playwright.sync_api import Page, expect
from pages.rag_page import RAGPage
from config.settings import BASE_URL, HEADLESS, TIMEOUT
from utils.logger import get_logger

logger = get_logger("conftest")


@pytest.fixture(scope="session")
def browser(playwright):
    """Create a shared browser instance using pytest-playwright."""
    logger.info("Launching browser session...")
    browser = playwright.chromium.launch(headless=HEADLESS)
    yield browser
    browser.close()
    logger.info("Browser session closed.")


@pytest.fixture
def page(browser) -> Page:
    """Create a fresh page for each test."""
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(TIMEOUT)
    yield page
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test execution results for failure detection."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture
def rag_page(page: Page) -> RAGPage:
    """Initialize and navigate the RAGPage Object."""
    rag = RAGPage(page)
    rag.url = BASE_URL
    rag.navigate()
    return rag