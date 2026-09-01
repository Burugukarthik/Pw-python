import pytest

from playwright.sync_api import Page, expect


def test_practicebootstrap(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(5000)

    page.get_by_text('PIM').click()

    page.locator("form i").nth(0).click()
    options = page.locator("div[role='listbox'] span")
    expect(options.first).to_be_visible()
    no_of_count = options.count()
    print("Total number of count: ", no_of_count)

    print("All the select options", options.all_text_contents())

    # printinh all the options usin loops
    for i in range(no_of_count):
        options.nth(i).text_content()

    # Selecting the option using a loop
    for i in range(no_of_count):
        # 1. Use text_content() and strip spaces for safe matching
        text = options.nth(i).text_content().strip()

        if text == "Full-Time Contract":
            print("Full Time Contract")
            options.nth(i).click()
            break  # 2. KEY FIX: Stops the loop so it won't try to look for nth(2)!

    page.wait_for_timeout(5000)






