from playwright.sync_api import Page,expect

def test_verify_inputbox(page: Page):
 """
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    text_box=page.locator("[name='username']")

    #check visibiltiy of the element
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()
 """
 page.goto("https://testautomationpractice.blogspot.com/")
 input_box=page.locator("#name")

 #check visibiltiy of the element
 expect(input_box).to_be_visible()
 expect(input_box).to_be_enabled()

 #check the attribute of the element
 length=input_box.get_attribute("maxlength")
 print("Maximun lenghth of the inputbox:",length)

 # check by filling the input box
 input_box.fill("Karthik Burugu")

 # get the input value from the input box

 value=input_box.input_value()
 print("Entered value:", value)

 page.wait_for_timeout(6000)

 """
 from playwright.sync_api import Page, expect

def test_verify_inputbox(page: Page):
    # 1. Navigate
    page.goto("https://testautomationpractice.blogspot.com/")
    input_box = page.locator("#name")

    # 2. Assertions (Health checks)
    expect(input_box).to_be_visible()
    # Real-world check: Verify the max length attribute equals a specific expected number (e.g., 50)
    expect(input_box).to_have_attribute("maxlength", "50") 

    # 3. Action
    input_box.fill("Karthik Burugu")

    # 4. Real-world Verification (No print statements, let the framework assert it)
    expect(input_box).to_have_value("Karthik Burugu")
    
    # Notice: No page.wait_for_timeout() here. The test finishes instantly and cleanly!
 """