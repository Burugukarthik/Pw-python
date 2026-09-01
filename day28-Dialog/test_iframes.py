import pytest
from playwright.sync_api import Page,expect


def test_frames(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    # A frame (iframe) is simply a webpage inside another webpage.
    frames=page.frames  #It returns a list of every frame present on the page.
#page.frames returns a list of all frame objects present on the current page,including the main frame and all childiframes.
    print(f"No of Frames ,{len(frames)}")
    # Frame 1  ...>To grab the Frame there are "three" specific ways
    # frame_locator - When ever we want to get the frame we use frame _locator()   OPTION 1
    # page.frame(url="")by using this also we will get the frame by url            OPTION 2
    # page.frame("By using name of the frame")
    frame1=page.frame(url='https://ui.vision/demo/webtest/frames/frame_1')
    inputbox=frame1.locator("input[name='mytext1']")
    inputbox.fill("Welcome")
    expect(inputbox).to_have_value("Welcome")
    print(inputbox.input_value())


    page.wait_for_timeout(3000)
 