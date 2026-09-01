from re import search

import pytest
from playwright.sync_api import Page,expect

validatons=[("karthikdevopsit@gmail.com","Test@123","valid"),
            ("Akhil@gmail.com","Test@123","invalid"),
            ("test@gmail.com","45862","invalid"),
            ("","","invalid")
            ]
@pytest.mark.parametrize("gmail,password,validity",validatons)
def test_datadriven_test(gmail,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("input[name='Email']").fill(gmail)
    page.locator("input[name='Password']").fill(password)
    page.locator("input[value='Log in']").click()

    # validation
    # expect(page.locator(".ico-logout")).to_be_visible(timeout=5000)
    # print("Logged in")

    if validity == "valid":
        logout_link=page.locator(".ico-logout")
        expect(logout_link).to_be_visible(timeout=5000)
        print("This test passed...")

    else:
        error_msg=page.locator(".validation-summary-errors")
        expect(error_msg).to_be_visible(timeout=5000)
        print("This Invalid Credentials...")

      

