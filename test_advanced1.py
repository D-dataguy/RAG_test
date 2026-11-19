"""Advanced tests for the RAG UI."""
import pytest
from playwright.sync_api import Page, expect


def test_page_title(rag_page):
    """Verify the page title."""
    rag_heading = rag_page.get_by_role("heading", name="RAG-LLM")
    expect(rag_heading).to_be_visible()


def test_clear_button(rag_page):
    """Verify clear conversation button."""
    clear_btn = rag_page.locator("button:has-text('Clear conversation')")
    expect(clear_btn).to_be_visible()
    expect(clear_btn).to_be_enabled()
    clear_btn.click()
    rag_page.wait_for_timeout(1000)
    textarea = rag_page.get_by_role("textbox")
    expect(textarea).to_be_enabled()


def test_example_buttons(rag_page):
    """Verify example question buttons exist."""
    example_btns = rag_page.query_selector_all("button.css-10opyvv")
    assert len(example_btns) >= 3
    btn_texts = [btn.inner_text() for btn in example_btns]
    assert any("Postman" in t for t in btn_texts)
    assert any("Selenium" in t for t in btn_texts)
    assert any("Java" in t for t in btn_texts)