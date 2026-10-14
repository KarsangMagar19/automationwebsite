from playwright.sync_api import Page, expect

username = "karsang Doe"


class RegisterBeforeCheckout:
    def __init__(self, page: Page):
        self.page = page
        self.goto_url = "https://www.automationexercise.com/"

    def verify_homePage(self):
        self.page.goto(self.goto_url)
        expect(self.page).to_have_url(self.goto_url)
        expect(self.page).to_have_title("Automation Exercise")

    def fill_signup_form(self, name, email):
        self.page.get_by_role("link", name="Signup / Login").click()

        self.page.locator('[data-qa="signup-name"]').fill(name)
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.locator('[data-qa="signup-button"]').click()

        expect(self.page).to_have_url("https://www.automationexercise.com/signup")

    def fill_account_information(self):
        self.page.locator('[for="id_gender1"]').check()
        self.page.locator('[data-qa="password"]').fill("password")

        self.page.locator('[data-qa="days"]').select_option("27")
        self.page.locator('[data-qa="months"]').select_option("7")
        self.page.locator('[data-qa="years"]').select_option("1990")

        self.page.get_by_role("checkbox", name="newsletter").check()
        self.page.locator("#optin").check()

        self.page.locator('[data-qa="first_name"]').fill("karsang")
        self.page.locator('[data-qa="last_name"]').fill("Doe")
        self.page.locator('[data-qa="company"]').fill("Company")
        self.page.locator("#address1").fill("123 Main St")
        self.page.locator("#address2").fill("123 Main St")

        self.page.locator('[data-qa="country"]').select_option(label="United States")
        self.page.locator('[data-qa="state"]').fill("California")
        self.page.locator('[data-qa="city"]').fill("Los Angeles")
        self.page.locator('[data-qa="zipcode"]').fill("12345")
        self.page.locator('[data-qa="mobile_number"]').fill("1234567890")

        self.page.get_by_role("button", name="Create Account").click()

        expect(self.page).to_have_url(
            "https://www.automationexercise.com/account_created"
        )
        expect(self.page.get_by_text("Account Created!", exact=True)).to_be_visible()

        self.page.get_by_role("link", name="Continue").click()

        expect(
            self.page.get_by_text(f"Logged in as {username}", exact=False)
        ).to_be_visible()

    def add_to_cart(self):
        first_product = self.page.locator(
            ".features_items .product-image-wrapper"
        ).first

        first_product.get_by_role("link", name="View Product").click()

        expect(self.page).to_have_url(
            "https://www.automationexercise.com/product_details/1"
        )

        self.page.locator("#quantity").fill("4")
        self.page.get_by_role("button", name="Add to cart").click()

        # Open the cart from the add-to-cart modal.
        view_cart = self.page.get_by_role("link", name="View Cart")
        expect(view_cart).to_be_visible()
        view_cart.click()

        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")

    def click_proceed_to_checkout(self):
        # Verify that the cart page is open.
        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")

        # Proceed to checkout only once.
        checkout_link = self.page.locator("a.check_out:visible")
        expect(checkout_link).to_be_visible()
        checkout_link.click()

        # Verify checkout navigation.
        expect(self.page).to_have_url("https://www.automationexercise.com/checkout")

        # Verify address and order sections.
        expect(self.page.get_by_role("heading", name="Address Details")).to_be_visible()

        expect(
            self.page.get_by_role("heading", name="Review Your Order")
        ).to_be_visible()

        # Verify the order total.
        expect(self.page.get_by_text("Rs. 2000", exact=True).last).to_be_visible()

        # Verify that Place Order is available.
        expect(self.page.get_by_role("link", name="Place Order")).to_be_visible()

    def click_cart(self):
        cart_link = self.page.get_by_role("link", name="Cart", exact=True)

        expect(cart_link).to_be_visible()
        cart_link.click()

        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")

    def checkout(self):
        # Use this method only when you are currently on the cart page.
        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")

        checkout_link = self.page.locator("a.check_out:visible")
        expect(checkout_link).to_be_visible(timeout=10000)
        checkout_link.click()

        expect(self.page).to_have_url("https://www.automationexercise.com/checkout")

        expect(self.page.get_by_role("heading", name="Address Details")).to_be_visible()

    def placeOrder(self):
        # Click Place Order from the checkout page.
        expect(self.page).to_have_url("https://www.automationexercise.com/checkout")

        self.page.get_by_role("link", name="Place Order").click()

        expect(self.page).to_have_url("https://www.automationexercise.com/payment")

        # Fill payment information.
        self.page.locator('[name="name_on_card"]').fill("karsang")
        self.page.locator('[name="card_number"]').fill("1234567890123456")
        self.page.locator('[name="cvc"]').fill("123")
        self.page.locator('[name="expiry_month"]').fill("12")
        self.page.locator('[name="expiry_year"]').fill("2030")

        # Submit payment.
        self.page.locator('[data-qa="pay-button"]').click()

        # Verify successful order placement.
        expect(self.page).to_have_url(
            "https://www.automationexercise.com/payment_done/2000"
        )

        expect(self.page.get_by_role("heading", name="Order Placed!")).to_be_visible()

        expect(
            self.page.get_by_text("Congratulations! Your order has been confirmed!")
        ).to_be_visible()

        # Delete the test account.
        self.page.get_by_role("link", name="Delete Account").click()

        expect(self.page.get_by_text("Account Deleted!", exact=False)).to_be_visible()
        self.page.wait_for_timeout(5000)

        self.page.get_by_role("link", name="Continue").click()
