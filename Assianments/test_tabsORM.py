import pytest

from playwright.sync_api import Page,Playwright,expect

def test_tabs(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    mainpage=context.new_page()

    mainpage.on("page",lambda page: page.wait_for_load_state())

    mainpage.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    mainpage.locator("a:has-text('OrangeHRM, Inc')").click()
    mainpage.wait_for_timeout(5000)

    alltabs=context.pages
    print(f"Total tabs: {len(alltabs)}")
    print(f"Main Tab: {alltabs[0].title()}")
    print(f"opened Tab: {alltabs[1].title()}")

    if "OrangeHRM: All in One HR Software for Businesses | OrangeHRM" in alltabs:
        print("All tabs opened",alltabs.url)