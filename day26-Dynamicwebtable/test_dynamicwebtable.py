# "we are gooing to see  dynamic webtable ,dynamic means data is going to change in the table "

import pytest

from playwright.sync_api import Page,expect
def test_dynamicwebtable(page: Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")
    t_body=page.locator("table.table tbody")
    rows=t_body.locator("tr").all()
    cpu_load=''
    for row in rows:
       table_data=row.locator("td").nth(1).inner_text()
       # print(f'table_data:{table_data}')
       if table_data=="Chrome":
           cpu_load=row.locator("td:has-text('%')").inner_text()
           print(f'cpu_load:{cpu_load}')
           break

    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)

    page.wait_for_timeout(5000)