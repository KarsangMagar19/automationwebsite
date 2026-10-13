from playwright.sync_api import Page, expect


class VerifyProductQuantityCart:
    def __init__(self, page: Page):
        self.page = page
        self.goto_url = "https://www.automationexercise.com/"

    def verify_homePage(self):
        self.page.goto(self.goto_url)
        expect(self.page).to_have_url(self.goto_url)
        expect(self.page).to_have_title("Automation Exercise")

    def click_view_product(self):
        self.page.locator(".features_items .product-image-wrapper").first.get_by_role(
            "link", name="View Product"
        ).click()
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_url(
            "https://www.automationexercise.com/product_details/1"
        )

    def enter_quantity(self):
        self.page.locator("#quantity").clear()
        self.page.locator("#quantity").fill("4")
        self.page.wait_for_timeout(2000)

    def add_to_cart_button(self):
        self.page.get_by_role("button", name="Add to cart").click()
        self.page.wait_for_timeout(2000)

    def click_viewcart(self):
        self.page.get_by_role("link", name="View Cart").click()
        self.page.wait_for_timeout(1000)

    def verify_quantity(self):
        quantity = self.page.locator(
            "#cart_info tbody tr#product-1 .cart_quantity button"
        )
        expect(quantity).to_have_text("4")
        self.page.wait_for_timeout(2000)
