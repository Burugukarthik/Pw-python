import pytest

from playwright.sync_api import Playwright,Page,expect

def test_login(page:Page):
    page.goto("http://onetrace-frontend-static.s3-website-ap-southeast-2.amazonaws.com/")
    page.get_by_role("button",name="Login").click()
    page.get_by_placeholder("Email Address").fill("pasupuletinaveenkumar22@gmail.com")
    page.get_by_placeholder("Password").fill("Test@123")
    page.locator("input[type='checkbox']").check()
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button",name="Create New Entry").click()
    page.get_by_role("button",name="Component Repair").click()

    page.locator("xpath=//label[contains(text(),'Serial Number')]/following-sibling::input").fill("0302")

    page.locator("//label[contains(text(),'Purchase Order Number')]/following-sibling::input").fill('2704')
    page.locator("//label[contains(text(),'Description')]/following-sibling::input").fill('new')
    page.get_by_role("textbox", name="Add Your Comments Here").fill("no")
    page.get_by_text("Select Enterprise").click()
    page.get_by_text("Ontrace SignOff2").click()
    page.get_by_role("button", name="Submit").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_text("0302")).to_be_visible()









