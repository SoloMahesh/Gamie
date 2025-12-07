from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 800, 'height': 600})
        page = context.new_page()

        # Get absolute path to the game file
        game_path = os.path.abspath("games/space-jump.html")
        page.goto(f"file://{game_path}")

        # Simulate game over condition to see Play Again button
        page.evaluate("gameOver()")
        page.wait_for_selector("#gameOver", state="visible")

        # Take screenshot of Space Jump Game Over
        page.screenshot(path="verification/space_jump_gameover.png")
        print("Space Jump screenshot taken")

        # --- Bubble Shooter ---
        game_path = os.path.abspath("games/bubble-shooter.html")
        page.goto(f"file://{game_path}")

        # Wait for canvas to be drawn
        page.wait_for_timeout(1000)

        # Take screenshot of Bubble Shooter (should see ball ready to shoot)
        page.screenshot(path="verification/bubble_shooter_ready.png")
        print("Bubble Shooter screenshot taken")

        # --- Dino Run ---
        game_path = os.path.abspath("games/dino-run.html")
        page.goto(f"file://{game_path}")

        # Simulate collision
        page.evaluate("gameRunning = false; document.getElementById('finalScore').innerText = score; const finalScoreEl = document.getElementById('finalScore'); finalScoreEl.style.animation = 'none'; finalScoreEl.offsetHeight; finalScoreEl.style.animation = 'popIn 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275)'; document.getElementById('gameOver').style.display = 'flex';")

        page.wait_for_selector("#gameOver", state="visible")
        page.wait_for_selector("#finalScore", state="visible")

        # Take screenshot of Dino Run Game Over
        page.screenshot(path="verification/dino_run_gameover.png")
        print("Dino Run screenshot taken")

        # --- Word Guess ---
        game_path = os.path.abspath("games/word-guess.html")
        page.goto(f"file://{game_path}")

        # Simulate Win
        page.evaluate('showModal("Splendid!", "You found the word!")')
        page.wait_for_selector("#gameModal", state="visible")

        # Take screenshot of Word Guess Modal
        page.screenshot(path="verification/word_guess_modal.png")
        print("Word Guess screenshot taken")

        browser.close()

if __name__ == "__main__":
    run()
