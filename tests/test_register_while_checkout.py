import random
import string

from pages.register_while_checkout import RegisterWhileCheckout


def test_register_while_checkout(page):
    random_email = "".join(random.choices(string.ascii_lowercase, k=10)) + "@gmail.com"

    register_while_checkout = RegisterWhileCheckout(page)

    register_while_checkout.verify_homePage()
    register_while_checkout.add_to_cart()
    register_while_checkout.click_proceed_to_checkout()

    register_while_checkout.fill_signup_form("karsang Doe", random_email)

    register_while_checkout.fill_account_information()
    register_while_checkout.click_cart()

    # Return to the cart after account creation
    register_while_checkout.checkout()
    register_while_checkout.placeOrder()
