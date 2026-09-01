
from playwright.async_api import Page, expect, async_playwright
from pytest_playwright.pytest_playwright import browser
import pytest
@pytest.mark.asyncio
async def test_verifyPageUrl():

    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True)
        page = await browser.new_page()

        myurl=page.url
        print("Url of the Application:" ,myurl)

        expect(page).to_have_url("https://demowebshop.tricentis.com")
