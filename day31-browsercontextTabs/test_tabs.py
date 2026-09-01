from idlelib import browser

import pytest
from playwright.sync_api import Page,Playwright,expect

def test_tabs(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    mainpage=context.new_page()

    mainpage.goto("https://testautomationpractice.blogspot.com/")

    # registering an event for handle tab
    mainpage.on("page",lambda page:page.wait_for_load_state())
    mainpage.locator("button:has-text('New Tab')").click()
    mainpage.wait_for_timeout(5000)

    all_pages=context.pages
    print(f"Main page: {all_pages[0].title()}")
    print(f"Opened Tab: {all_pages[1].title()}")

    childpage=all_pages[1]
    print(f"Child page: {childpage.url}")