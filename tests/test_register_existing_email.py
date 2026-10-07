from pages.register_existing_email import RegisterExistingEmail
import pytest 
class TestRegisterExistingEmail:
    def test_register_existing_email(self, page):
        register_existing_email = RegisterExistingEmail(page)
        register_existing_email.open_home_page()
        register_existing_email.click_signup_login()
        register_existing_email.enter_signup_credentials()