import pytest

from playwright.sync_api import Playwright, expect


def test_browcontext(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page1=context.new_page()
    page2=context.new_page()

    page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page1.get_by_alt_text("company-branding")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("OrangeHRM")

    page2.goto("https://playwright.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")