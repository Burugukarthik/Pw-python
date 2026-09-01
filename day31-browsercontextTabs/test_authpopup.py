import pytest
from playwright.sync_api import sync_playwright,expect,Playwright,Page
# https://admin:admin@the-internet.herokuapp.com/basic_auth
@pytest.mark.skip
def test_authpopup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("p:has-text('Congratulations! You must have the proper credentials.')")).to_be_visible()
    page.wait_for_timeout(8000)

def test_authpopup_credentials(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context(http_credentials={"username":"admin","password":"admin"})
    page=context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("p:has-text('Congratulations! You must have the proper credentials.')")).to_be_visible()
    page.wait_for_timeout(5000)
    """
Interviewer: Why do we pass http_credentials to browser.new_context() instead of page.goto()?

Answer:

HTTP Basic Authentication is handled at the browser session level. 
The browser must send the username and password with the initial HTTP request. 
That's why Playwright requires http_credentials 
to be configured when creating the BrowserContext, before any page is opened or navigation begins.
    """
