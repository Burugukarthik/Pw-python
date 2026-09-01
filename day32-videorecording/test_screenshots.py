from datetime import datetime

import pytest

from playwright.sync_api import Playwright

def test_screenshots(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # it will take only "paritial page" screenshot
    # page.screenshot(path=f"screenshots/hoomepage_{timestamp}.png")

    # now if we want to take full page screenshot
    # page.screenshot(path=f"screenshots/{timestamp}.png",full_page=True)
    # browser.close()
    # logo=page.locator("img[alt='company-branding']")
    # logo.screenshot(path=f"screenshots/logo_{timestamp}.png")
    featureproduct=page.locator(".orangehrm-login-slot")
    featureproduct.screenshot(path=f"screenshots/featurefpro{timestamp}.png" )
    browser.close()