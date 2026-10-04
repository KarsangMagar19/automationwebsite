import pytest
import re
from playwright.sync_api import expect, sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.goto("https://www.automationexercise.com/")
    yield page
    page.close()