"""Enhanced Pytest configuration with logging, settings, and auto-screenshots on failure."""
import os
import pytest
from playwright.sync_api import sync_playwright, Page
from pages.rag_page import RAGPage
from config.settings import BASE_URL, HEADLESS, TIMEOUT
from utils.logger import get_logger

logger = get_logger("conftest")


@pytest.fixture(scope="session")
def browser_instance():
    """Create a shared browser instance."""
    logger.info("Launching browser session...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()
    logger.info("Browser session closed.")


@pytest.fixture
def page(browser_instance, request) -> Page:
    """Create a fresh browser context and page, with automatic failure screenshot capture."""
    context = browser_instance.new_context()
    context.set_default_timeout(TIMEOUT)
    page = context.new_page()
    
    logger.info(f"Starting test: {request.node.name}")
    yield page
    
    # Check if test failed
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        screenshot_path = os.path.abspath(f"screenshots/{request.node.name}.png")
        page.screenshot(path=screenshot_path, full_page=True)
        logger.error(f"Test failed! Screenshot saved to {screenshot_path}")
    
    logger.info(f"Finished test: {request.node.name}")
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
