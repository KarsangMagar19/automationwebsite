from playwright.sync_api import expect

productname = "Blue Top"
Category = "Women > Tops"
Price = "Rs. 500"
Availability = "In Stock"
condition = "New"
brand = "Polo"


class VerifyAllProducts:
    def __init__(self, page):
        self.page = page
        self.product_heading = page.locator(".title")
        self.product_name = page.locator(".productinfo")

    def open_product_page(self):
        self.page.goto("https://www.automationexercise.com/products")

    def verify_product_page_heading(self):
        expect(self.product_heading).to_have_text("All Products")

    def verify_productslist_visibility(self):
        count = self.product_name.count()
        assert count > 0, "No products found"
        for i in range(count):
            expect(self.product_name.nth(i)).to_be_visible()

    def click_product(self):
        first_product = self.page.locator("a[href='/product_details/1']")
        expect(first_product).to_be_visible()
        first_product.click()

        expect(self.page).to_have_url(
            "https://www.automationexercise.com/product_details/1"
        )
        self.page.wait_for_timeout(3000)


    def verify_product_details(self):
        product_info = self.page.locator(".product-information")

        expect(product_info.locator("h2")).to_have_text(productname)

        expect(product_info.locator("p").filter(has_text="Category:")).to_have_text(
            f"Category: {Category}"
        )

        # Price is displayed as "Rs. 500", not "Price: Rs. 500"
        expect(product_info.get_by_text(Price, exact=True)).to_be_visible()

        expect(product_info.locator("p").filter(has_text="Availability:")).to_contain_text(
            Availability
        )

        expect(product_info.locator("p").filter(has_text="Condition:")).to_contain_text(
            condition
        )

        expect(product_info.locator("p").filter(has_text="Brand:")).to_contain_text(brand)
