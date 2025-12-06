from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Use a mobile viewport to verify the layout change
        page = browser.new_page(viewport={"width": 375, "height": 667})

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        page.goto(file_path)

        # Verify new games are present
        page.wait_for_selector('p:has-text("Tetris Clone")')
        page.wait_for_selector('p:has-text("Dino Run")')
        page.wait_for_selector('p:has-text("Word Guess")')
        page.wait_for_selector('p:has-text("Fruit Slicer")')

        # Verify grid layout logic (check class presence)
        grid = page.locator('#games-grid')
        classes = grid.get_attribute('class')
        print(f"Grid classes: {classes}")

        # Take screenshot of the grid in mobile view
        page.locator('#explore-library').scroll_into_view_if_needed()
        page.screenshot(path="verification/mobile_grid_layout.png")

        browser.close()

if __name__ == "__main__":
    run()
