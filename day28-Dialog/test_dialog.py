import pytest

from playwright.sync_api import Page,expect
# in python, we can create one function in another function so this is called nested function
@pytest.mark.skip
def test_simple_dialog(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # registering an event   APPROACH 1

    def handle_dialog(dialog):
        print(dialog.message)
        dialog.accept()

    # page.on is for rising the event inside this we have pass two parameters one paramter should br "dialog"
    page.on("dialog",handle_dialog)  #registerd the event
    page.wait_for_timeout(3000)
    page.locator("#alertBtn").click()

    page.wait_for_timeout(5000)
    """
    1.Your website has an alert.
    2.When you click:  an alert appears:
    3.Now ask yourself:
      Who will click the OK button?
      Not you.
      You want Playwright to click it automatically
    4.Step 2: How does Playwright know an alert appeared?
    Playwright has events.
    One of them is: ""dialog" 
    Step 3: Tell Playwright what to do
            Now think in plain English:
            When a dialog appears, accept it.
            Convert that sentence into code.
            When dialog appears
                   ↓
              accept it  dialog.accept()
              def handle_dialog(dialog):
                  dialog.accept()......>Python allows writing it in one line
             lambda dialog: dialog.accept()
    
    Instead, always ask yourself:
What event am I waiting for? (dialog)
What action do I want to perform? (accept)
How do I connect the event to the action? (page.on(event, callback))
 """

@pytest.mark.skip
def test_simple_dialog1(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.on("dialog", lambda dialog: dialog.accept())#dialog.accept() automatically clicks the OK button.
    page.wait_for_timeout(3000)
    page.locator("#alertBtn").click()
    page.locator("#confirmBtn").click()

    page.wait_for_timeout(3000)
@pytest.mark.skip
def test_confirm(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: dialog.dismiss())
    page.wait_for_timeout(5000)
    page.locator("#confirmBtn").click()

    page.wait_for_timeout(3000)
    text=page.locator("#demo").inner_text()
    print(f"text :" , text)

    # expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")
    page.wait_for_timeout(3000)

def test_prompt(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("dialog", lambda dialog: dialog.accept('karthik'))
    page.locator("#promptBtn").click()
    page.wait_for_timeout(3000)
    text=page.locator("#demo").inner_text()
    print(f"text :" , text)
    expect(page.locator("#demo")).to_have_text("Hello karthik! How are you today?")
    page.wait_for_timeout(3000)    