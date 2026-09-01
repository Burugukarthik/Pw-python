# we need to navigate each page grab all the rows and colums present in next pages and till last pages

import pytest

from playwright.sync_api import Page,expect

def test_paginationtable(page: Page):
    page.goto("https://datatables.net/")
    all_row_data=[]
    has_more_pages =True

    while has_more_pages:      # we preffer whileloop
        rows=page.locator("#example tbody tr").all()
        for row in rows:                              #to read each and every row from rows
           all_row_data.append(row.inner_text()) # when ever i write innertext the data present in td will be returned
        page.wait_for_timeout(3000)
  # this will ^ repeat times after that it will go to while loop,so while loop is stiil true and again it will go to
# another page
# Once you read all the ten rows,we need to go to the next page and again get the ten rows
        next_button=page.locator("button[aria-label='Next']")  #grabbed the next button
        #we will now the state of the button based on class attribute
        '''
        class=dt-paging-button next 1-5 pages it will return the next page  
        class=dt-paging-button disabled next  last page it will return
        '''
        is_disabled=next_button.get_attribute("class")
        if "disabled" in is_disabled:
            has_more_pages=False
        else:
            next_button.click()

        print(f"data presnt in table :{all_row_data}")

# now we are checking that filters are workimg are not if we select 10rows or 25 rows it should work exactly
@pytest.mark.skip
def test_filter_rows(page: Page):
    page.goto("https://datatables.net/")
    dropdown=page.locator("#dt-length-0")
    dropdown.select_option(label="25")
    rows = page.locator("#example tbody tr")
    print(f"rows: {rows}")
    expect(rows).to_have_count(25)