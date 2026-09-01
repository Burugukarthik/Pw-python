from playwright.sync_api import Page,expect


# getByAltText()

"""
def test_verify_pwlocators(page:Page):
    page.goto( 'http://automationexercise.com')

    # it will capture one element stores in a Variable "Logo"
    logo=page.get_by_alt_text("demo website for practice").nth(2)
#     To perform Asseration we have "expect" method
#     expect(logo).to_be_visible() this will verify that particular element is present or not
    expect(logo).to_be_visible(timeout=30000)



    if we run headless it will get fail
    so we have to run in headed mode

"""
from playwright.sync_api import Page, expect
import time

def test_login(page: Page):
    page.goto("https://automationexercise.com/#google_vignette")

    # logo = page.get_by_alt_text("demo website for practice").nth(2)


    # expect(logo).to_be_visible(timeout=30000)
    # page.get_by_text()
    # expect(page.get_by_text("Category").first).to_be_visible(timeout=30000)

    # page.goto("https://automationexercise.com/products#google_vignette")
    # expect(page.get_by_role(role="heading",name="Login to your account")).to_be_visible(timeout=30000)

# page.get_by_label()
#     page.goto('https://automationexercise.com/products#google_vignette')
#     search_box=page.get_by_placeholder("Search Product")
#     expect(search_box).to_be_visible(timeout=30000)
#     search_box.fill("Snitch Shirts")
# #page.get_by_title()
#
"""
Q: An element takes 40 seconds to appear. What would you do?

A good answer is:

"Since Playwright's default action timeout is 30 seconds, 
I would increase the timeout for that specific action or assertion, for example:
"""