import pytest

from playwright.sync_api import Page,expect
def test_static_practice(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    no_of_rows=table.locator("tr")
    count_of_rows=no_of_rows.count()
    print(f"There are {count_of_rows} rows")

    table_header=no_of_rows.locator("th")
    print(table_header.all_inner_texts())
    # print(f"There are {len(data)} rows")

    row_data=no_of_rows.nth(2).locator("td")
    print(row_data.all_inner_texts())
    expect(row_data).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
    print("Assertion passed")
    for i in range(1,count_of_rows):
        data=no_of_rows.nth(i).locator("td")
        total_rowdata=data.all_inner_texts()
        print(f"Row {i} data is: {total_rowdata}")