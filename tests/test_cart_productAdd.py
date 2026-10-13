from playwright.sync_api import Page
from pages.cart_productAdd import CartProductAdd


class TestCartProductAdd:
    def test_cart_productAdd(self, page: Page):
        cart_productAdd = CartProductAdd(page)
        cart_productAdd.verify_homePage()
        cart_productAdd.hoverfirstProduct()
        cart_productAdd.clickaddCart()
        cart_productAdd.click_continue_shopping()
        cart_productAdd.hoversecondProduct()
        cart_productAdd.click_add_to_cart_secondProduct()
        cart_productAdd.click_viewcart()
        cart_productAdd.verifyboth_products_in_cart()
