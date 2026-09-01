import pytest
from _pytest._code import source

from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_mousehover(page :Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    button=page.locator('.dropbtn')
    button.hover()

    child_btn=page.locator(".dropdown-content a:nth-child(1)")
    child_btn.hover()
    page.wait_for_timeout(5000)


# right click
@pytest.mark.skip
def test_rightclick(page :Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    button_click=page.locator(".context-menu-one")
    # button_click.click() if we dont perform any paramter it will perform left click
    button_click.click(button="right")     #click(button='right') this is will performs right click action
    page.wait_for_timeout(5000)
@pytest.mark.skip
def test_doubleclick(page :Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    double_click=page.locator("button[ondblclick='myFunction1()']")
    double_click.dblclick()   #this will perform doulbe click action
    field2=page.locator("#field2")
    expect(field2).to_have_value("Hello World!")
    page.wait_for_timeout(5000)


def test_mouse_draganddrop(page :Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    source=page.locator("div[id='draggable']")
    target=page.locator("#droppable")
    '''
    # Approach 1 . this is not prefferable because most of the times we use multiple methods
    # manual drag using hover method
    source.hover() #step 1
    page.mouse.down() #step 2
    target.hover()    #step3
    page.mouse.up()
    page.wait_for_timeout(5000)
    '''
    source.drag_to(target)
    page.wait_for_timeout(5000)