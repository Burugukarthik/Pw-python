import pytest
from faker import Faker
from playwright.sync_api import Playwright, Page, expect


fake = Faker()


def test_login(page: Page):

    serial_number = f"SN-{(fake.random_number(digits=6, fix_len=True))}"
    po_number = f"PO-{(fake.random_number(digits=4, fix_len=True))}"


    print(f"Generated Serial Number: {serial_number}")
    print(f"Generated Purchase Order Number: {po_number}")


    page.goto("http://onetrace-frontend-static.s3-website-ap-southeast-2.amazonaws.com/")
    page.get_by_role("button", name="Login").click()
    page.get_by_placeholder("Email Address").fill("pasupuletinaveenkumar22@gmail.com")
    page.get_by_placeholder("Password").fill("Test@123")
    page.locator("input[type='checkbox']").check()
    page.get_by_role("button", name="Login").click()


    page.get_by_role("button", name="Create New Entry").click()
    page.get_by_role("button", name="Component Repair").click()


    page.locator("//label[contains(text(),'Serial Number')]/following-sibling::input").fill(serial_number)
    page.locator("//label[contains(text(),'Purchase Order Number')]/following-sibling::input").fill(po_number)
    page.locator("//label[contains(text(),'Description')]/following-sibling::input").fill("new")
    page.get_by_role("textbox", name="Add Your Comments Here").fill("no comments")

    page.get_by_text("Select Enterprise").click()
    page.get_by_text("Ontrace SignOff2").click()
    page.get_by_role("button", name="Submit").click()


    expect(page.get_by_text("Entry created successfully!").first).to_be_visible()
    page.wait_for_timeout(5000)
    expect(page.get_by_text(serial_number)).to_be_visible()

    page.get_by_role("button",name="Menu").click()
    page.get_by_text("Material/Core Received").click()
    page.locator(
        "(//div[@class='absolute inset-y-0 right-0 flex items-center pr-2 sm:pr-3 cursor-pointer'])[1]").click()
    page.locator("#receivedDate").fill("21/08/2026",force=True)
    page.locator("#expectedStartDate").fill("21/08/2026",force=True)


    page.get_by_role("button",name="Yes").click()
    page.get_by_role("button",name="Repair").click()
    page.get_by_placeholder("Comments").fill("Flow")
    page.get_by_role("button",name="Submit").click()