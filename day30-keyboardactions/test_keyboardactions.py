import pytest

from playwright.sync_api import Playwright,Page,expect

def test_keyboard_actions(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    input1=page.locator("#input1")

    # Step 1: focus on input1  "Before typing with the keyboard, the element must have focus."
    input1.focus()   #cursor will wait in the inputbox to get value
    # now we will pass sometext inside inputbox1 through keyboard
    # step 2: provide text in Inpu1
    page.keyboard.insert_text("using this without fill method")
    # step3 : ctrl+A
    page.keyboard.press("Control+A")
    # step4: ctrl+C
    page.keyboard.press("Control+C")
    # step5: press Tab key 2 times to navigate or focus on input2
    page.keyboard.press("Tab") #we to press two times so we need to write again
    page.keyboard.press("Tab")

    # step6: ctrl+v
    page.keyboard.press("Control+V") #it will paste in inputbox2
    page.keyboard.press("Tab")  # we to press two times so we need to write again
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")


    input2=page.locator("#input2")
    input3=page.locator("#input3")
    expect(input2).to_have_value("using this without fill method")
    expect(input3).to_have_value("using this without fill method")

    '''
    When do we use keyboard actions?

Use keyboard actions when the application requires real user interactions, such as:

Keyboard shortcuts (Ctrl+C, Ctrl+V, Ctrl+A)
Pressing Enter to submit a form
Navigating using Tab
Closing popups with Escape
Working with rich text editors
Applications that depend on keyboard events instead of simple value assignment
    
    
Why would you use keyboard actions instead of fill()?

A good answer is:

"I use keyboard actions when the application depends on actual keyboard events,such as pressing 
 Enter to submit a form, navigating with Tab, selecting from auto-suggestions using arrow keys,testing keyboard shortcuts,
 or validating accessibility. For simple text entry, I generally prefer fill() because it's simpler and faster."
    '''