from playwright.sync_api import sync_playwright
import os

def check_word_guess_modal():
    print("Checking Word Guess modal...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the page
        url = f"file://{os.getcwd()}/games/word-guess.html"
        page.goto(url)

        # We need to simulate a game over or a win to see the modal.
        # It's easier to simulate a loss by forcing the game state or mocking the word.

        # Let's inject a script to force a win condition or just call the function directly
        # verifying the function exists and works is good enough given the manual override I did.

        # Option 1: Mock the target word to "AAAAA" and type it.
        # But the word list is random.
        # Easier: Execute showResult(true) in console and check if modal appears.

        page.evaluate("showResult(true)")

        # Check if modal is visible
        modal = page.locator("#resultModal")
        if modal.is_visible():
            print("✅ Word Guess: Modal appeared after calling showResult(true).")
        else:
            print("❌ Word Guess: Modal did NOT appear.")

        # Check content
        title = page.locator("#modalTitle").inner_text()
        if "Won" in title:
            print(f"✅ Word Guess: Modal title correct: {title}")
        else:
            print(f"❌ Word Guess: Modal title incorrect: {title}")

        # Test Close/Reset
        page.click("button.modal-btn") # "Play Again"

        if not modal.is_visible():
            print("✅ Word Guess: Modal closed after clicking Play Again.")
        else:
            print("❌ Word Guess: Modal did NOT close.")

        browser.close()

if __name__ == "__main__":
    check_word_guess_modal()
