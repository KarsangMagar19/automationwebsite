from pages.register_user import RegisterUser
import random
import string
class TestRegisterUser:
    def test_register_user(self, page):
        random_email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com"
        register_user = RegisterUser(page)
        register_user.open_home_page()
        register_user.click_login_link()
        register_user.fill_signup_form("John Doe", random_email)
        assert page.url == "https://www.automationexercise.com/signup"
        if page.url == "https://www.automationexercise.com/signup":
            print("Test passed")
        else:
            print("Test failed")
            raise Exception("Test failed")
        register_user.enter_account_details()
        
        register_user.close_browser()





    