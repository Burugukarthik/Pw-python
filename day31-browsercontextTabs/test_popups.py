import pytest

from playwright.sync_api import Playwright, expect


def test_popup(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")


    page.on("popup",lambda popup:popup.wait_for_load_state())
    page.locator("#PopUp").click()
    page.wait_for_timeout(2000)

    all_popups=context.pages
    print(f"No of popups: {len(all_popups)}")


# now three pages/windows are opened now i want to close one window
# now i want to do activity in specific popup ...playwright popup window
#I want to iterate all the popups whenever i get a playwright pop up  then i want to do some activity
    for popup in all_popups:
        print(f"Popup: {popup.url}")
    # i want to get the title because i want to know the information about the popup window otherwise we cannot switch
        title=popup.title()
        # now compare if the title is
        if "Playwright" in title:
            # page.locator("getStarted_Sjon") Here we cannot use the page because we have three pages
            popup.locator("getStarted_Sjon")
            popup.wait_for_timeout(5000)
            expect(popup).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
            # After validating this all I want to close this window
            popup.close() #it will close the playwright window

    print("Pop up Validations done successfully")