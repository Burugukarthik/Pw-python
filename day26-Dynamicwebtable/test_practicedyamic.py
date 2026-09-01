import pytest

from playwright.sync_api import Page,expect

def test_dynamictable(page: Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")
    page.wait_for_selector("table.table thead")
    header=page.locator("table.table thead th").all_inner_texts()
    header=[h.strip() for h in header]
    name_idx=header.index("Name")
    cpu_index=header.index("CPU")

    rows=page.locator("table.table tbody tr").all()

    for row in rows:
        cells=row.locator("td")
        browser_name=cells.nth(name_idx).inner_text().strip()
        if browser_name== "Chrome":
           cpu_load=cells.nth(cpu_index).inner_text().strip()

        break
    assert cpu_load is not None, "Chrome row was not found in the table"
    print(f"cpu_load from table: {cpu_load}")
