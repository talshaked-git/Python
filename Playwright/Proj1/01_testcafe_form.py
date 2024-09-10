from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False) #slow_mo=500 (or more) for debugging purposes. args=["--start-maximized"]

    page = browser.new_page() #when using maximized mode, change manually to no_viewport=True

    page.goto("https://devexpress.github.io/testcafe/example/")
    myName = "Tal"
    textbox = page.get_by_role('textbox').nth(0).press_sequentially(myName)
    checkboxes = page.get_by_role('checkbox').all()
    
    for box in checkboxes:
        box.check()
    
    slider = page.locator('#slider')
    box = slider.bounding_box()
    # Calculate the desired position on the slider (e.g., move it halfway)
    target_x = box['x'] + box['width'] * 0.5  # Moves to 50%
    target_y = box['y'] + box['height'] / 2
    page.mouse.click(target_x, target_y)

    page.get_by_label("windows").check()

    textbox = page.get_by_role('textbox').nth(1).fill("Testing using automation")

    page.get_by_role('button').nth(1).click()

    thank_you_header = page.get_by_test_id("thank-you-header")
    expect(thank_you_header).to_contain_text(myName)

    browser.close()