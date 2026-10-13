from playwright.sync_api import Page
from pages.verify_all_products import VerifyAllProducts


class TestVerifyAllProducts:
    def test_verify_all_products(self, page: Page):
        verify_all_products = VerifyAllProducts(page)
        verify_all_products.open_product_page()
        verify_all_products.verify_product_page_heading()
        verify_all_products.verify_productslist_visibility()
        verify_all_products.click_product()
        verify_all_products.verify_product_details()
