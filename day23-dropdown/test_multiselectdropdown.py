import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_multiselectdropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # select multiple options from the dropdown -3 ways
    page.locator("#colors").select_option(["Red","Blue","Green"])






