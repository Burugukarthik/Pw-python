import pytest
from playwright.sync_api import Page,expect

from loginpage import LoginPage
from homepage import Homepage
from cartpage import CartPage
@pytest.mark.parametrize("username,password,product_name",
                         [("pavanol","test@123","Nokia lumia 1520")])
def test_user_can_login_and_add_products_to_cart(page:Page,username,password,product_name):
    page.goto("https://www.demoblaze.com/index.html")

    #LoginPage
    # create one object
    login_page=LoginPage(page)
    login_page.click_login_link()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
# homepage
    homepage=Homepage(page)
    homepage.add_product_to_cart(product_name)
    page.wait_for_timeout(3000)
    homepage.click_cart_link()

    # cartpage
    cartpage=CartPage(page)
    product_in_cart=cartpage.check_product_in_cart(product_name)
    page.wait_for_timeout(3000)
    expect(product_in_cart).to_be_visible()