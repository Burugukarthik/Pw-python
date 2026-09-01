import pytest
from playwright.sync_api import Playwright, expect


def test_popup(playwright: Playwright):
    # Launch Chromium browser in headed mode
    browser = playwright.chromium.launch(headless=False)

    # Create a new Browser Context (similar to an Incognito window)
    context = browser.new_context()

    # Open the main page inside the context
    page = context.new_page()

    # Navigate to the application
    page.goto("https://testautomationpractice.blogspot.com/")


    # Register a popup event.
    # Whenever a new popup/tab opens, wait until it is completely loaded.
    page.on("popup", lambda popup: popup.wait_for_load_state())


    # Click the button that opens multiple popup windows/tabs
    page.locator("#PopUp").click()

    # Wait for 2 seconds so all popups are opened
    page.wait_for_timeout(2000)



    # context.pages returns a list of all open pages
    # (Main page + all popup windows)
    all_popups = context.pages

    print(f"Number of Open Pages: {len(all_popups)}")


    # Iterate through every opened page
    for popup in all_popups:

        # Print the URL of the current page
        print(f"Current Page URL: {popup.url}")

        # Get the title of the current page
        title = popup.title()

        print(f"Title: {title}")

        # Check whether this is the Playwright website
        if "Playwright" in title:

            print("Playwright window found...")

            # Perform actions only on the Playwright popup
            # Example:
            # popup.locator("text=Get started").click()

            # Validate the page title
            expect(popup).to_have_title(
                "Fast and reliable end-to-end testing for modern web apps | Playwright"
            )

            print("Title validation successful.")

            # Close only the Playwright popup window
            popup.close()

            print("Playwright popup closed.")


    print("Popup validations completed successfully.")

    # Close the browser
    browser.close()