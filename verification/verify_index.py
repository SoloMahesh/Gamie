from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Determine the absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        page.goto(file_path)

        # 1. Verify Home Page Load
        page.wait_for_selector('h1:has-text("Welcome to the game world")')
        page.screenshot(path="verification/home_page.png")

        # 2. Verify Search Feature
        page.fill('#game-search', 'Snake')
        page.wait_for_timeout(500) # Wait for filter
        page.screenshot(path="verification/search_result.png")

        # 3. Verify Explore Button Scroll
        # Reset search
        page.fill('#game-search', '')
        page.click('button:has-text("Explore Games")')
        page.wait_for_timeout(1000) # Wait for scroll
        page.screenshot(path="verification/scrolled_to_library.png")

        # 4. Verify New Games are present in list
        page.wait_for_selector('p:has-text("Memory Match")')
        page.wait_for_selector('p:has-text("Tower Stack")')
        page.wait_for_selector('p:has-text("Whack-a-Mole")')
        page.wait_for_selector('p:has-text("Flappy Bird Clone")')
        page.wait_for_selector('p:has-text("Simon Says")')
        page.screenshot(path="verification/new_games_listed.png")

        browser.close()

if __name__ == "__main__":
    run()
