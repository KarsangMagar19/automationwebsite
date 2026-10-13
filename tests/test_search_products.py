from playwright.sync_api import Page
from pages.search_products import SearchProducts


class TestSearchProducts:
    def test_search_products(self, page: Page):
        search_products = SearchProducts(page)
        search_products.verify_homePage()
        search_products.Click_Products()
        search_products.enter_Productname()
        search_products.verify_search_products()
        search_products.allrelated_searchProducts()
        search_products.verify_allrelated_searchProducts()
