import pytest
from playwright.sync_api import sync_playwright

from utils.helpers import url


@pytest.fixture(scope="class")
def browser_instance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_page()
        context.goto(url)
        yield context
        context.close()