import random
import string

from pages.register_before_checkout import RegisterBeforeCheckout


class TestRegisterBeforeCheckout:
    def test_register_before_checkout(self, page):
        random_email = (
            "".join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com"
        )

        register_before_checkout = RegisterBeforeCheckout(page)

        register_before_checkout.verify_homePage()
        register_before_checkout.fill_signup_form("karsang Doe", random_email)
        register_before_checkout.fill_account_information()
        register_before_checkout.add_to_cart()
        register_before_checkout.click_proceed_to_checkout()
