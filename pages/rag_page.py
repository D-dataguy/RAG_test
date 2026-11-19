"""Page Object Model for the RAG UI at https://rahulshettyacademy.com/rag-ui/."""
from playwright.sync_api import Page, expect

class RAGPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://rahulshettyacademy.com/rag-ui/"
        
        # Robust locators (avoiding brittle CSS classes)
        self.heading = page.get_by_role("heading", name="RAG-LLM")
        self.textbox = page.get_by_role("textbox")
        self.send_button = page.get_by_role("button", name="send_button")
        self.clear_button = page.locator("button:has-text('Clear conversation')")
        self.light_mode_button = page.locator("button:has-text('Light mode')")

    def navigate(self):
        """Navigate to the RAG UI page."""
        self.page.goto(self.url, wait_until="domcontentloaded")
        expect(self.heading).to_be_visible()

    def send_message(self, message: str):
        """Type a message and click send."""
        expect(self.textbox).to_be_enabled()
        self.textbox.fill(message)
        assert self.textbox.input_value() == message
        self.send_button.click()
        # Wait a moment for submission to process
        self.page.wait_for_timeout(2000)

    def clear_conversation(self):
        """Click the clear conversation button."""
        self.clear_button.click()
        self.page.wait_for_timeout(1000)

    def click_example_by_text(self, text_snippet: str):
        """Click an example question button containing the given text snippet."""
        example_btn = self.page.locator(f"button:has-text('{text_snippet}')").first
        expect(example_btn).to_be_visible()
        example_btn.click()
        self.page.wait_for_timeout(3000)

    def get_body_text(self) -> str:
        """Get the inner text of the entire body for validation."""
        return self.page.inner_text("body")
