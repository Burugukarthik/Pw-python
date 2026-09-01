import pytest
from playwright.sync_api import Page,expect

def test_dynamic_webtable(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("table#taskTable thead tr")
    headers=page.locator("table#taskTable thead th").all_inner_texts()
    headers=[h.strip()for h in headers]
    print(headers)
    inx_name=headers.index("Name")
    cpu_load=headers.index("CPU (%)")

    rows=page.locator("table#taskTable tbody tr").all()
    for row in rows:
        t_data=row.locator("td")
        browswe_name=t_data.nth(inx_name).inner_text().strip()

        if browswe_name=="Chrome":
            cpu=t_data.nth(cpu_load).inner_text().strip()

            break


    print(f"CPU LOAD: {cpu}")
