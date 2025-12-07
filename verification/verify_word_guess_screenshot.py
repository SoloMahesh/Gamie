from playwright.sync_api import sync_playwright
import os

def capture_word_guess_modal():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        url = f"file://{os.getcwd()}/games/word-guess.html"
        page.goto(url)

        # Manually trigger the win modal
        page.evaluate("showResult(true)")

        # Wait for animation/modal visibility
        page.wait_for_selector("#resultModal")

        # Take screenshot
        output_path = "verification/word_guess_modal.png"
        page.screenshot(path=output_path)
        print(f"Screenshot saved to {output_path}")

        browser.close()

if __name__ == "__main__":
    capture_word_guess_modal()
