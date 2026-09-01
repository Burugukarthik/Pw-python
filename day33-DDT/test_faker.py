import pytest
from faker import Faker
from playwright.sync_api import Page, expect

fake = Faker()

def generate_invalid_users(n=20):
    """Randomly generated users — these don't exist, so they should always fail login."""
    return [(fake.email(), fake.password(), "invalid") for _ in range(n)]

# Keep your known-good real accounts separate from generated junk data
known_credentials = [
    ("karthikdevopsit@gmail.com", "Test@123", "valid"),
    ("Akhil@gmail.com", "Test@123", "invalid"),
    ("test@gmail.com", "45862", "invalid"),
    ("", "", "invalid"),
]

all_credentials = known_credentials + generate_invalid_users(20)

@pytest.mark.parametrize("gmail,password,validity", all_credentials)
def test_datadriven_test(gmail, password, validity, page: Page):
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator("input[name='Email']").fill(gmail)
    page.locator("input[name='Password']").fill(password)
    page.locator("input[value='Log in']").click()

    if validity == "valid":
        logout_link = page.locator(".ico-logout")
        expect(logout_link).to_be_visible(timeout=5000)
        print("This test passed...")
    else:
        error_msg = page.locator(".validation-summary-errors")
        expect(error_msg).to_be_visible(timeout=5000)
        print("This Invalid Credentials...")