from playwright.sync_api import Page, expect


class CartProductAdd:
    def __init__(self, page: Page):
        self.page = page
        self.goto_url = "https://www.automationexercise.com/"

    def verify_homePage(self):
        self.page.goto(self.goto_url)
        expect(self.page).to_have_url(self.goto_url)
        expect(self.page).to_have_title("Automation Exercise")

    def hoverfirstProduct(self):
        self.page.locator(".product-image-wrapper").first.hover()
        self.page.wait_for_timeout(1000)

    def clickaddCart(self):
        self.page.locator(".btn.btn-default.add-to-cart").first.click()
        self.page.wait_for_timeout(1000)

    def click_continue_shopping(self):
        self.page.get_by_role("button", name="Continue Shopping").click()
        self.page.wait_for_timeout(1000)

    def hoversecondProduct(self):
        self.page.locator(".product-image-wrapper").nth(1).hover()
        self.page.wait_for_timeout(1000)

    def click_add_to_cart_secondProduct(self):
        second_product = self.page.locator(
            ".features_items .product-image-wrapper"
        ).nth(1)
        add_to_cart = second_product.locator("a.add-to-cart").first
        add_to_cart.click()
        self.page.wait_for_timeout(1000)

    def click_viewcart(self):
        self.page.get_by_role("link", name="View Cart").click()
        self.page.wait_for_timeout(3000)

    def verifyboth_products_in_cart(self):
        products = self.page.locator("tr[id^='product-']")
        expect(products).to_have_count(2)
        expect(products.nth(0)).to_contain_text("Blue Top")
        expect(products.nth(1)).to_contain_text("Men Tshirt")

    def verify_price_quantity_total(self):
        products = self.page.locator("tr[id^='product-']")
        expect(products.locator("td.cart_price")).to_have_count(2)
        expect(products.locator("td.cart_quantity")).to_have_count(2)
        expect(products.locator("td.cart_total")).to_have_count(2)
        self.page.wait_for_timeout(1000)
