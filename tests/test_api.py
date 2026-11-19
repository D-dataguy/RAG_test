"""API testing module for RAG endpoint inspection and validation."""
import pytest
from playwright.sync_api import APIRequestContext, expect


def test_rag_api_endpoint(playwright):
    """Intercept or directly query the RAG backend API endpoint to validate response structure."""
    # Create request context
    api_request_context: APIRequestContext = playwright.request.new_context(
        base_url="https://rahulshettyacademy.com"
    )
    
    # Check that the main application page or asset endpoints are reachable
    response = api_request_context.get("/rag-ui/")
    assert response.ok, f"Expected 200 OK from RAG UI, got {response.status}"
    
    # Verify content type
    content_type = response.headers.get("content-type", "")
    assert "text/html" in content_type or "application/javascript" in content_type
    
    api_request_context.dispose()
