from playwright.sync_api import expect
from pages.loginwith_invalid_credentials import LoginWithInvalidCredentials
class TestLoginWithInvalidCredentials:
    def test_login_with_invalid_credentials(self, page):
        login_with_invalid_credentials = LoginWithInvalidCredentials(page)
        login_with_invalid_credentials.open_home_page()
        login_with_invalid_credentials.click_login_link()
        login_with_invalid_credentials.fill_login_form()
        login_with_invalid_credentials.close_browser()