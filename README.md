# RAG UI Testing

## Project Structure
- `test_basic.py` - Basic Playwright pytest tests for RAG UI functionality
- `conftest.py` - Pytest fixtures (browser, page, rag_page)
- `requirements.txt` - Python dependencies
- `explore.py` - Initial page exploration script
- `explore_chat.py` - Chat interaction exploration
- `explore_deep.py` - Deep structure exploration
- `fetch_js.py` - JS bundle analysis
- `screenshot.png` - Screenshot from exploration
- `deep_explore.png` - Deep exploration screenshot
- `chat_test.png` - Chat test screenshot
- `screenshot.png` - General screenshot

## Testing Approach

This project tests the RAG (Retrieval-Augmented Generation) UI at https://rahulshettyacademy.com/rag-ui/ using **Playwright + pytest**.

### Page Overview
The page is a ChatGPT-like interface built with React (Vite) that:
- Uses OpenAI API (`https://api.openai.com/v1/chat/completions`)
- Proxies through `https://rahulshettyacademy.com/rag-llm`
- Has a `CHATGPT_SECRET_KEY` environment variable
- Contains example questions about online courses (Postman, Selenium, Java)

### Tests Included
1. `test_page_title` - Verifies the "RAG-LLM" heading is visible
2. `test_clear_button` - Verifies the "Clear conversation" button exists and is enabled
3. `test_example_buttons` - Verifies at least 3 example buttons exist (Postman, Selenium, Java)
4. `test_text_input` - Verifies the textbox exists, is enabled, and can receive input
5. `test_send_button` - Verifies the send button exists and is enabled
6. `test_send_message` - Verifies sending a message clears the input and generates a response

### Running Tests
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
python -m pytest -v

# Run with HTML report
python -m pytest --html=report.html -v
```

### Key Testing Patterns Used
- **`get_by_role()`** - For robust selectors (headings, textboxes, buttons)
- **`locator(:has-text())`** - For text-based button/element location
- **`wait_for_timeout()`** - For React rendering delays (consider replacing with proper wait conditions for production)
- **Session-scoped browser** - Shared browser instance for efficiency

### Notes
- The page dynamically loads content via JavaScript, so tests include appropriate waits
- The RAG system queries a course database and returns AI-generated answers
- All tests use headless=True by default (set headless=False in conftest for debugging)