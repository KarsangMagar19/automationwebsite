
from pages.login_correct_email_password import LoginCorrectEmailPassword

class TestLoginWithValidCredentials:
    def test_login_with_valid_credentials(self, page):
        login_correct_email_password = LoginCorrectEmailPassword(page)
        login_correct_email_password.open_home_page()
        login_correct_email_password.click_login_link()
        login_correct_email_password.fill_login_form()
        login_correct_email_password.close_browser()