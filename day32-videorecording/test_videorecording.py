# Import Path class to rename or move the recorded video file
from pathlib import Path

# Import Playwright classes for browser automation and assertions
from playwright.sync_api import Playwright, expect


# Test function executed by pytest
def test_record_video(playwright: Playwright):

    # Launch a Chromium browser in headed mode (browser UI will be visible)
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser context
    # A BrowserContext is an isolated browser session
    # Enable video recording and specify the folder and resolution
    context = browser.new_context(
        record_video_dir="videos",
        record_video_size={"width": 1024, "height": 768},
    )

    # Open a new page (tab) inside the browser context
    page = context.new_page()

    # Navigate to the Demoblaze website
    page.goto("https://www.demoblaze.com/")

    # Click the Login link to open the login popup
    page.locator("#login2").click()

    # Enter the username into the username textbox
    page.locator("#loginusername").fill("pavanol")

    # Enter the password into the password textbox
    page.locator("#loginpassword").fill("test@123")

    # Click the 'Log in' button
    page.locator("button:has-text('Log in')").click()

    # Pause for 6 seconds (used only for demo or debugging)
    # Avoid wait_for_timeout() in production automation
    page.wait_for_timeout(500)

    # Verify that the Logout button is visible after successful login
    expect(page.locator("#logout2")).to_be_visible()

    # Verify that the welcome message contains the logged-in username
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavanol")

    # Close the browser context
    # IMPORTANT:
    # The recorded video is saved to disk only after the context is closed
    context.close()

    # Get the path of the recorded video file
    video_path = page.video.path()

    # Rename the automatically generated video
    # (e.g., page@c7.webm -> test_login_success.webm)
    Path(video_path).rename("videos/test_login_success.webm")

    # Close the browser and release all browser resources
    browser.close()