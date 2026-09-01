from playwright.sync_api import Page,expect

def test_singleselectdropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.locator("#country").select_option("India")

    # to capture all the options we use css #id>option
    dropdown_options=page.locator("#country>option") #this will return all the options
    expect(dropdown_options).to_have_count(10)

    # I want to print them in a console window ,if we want to capture then
    # to capture the text of the particular element we use "text_content",
    # so here we have multiple elements then "all text content"
    # dropdown_options.all_text_contents() ...this will actually return all list collections // from the particular list
    # we will read each and every text into a variable using for loop like for text in that text wull read
    # text.strip() It will trim the spaces and it will  capture exact text from the element
    options_text=[text.strip()for text in dropdown_options.all_text_contents()]
    print(options_text)

    # printing countries using loop
    for options in options_text:
        print(options)

    '''
📌 Working with Multiple Elements in Playwright
page.locator("selector") →         Creates a locator for one or more matching elements.
expect(locator).to_have_count(n) → Verifies how many elements match the locator.
all_text_contents() →              Returns the text of all matched elements as a Python list.
strip() →                          Removes leading and trailing whitespace from each string.

List comprehension is a short way to transform every item in a list:

cleaned = [text.strip() for text in texts]
Use a for loop to process or print each item individually.

Memory trick:
Locate → Validate → Extract → Clean → Store → Use (LVECSU)

If you practice this pattern, you'll notice it applies not just to dropdowns, 
but also to tables, lists, search results, menu items, checkboxes, and any collection of elements in Playwright.
 '''