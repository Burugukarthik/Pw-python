import pytest

from playwright.sync_api import Page,expect


def test_innerframe(page: Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frame3=page.frame(url='https://ui.vision/demo/webtest/frames/frame_3')
    frame3.locator("input[name='mytext3']").fill("Frame3")
    inside_frames=frame3.child_frames
    print(f"No .of inside_frames : {len(inside_frames)}")
    page.wait_for_timeout(3000)
     