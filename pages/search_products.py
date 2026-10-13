from playwright.sync_api import Page, expect

productname = "winter top"
name = "top"


class SearchProducts:
    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")

    def verify_homePage(self):
        self.page.goto("https://www.automationexercise.com/")
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_url("https://www.automationexercise.com/")
        expect(self.page).to_have_title("Automation Exercise")

    def Click_Products(self):
        self.page.locator("a[href='/products']").click()
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_title("Automation Exercise - All Products")

    def enter_Productname(self):
        self.search_box.fill(productname)
        self.page.wait_for_timeout(1000)
        self.search_button.click()

    def verify_search_products(self):
        expect(self.page.locator(".title")).to_be_visible()
        expect(self.page.locator(".title")).to_contain_text("SEARCHED PRODUCTS", ignore_case=True)
        expect(self.page.locator(".features_items .productinfo p").first).to_be_visible()
        expect(self.page.locator(".features_items .productinfo p").first).to_contain_text(
            productname, ignore_case=True
        )

    def allrelated_searchProducts(self):
        self.search_box.fill(name)
        self.page.wait_for_timeout(1000)
        self.search_button.click()

    def verify_allrelated_searchProducts(self):
        expect(self.page.locator(".title")).to_be_visible()
        expect(self.page.locator(".title")).to_contain_text("SEARCHED PRODUCTS", ignore_case=True)
        products = self.page.locator(".features_items .productinfo")
        count = products.count()
        assert count > 0, "No related products found"
        for i in range(count):
            expect(products.nth(i)).to_be_visible()
