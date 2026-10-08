from pages.testcase_page import TestCasePage


class TestTestCasePage:
    def test_testcase_page(self, page):
        testcase_page = TestCasePage(page)
        testcase_page.open_test_case_page()
        testcase_page.click_testcase()
        testcase_page.verify_testcase_page()
