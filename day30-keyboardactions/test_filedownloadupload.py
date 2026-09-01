import pytest

from playwright.sync_api import Playwright,Page,expect

def test_singlefileupload(page: Page):
    """
    page.goto('https://testautomationpractice.blogspot.com/')

    # set_input_files("").....>inside just we need to specify the path of the file where exactly file is exist
    page.locator("#singleFileInput").set_input_files("Uploads/pyfile1.txt")
    page.locator("button:has-text('Upload Single File')").click()
    #validation
    msg=page.locator("#singleFileStatus")
    expect(msg).to_contain_text("pyfile1.txt")
    print("File upload Successful")
    
    # how to upload multiple files if we have group of files
    files=["Uploads/pyfile1.txt","Uploads/pyfile2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()
    msg=page.locator("#multipleFilesStatus")
    expect(msg).to_contain_text("pyfile1.txt")
    expect(msg).to_contain_text("pyfile2.txt")
    for file in files:
        print("File upload Successful",file)
    """
    # Assianment
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")
    page.locator("#filesToUpload").set_input_files("Uploads/pyfile1.txt")
    msg=page.locator("ul[id='fileList'] li")
    expect(msg).to_contain_text("pyfile1.txt")
    print("File is uploaded Successful")