from playwright.sync_api import Page,expect

def test_verifyOrangeHrm(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name="Login").click()
    page.wait_for_timeout(5000)  # Wait 5 seconds
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    test=page.get_by_role("heading",name="Dashboard")
    expect(test).to_be_visible(timeout=3000)
    print("Verified")