from playwright.sync_api import Page, expect

class WaitUtils:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, locator):
        expect(locator).to_be_visible(timeout=5000)

    def wait_for_text(self, locator, text):
        expect(locator).to_have_text(text, timeout=5000)

    def wait_until_value(self, locator, value):
        expect(locator).to_have_value(value, timeout=5000)
