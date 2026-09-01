import pytest

from playwright.sync_api import Page,expect

def test_static_web_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # Here the locators what we are using  is important we are work with the no.of rows,colums,rowdata

    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    # 1.count total no.of rows in a table nd verify them
    # every <tr> represents row in a table it represnts in a <tbody> in dom
    """
     table[name='BookTable'] tbody tr  it matches the 7 elements,css is doing it will retuen the 7 elements 
    """
    # rows=page.locator("table[name='BookTable'] tbody tr")
    # ^^instead od writing  total page.locator() its already stored in a table so we can wrirte
    rows=table.locator("tr")  #this is a short to rows=page.locator("table[name='BookTable'] tbody tr") "chaining of locator"
    expect(rows).to_have_count(7)

    # to count no.of row and to print them
    row_count=rows.count()
    print("Number of rows in a table: ",row_count)

    #count total no of colums/headers in table
    header=rows.locator("th")               #header/colum
    expect(header).to_have_count(4)

    header_count=header.count()
    print("Number of headers in a table: ",header_count)

    # read all the data from second row of the table
    tabel_data=rows.nth(2).locator("td")
    secondrow_data=tabel_data.all_inner_texts()
    print("Data in the second row of a table: ",secondrow_data)
    expect(tabel_data).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])
    print("this test is passed")
    # we printed above values one after another through looping
    for text in  secondrow_data:
        print(text)

    print("--- Printing All Rows Dynamically ---")

    # This loop repeats the process for rows 1, 2, 3, 4, 5, and 6
    for i in range(1, row_count):    #row_count =7
        tabel_data = rows.nth(i).locator("td")  # Dynamic locator using 'i'
        row_data = tabel_data.all_inner_texts()  # Grabs text for this specific row
        print(f"Row {i} data is: {row_data}")  # Prints it beautifully

        """
        --- Printing All Rows Dynamically ---
Row 1 data is: ['Learn Selenium', 'Amit', 'Selenium', '300']
Row 2 data is: ['Learn Java', 'Mukesh', 'Java', '500']
Row 3 data is: ['Learn JS', 'Animesh', 'Javascript', '300']
Row 4 data is: ['Master In Selenium', 'Mukesh', 'Selenium', '3000']
Row 5 data is: ['Master In Java', 'Amod', 'JAVA', '2000']
Row 6 data is: ['Master In JS', 'Amit', 'Javascript', '1000']
        """