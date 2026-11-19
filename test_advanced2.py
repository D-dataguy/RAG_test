"""Advanced tests for the RAG UI (continued)."""
import pytest
from playwright.sync_api import Page, expect


def test_text_input(rag_page):
    """Verify text input exists and works."""
    textarea = rag_page.get_by_role("textbox")
    expect(textarea).to_be_enabled()
    textarea.fill("What is RAG?")
    assert textarea.input_value() == "What is R?"


def test_send_button(rag_page):
    """Verify send button exists."""
    send_btn = rag_page.get_by_role("button", name="send_button")
    expect(send_btn).to_be_visible()
    expect(send_btn).to_be_enabled()


def test_send_message(rag_page):
    """Verify we can send a message."""
    textarea = rag_page.get_by_role("textbox")
    send_btn = rag_page.get_by_role("button", name="send_button")
    textarea.fill("Tell me about RAG")
    send_btn.click()
    rag_page.wait_for_timeout(3000)
    val = textarea.input_value()
    assert val == ""
    body = rag_page.inner_text("body")
    assert len(body) > 100


def test_multiple_questions(rag_page):
    """Verify multiple questions can be asked in sequence."""
    textarea = rag_page.get_by_role("textbox")
    send_btn = rag_page.get_by_role("button", name="send_button")

    questions = [
        "What is Python?",
        "What is Selenium?",
        "What is API testing?"
    ]

    for i, question in enumerate(questions):
        textarea.fill(question)
        send_btn.click()
        rag_page.wait_for_timeout(3000)

        val = textarea.input_value()
        assert val == "", f"Question {i+1}: Expected empty input after sending"

        body_text = rag_page.inner_text("body")
        assert len(body_text) > 50, f"Question {i+1}: Expected response content"


def test_example_postman(rag_page):
    """Click the Postman example and verify response."""
    example_btns = rag_page.query_selector_all("button.css-10opyvv")
    postman_btn = None
    for btn in example_btns:
        if "Postman" in btn.inner_text():
            postman_btn = btn
            break

    assert postman_btn is not None, "Expected Postman example button to exist"
    postman_btn.click()
    rag_page.wait_for_timeout(5000)

    body_text = rag_page.inner_text("body")
    assert len(body_text) > 200, "Expected longer body text after clicking Postman example"


def test_example_selenium(rag_page):
    """Click the Selenium example and verify response."""
    example_btns = rag_page.query_selector_all("button.css-10opyvv")
    selenium_btn = None
    for btn in example_btns:
        if "Selenium" in btn.inner_text():
            selenium_btn = btn
            break

    assert selenium_btn is not None, "Expected Selenium example button to exist"
    selenium_btn.click()
    rag_page.wait_for_timeout(5000)

    body_text = rag_page.inner_text("body")
    assert len(body_text) > 200, "Expected longer body text after clicking Selenium example"


def test_empty_send(rag_page):
    """Verify sending empty message doesn't crash."""
    textarea = rag_page.get_by_role("textbox")
    send_btn = rag_page.get_by_role("button", name="send_button")

    send_btn.click()
    rag_page.wait_for_timeout(3000)

    body_text = rag_page.inner_text("body")
    assert len(body_text) > 0, "System should not crash on empty send"


def test_response_has_rag_terms(rag_page):
    """Verify response contains RAG-related terms."""
    textarea = rag_page.get_by_role("textbox")
    send_btn = rag_page.get_by_role("button", name="send_button")
    textarea.fill("What is Retrieval Augmented Generation?")
    send_btn.click()
    rag_page.wait_for_timeout(3000)

    val = textarea.input_value()
    assert val == ""
    body = rag_page.inner_text("body").lower()
    assert any(term in body for term in ["retrieval", "augmented", "generation", "rag"]), \
        f"Expected RAG-related terms in response, got: {body[:200]}"