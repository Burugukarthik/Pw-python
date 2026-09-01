from itertools import count

import pytest
from playwright.sync_api import Page,expect

def test_bootstrapdropdown(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(5000)

    page.get_by_text('PIM').click()

    """
    major drop down in bootstrap dropdown is we can't see the specific one in  DOM structure they are hidden
    In DOM structure go to selector hub in that there will be a turn on debugger ,immediatly try to expand the dropdown
    then screen will be frized,once it is frized go to elements now inspect this dropdown options 
      
    """

# click on the Job title dropdown
    page.locator("form i").nth(2).click() #this will open options from the dropdown

    # capture all the options from dropdown
    options=page.locator("div[role='listbox'] span")
    # capturing all the options into the variable "options"
    expect(options.first).to_be_visible()
    count=options.count()   #using the options counted them  options.count and stored them in a count
    print("Number of options in the dropdown",count) # printing the count

    page.wait_for_timeout(5000)

    #print all the options
    print("All the options from the dropdown.....",options.all_text_contents())

    #print all the options text using loop
    for i in range(count):
        print(options.nth(i).text_content())
        '''
                 range(5)
               │
               ▼
         0 → options.nth(0) → Automation Testing → print()

         1 → options.nth(1) → Automation Tester → print()

         2 → options.nth(2) → CEO → print()

         3 → options.nth(3) → CFO → print()

         4 → options.nth(4) → CTO → print()

                 '''


        #   now we are selecting the option from the dropdown
        '''
        select_option method is not there so we need to again get each and every option compare with ur expected one

        "select / click on specific option"
        '''

    for i in range(count):
        text=options.nth(i).inner_text() #

        if text=="Database Administrator":
           print("option to be selected----->", text)
           print("Matching Success")
           options.nth(i).click()
        break
    page.wait_for_timeout(5000)

