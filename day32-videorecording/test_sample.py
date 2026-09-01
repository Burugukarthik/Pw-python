import pytest

from playwright.sync_api import Page,expect

def test_url(page: Page):
    page.goto("https://www.flipkart.com/")
    expect(page).to_have_url("https://www.flipkart.com/")

def test_logo(page: Page):
    page.goto("https://www.flipkart.com/")
    page.locator("div._1psv1zeb9._1psv1ze0._1psv1ze9x._1psv1ze7o._1psv1ze2u._1psv1ze53._7dzyg2w._1psv1ze29._1psv1ze53."
                 "_1psv1zee3._1o6mltlgo._1o6mltlbr._1o6mltl1x._1o6mltl6u._1o6mltljo:visible")
    expect(page).to_be_visible()


