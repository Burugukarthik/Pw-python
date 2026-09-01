 # sorted list and unsorted list
    # during interview they will ask
# let see how we can check the dropdown elements or options are in sorted order or not
import pytest
from playwright.sync_api import Page,expect

def test_sorteddropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # dropdown_options=page.locator("#colors>option")
    '''
    options_text=[text.strip()for text in dropdown_options.all_text_contents()]
    # copying the actually list
    original_list=options_text.copy()
    sorted_list=sorted(options_text)

    print("original_list:",original_list)
    print("sorted_list:",sorted_list)
    '''
    dropdown_sortedlist=page.locator("#animals>option")
    actual_list=[text.strip()for text in dropdown_sortedlist.all_text_contents()]
    original_list=actual_list.copy()
    sorted_list=sorted(actual_list)         #sorted logic
    print("Original list",original_list)
    print("Sorted list",sorted_list)

    if original_list==sorted_list:
        print("Test passed")
    else:
        print("Test failed")
