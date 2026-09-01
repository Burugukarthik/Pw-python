import pytest
from playwright.sync_api import Page, expect


def test_dynamic_webtable(page: Page):
    # 1. Go to the page
    page.goto("https://practice.expandtesting.com/dynamic-table")

    # 2. Wait until the table rows are actually rendered (table loads via JS)
    page.wait_for_selector("table.table tbody tr")

    # 3. Read the header row to find out WHERE "Name" and "CPU" columns are
    #    (this page shuffles column order on every reload, so we can't hardcode positions)
    headers = page.locator("table.table thead th").all_inner_texts()
    headers = [h.strip() for h in headers]
    name_idx = headers.index("Name")
    cpu_idx = headers.index("Memory")

    # 4. Loop through every row in the table body
    rows = page.locator("table.table tbody tr").all()
    # cpu_load = None

    for row in rows:
        cells = row.locator("td")
        browser_name = cells.nth(name_idx).inner_text().strip()

        if browser_name == "Firefox":
            cpu_load = cells.nth(cpu_idx).inner_text().strip()


            break

    # 5. Make sure Chrome was actually found — fail loudly if not
    # assert cpu_load is not None, "Chrome row was not found in the table"



    # 6. Compare the table's CPU value against the yellow label below the table
    # expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)