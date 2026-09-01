import pytest
from playwright.sync_api import Page, Expect, expect


def test_xpath_locator(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #1.absoulte xpath (//full xpath) we never prefer this
    # /html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[3]/div/div[1]/a/img
    logo=page.locator("//html/body/div[4]/div[1]/div[4]/div[3]/div/div/div[3]/div[3]/div/div[1]/a/img")
    expect(logo).to_be_visible(timeout=5000)
    # 2.relative xpath : //tagname[@attribute='value']
    img=page.locator("//img[@alt='Picture of $25 Virtual Gift Card']")
    expect(img).to_be_visible(timeout=5000)
    #3.xpath with contains() we will use this most of the time to handle dynamic elements
    products=page.locator("//h2//a[contains(@href,'computer')]")
    product_counts=products.count()
    print("Products count:", product_counts)
    expect(products).to_have_count(product_counts)
    print("first computer products:", products.first.text_content())
    print("last computer products:", products.last.text_content())
    print("N-th computer products:", products.nth(2).text_content())