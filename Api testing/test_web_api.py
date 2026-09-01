from utils.apibase import APIUtils
from playwright.sync_api import Playwright,expect


def test_e2e_web_api(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page=context.new_page()

    # Create order -> orderId
    api_utils=APIUtils()  #creating object for APIUtils class
    orderid=api_utils.createOrder(playwright)


    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("karthikdevopsit@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Test@123")
    page.get_by_role("button",name="login").click()
    page.get_by_role("button",name="ORDERS").click()


     # go to orders page -> confirm order is present or not

    row_item=page.locator("tr").filter(has_text=orderid)
    row_item.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()