"""Data-driven test suite loading test cases from JSON test data."""
import json
import os
import pytest
from playwright.sync_api import expect
from pages.rag_page import RAGPage
from utils.logger import get_logger

logger = get_logger("test_rag_datadriven")


def load_test_data():
    """Load queries from JSON file using path relative to this file."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "test_data", "questions.json")
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)["rag_queries"]


@pytest.mark.parametrize("query_data", load_test_data())
def test_data_driven_rag_queries(rag_page: RAGPage, query_data):
    """Data-driven test executing questions from questions.json and verifying relevance."""
    question = query_data["question"]
    keyword = query_data["expected_keyword"].lower()
    
    logger.info(f"Executing query: '{question}' expecting keyword: '{keyword}'")
    
    rag_page.send_message(question)
    
    body = rag_page.get_body_text().lower()
    assert len(body) > 100, "Response body too short"
    assert keyword in body, f"Expected keyword '{keyword}' in response body, got: {body[:300]}"
    
    logger.info(f"Successfully validated query: '{question}'")