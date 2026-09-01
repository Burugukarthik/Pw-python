
"""
playwright is provided two packages
sync_api
async_api

"""
# import Page class so that we can access fixture ,that fixture is part of the class

from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page


def test_verifyPageUrl(page:Page):
    page.goto("https://demowebshop.tricentis.com") #passing url
    #checking whteher the url is same or not
    myurl=page.url
    print("url of the application:",myurl)

    expect(page).to_have_url("https://demowebshop.tricentis.com") #expected url

"""
mode of execution
.....headless - No UI
..... headed it will open brower 
"""
def test_verifyTitle(page:Page):
    page.goto("http://www.automationpractice.pl/index.php")
    mytitle=page.title()
    print("Title of the page:" , mytitle)
    expect(page).to_have_title("My Shop")



