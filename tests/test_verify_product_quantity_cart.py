from pages.verify_product_quantity_cart import VerifyProductQuantityCart


class TestVerifyProductQuantityCart:
    def test_verify_product_quantity_cart(self, page):
        verifyProductQuantityCart = VerifyProductQuantityCart(page)
        verifyProductQuantityCart.verify_homePage()
        verifyProductQuantityCart.click_view_product()
        verifyProductQuantityCart.enter_quantity()
        verifyProductQuantityCart.add_to_cart_button()
        verifyProductQuantityCart.click_viewcart()
        verifyProductQuantityCart.verify_quantity()
