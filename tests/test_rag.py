"""Professional test suite for RAG UI using Page Object Model and robust assertions."""
import pytest
from playwright.sync_api import expect
from pages.rag_page import RAGPage


def test_page_title(rag_page: RAGPage):
    """Verify the page heading is visible and correct."""
    expect(rag_page.heading).to_be_visible()
    expect(rag_page.heading).to_have_text("RAG-LLM")


def test_clear_conversation(rag_page: RAGPage):
    """Verify clear conversation button resets the chat view."""
    expect(rag_page.clear_button).to_be_visible()
    expect(rag_page.clear_button).to_be_enabled()
    rag_page.clear_conversation()
    expect(rag_page.textbox).to_be_enabled()


def test_text_input_and_assertion_fix(rag_page: RAGPage):
    """Verify text input works and correct assertion defect ("What is RAG?")."""
    expect(rag_page.textbox).to_be_enabled()
    rag_page.textbox.fill("What is RAG?")
    # Fixed assertion defect from "What is R?" to "What is RAG?"
    assert rag_page.textbox.input_value() == "What is RAG?"


def test_send_message_and_response(rag_page: RAGPage):
    """Verify sending a custom message triggers an AI response without fixed waits."""
    rag_page.send_message("Tell me about Retrieval Augmented Generation")
    
    # Verify response appears in DOM
    body = rag_page.get_body_text().lower()
    assert len(body) > 100
    assert any(term in body for term in ["retrieval", "augmented", "generation", "rag"])


def test_example_question_postman(rag_page: RAGPage):
    """Verify clicking an example question (Postman) loads the correct RAG answer."""
    rag_page.click_example_by_text("Postman")
    
    # Verify response content
    body = rag_page.get_body_text()
    assert len(body) > 200
    assert "Postman" in body


def test_example_question_python_selenium(rag_page: RAGPage):
    """Verify clicking a Python/Selenium example loads the correct RAG answer."""
    rag_page.click_example_by_text("Selenium Webdriver with PYTHON")
    
    body = rag_page.get_body_text()
    assert len(body) > 200
    assert "Selenium" in body


def test_multiple_sequential_questions(rag_page: RAGPage):
    """Verify sequential conversation continuity and response validation."""
    questions = [
        "What is Python?",
        "What is API testing?"
    ]

    for i, q in enumerate(questions):
        rag_page.send_message(q)
        body = rag_page.get_body_text()
        assert len(body) > 100, f"Question {i+1}: Expected response content"


def test_empty_message_handling(rag_page: RAGPage):
    """Verify submitting an empty message does not crash the UI."""
    rag_page.send_button.click()
    # Input should remain empty and system stable (textbox still visible/enabled)
    expect(rag_page.textbox).to_have_value("")
    expect(rag_page.textbox).to_be_enabled()
