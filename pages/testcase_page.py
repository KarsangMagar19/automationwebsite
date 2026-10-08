from playwright.sync_api import expect
from playwright._impl import _page


class TestCasePage:
    def __init__(self, page: _page):
        self.page = page

    def open_test_case_page(self):
        self.page.goto("https://www.automationexercise.com/")

    def click_testcase(self):
        self.page.click("//a[@href='/test_cases']")

    def verify_testcase_page(self):
        expect(self.page).to_have_url("https://www.automationexercise.com/test_cases")
