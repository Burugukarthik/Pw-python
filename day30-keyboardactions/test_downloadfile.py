import os

import pytest
from playwright.sync_api import Page,expect

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator('#inputText').fill("Learning the downloadimg Automation")
    page.locator('#generateTxt').click()
    # register an evev nt
    page.on("download",lambda download: download.save_as("downloads/testfile.txt"))
    page.locator('#txtDownloadLink').click()
    page.wait_for_timeout(5000)

   #Now we should we verify the downloaded file it is present or not
    if os.path.exists("downloads/testfile.txt"):
        print("file exists")
    else:
       print("file does not exist")
