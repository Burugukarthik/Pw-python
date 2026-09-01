from itertools import product

import pytest
from playwright.sync_api import Page,expect
def test_comparsionmethods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    products=page.locator(".product-title")
    count=products.count()
    product_locator = products.all()
    for product in product_locator:
        print(product.inner_text())
    # p=products.all_text_contents()
    # p = products.all_inner_texts()
    # print(p)

    #1. Difference b/w inner_text() and text_content()

    # print(products.nth(1).inner_text())    #if we use inner text we will get exact value no sapces nothing
    # print(products.nth(1).text_content())  #returns content with special chars and spaces we use strip it can elima space
    # PASSED [100%]14.1-inch Laptop
    #
    #             14.1-inch Laptop
'''
    for i in range(count):
        # product_name=products.nth(i).inner_text()
        product_name=products.nth(1).text_content()
        print(product_name.strip()) 
'''
#3 all() list of locators [] index concept
