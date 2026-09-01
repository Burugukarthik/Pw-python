import csv

import pytest
from playwright.sync_api import Page,expect
login_data=[]

csvfile=open("testdata/data.csv",newline='',encoding="utf-8")
reader=csv.DictReader(csvfile)

for row in reader:
    login_data.append(
        (row["email"],row["password"],row["validity"]))
@pytest.mark.parametrize("email,password,validity", login_data)
def test_datadriven_test(email, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("input[name='Email']").fill(email)
    page.locator("input[name='Password']").fill(password)
    page.locator("input[value='Log in']").click()

    # validation
    # expect(page.locator(".ico-logout")).to_be_visible(timeout=5000)
    # print("Logged in")

    if validity == "valid":
        logout_link = page.locator(".ico-logout")
        expect(logout_link).to_be_visible(timeout=5000)
        print("This test passed...")

    else:
        error_msg = page.locator(".validation-summary-errors")
        expect(error_msg).to_be_visible(timeout=5000)
        print("This Invalid Credentials...")


"""
When the interviewer asks:

Why do we use append((...)) instead of append(...)?

You can answer:

"append() accepts only one argument. 
Since each test case consists of three related values (email, password, and validity),
 I group them into a single tuple and append that tuple to the list.
 PyTest then treats each tuple as one set of test data and automatically unpacks it during parameterized execution."



"""

