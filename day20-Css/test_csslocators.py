import pytest,time
from playwright.sync_api import Page,expect

def test_verify_css_locator(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
     # now iam using tag id combination
    # to locate the web elemnet playwright provide one method caleed "Locator"
    # tag id ...tag#id

    # tag id
    # page.locator("input#small-searchterms").fill("Clothes")
    # page.locator("#small-searchterms").fill("Clothes")  #tag is optional in all this combinations not mandatory
    # page.wait_for_timeout(5000)


    #tag class
    #search-box-text ui-autocomplete-input 'there is space between (text ui) if there is space it wont work sometimes '
    # page.locator(".search-box-text").fill("Snitch Shop")
    # page.wait_for_timeout(5000)

    # tag attribute
    # page.locator("input[name=q]").fill("tshirts")
    # page.wait_for_timeout(2000)

    #tag class attribute
    page.locator(".search-box-text[value='Search store']").fill("Search store")
    page.wait_for_timeout(5000)
