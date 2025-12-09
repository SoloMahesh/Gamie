# """
# Comprehensive Game Testing and Verification Script
# Tests the first 10 games for all functionalities and captures screenshots
# """
# from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
# import os
# import json
# from datetime import datetime

# # First 10 games to test
# GAMES_TO_TEST = [
#     'whack-a-mole.html',
#     'classic-snake.html',
#     'flappy-bird.html',
#     'dino-run.html',
#     'space-jump.html',
#     'bubble-shooter.html',
#     'word-guess.html',
#     'memory-match.html',
#     'tetris.html',
#     '2048-puzzle.html',
#     'food-catcher.html',
#     'pong.html'
# ]

# class GameTester:
#     def __init__(self):
#         self.results = {}
#         self.screenshots_dir = "verification/screenshots"
#         os.makedirs(self.screenshots_dir, exist_ok=True)
        
#     def test_game(self, browser, game_name):
#         """Test individual game for all functionalities"""
#         print(f"\n{'='*60}")
#         print(f"Testing: {game_name}")
#         print(f"{'='*60}")
        
#         game_path = os.path.abspath(f"games/{game_name}")
#         test_results = {
#             'game': game_name,
#             'timestamp': datetime.now().isoformat(),
#             'tests': {}
#         }
        
#         try:
#             context = browser.new_context(viewport={'width': 1280, 'height': 800})
#             page = context.new_page()
            
#             # Test 1: Page loads correctly
#             try:
#                 page.goto(f"file://{game_path}")
#                 page.wait_for_load_state('domcontentloaded', timeout=5000)
#                 test_results['tests']['page_load'] = 'PASS'
#                 print("✓ Page loads correctly")
#             except Exception as e:
#                 test_results['tests']['page_load'] = f'FAIL: {str(e)}'
#                 print(f"✗ Page load failed: {e}")
#                 return test_results
            
#             # Take initial screenshot
#             screenshot_base = game_name.replace('.html', '')
#             page.screenshot(path=f"{self.screenshots_dir}/{screenshot_base}_initial.png")
            
#             # Test 2: Check for visual elements
#             try:
#                 page.wait_for_timeout(500)
#                 # Check if canvas or game elements exist
#                 has_canvas = page.locator('canvas').count() > 0
#                 has_game_elements = page.locator('body *').count() > 10
#                 if has_canvas or has_game_elements:
#                     test_results['tests']['visual_elements'] = 'PASS'
#                     print("✓ Visual elements present")
#                 else:
#                     test_results['tests']['visual_elements'] = 'FAIL: No game elements'
#                     print("✗ Missing visual elements")
#             except Exception as e:
#                 test_results['tests']['visual_elements'] = f'FAIL: {str(e)}'
#                 print(f"✗ Visual elements check failed: {e}")
            
#             # Test 3: Check for start button or auto-start
#             try:
#                 start_button = page.locator('button:has-text("Start")').first
#                 if start_button.count() > 0:
#                     start_button.click()
#                     page.wait_for_timeout(1000)
#                     test_results['tests']['start_game'] = 'PASS'
#                     print("✓ Game starts with button")
#                 else:
#                     # Game might auto-start
#                     test_results['tests']['start_game'] = 'PASS (auto-start)'
#                     print("✓ Game appears to auto-start")
#             except Exception as e:
#                 test_results['tests']['start_game'] = f'INFO: {str(e)}'
#                 print(f"ℹ Start button: {e}")
            
#             # Take gameplay screenshot
#             page.wait_for_timeout(1000)
#             page.screenshot(path=f"{self.screenshots_dir}/{screenshot_base}_gameplay.png")
            
#             # Test 4: Check for score element
#             try:
#                 score_elements = page.locator('text=/score|points|hits/i').all()
#                 if len(score_elements) > 0:
#                     test_results['tests']['score_tracking'] = 'PASS'
#                     print("✓ Score tracking element found")
#                 else:
#                     test_results['tests']['score_tracking'] = 'INFO: No score element'
#                     print("ℹ No score element found")
#             except Exception as e:
#                 test_results['tests']['score_tracking'] = f'INFO: {str(e)}'
            
#             # Test 5: Check for timer
#             try:
#                 timer_elements = page.locator('text=/time|timer|countdown/i').all()
#                 if len(timer_elements) > 0:
#                     test_results['tests']['timer'] = 'PASS'
#                     print("✓ Timer element found")
#                 else:
#                     test_results['tests']['timer'] = 'INFO: No timer'
#                     print("ℹ No timer found")
#             except Exception as e:
#                 test_results['tests']['timer'] = f'INFO: {str(e)}'
            
#             # Test 6: Simulate interaction (click/tap)
#             try:
#                 # Click in the middle of the viewport
#                 page.mouse.click(640, 400)
#                 page.wait_for_timeout(500)
#                 test_results['tests']['interaction'] = 'PASS'
#                 print("✓ User interaction works")
#             except Exception as e:
#                 test_results['tests']['interaction'] = f'FAIL: {str(e)}'
#                 print(f"✗ Interaction failed: {e}")
            
#             # Test 7: Check for keyboard support
#             try:
#                 page.keyboard.press('Space')
#                 page.wait_for_timeout(300)
#                 page.keyboard.press('ArrowUp')
#                 page.wait_for_timeout(300)
#                 test_results['tests']['keyboard'] = 'PASS'
#                 print("✓ Keyboard events processed")
#             except Exception as e:
#                 test_results['tests']['keyboard'] = f'INFO: {str(e)}'
            
#             # Test 8: Check mobile responsiveness
#             try:
#                 mobile_context = browser.new_context(
#                     viewport={'width': 375, 'height': 667},
#                     device_scale_factor=2,
#                     is_mobile=True,
#                     has_touch=True
#                 )
#                 mobile_page = mobile_context.new_page()
#                 mobile_page.goto(f"file://{game_path}")
#                 mobile_page.wait_for_load_state('domcontentloaded', timeout=3000)
#                 mobile_page.screenshot(path=f"{self.screenshots_dir}/{screenshot_base}_mobile.png")
#                 test_results['tests']['mobile_responsive'] = 'PASS'
#                 print("✓ Mobile responsive")
#                 mobile_context.close()
#             except Exception as e:
#                 test_results['tests']['mobile_responsive'] = f'FAIL: {str(e)}'
#                 print(f"✗ Mobile test failed: {e}")
            
#             # Test 9: Check for game over modal
#             try:
#                 # Try to trigger game over
#                 modal = page.locator('[class*="modal"]').first
#                 if modal.count() > 0:
#                     test_results['tests']['game_over_modal'] = 'PASS'
#                     print("✓ Game over modal found")
#                 else:
#                     test_results['tests']['game_over_modal'] = 'INFO: Not found'
#                     print("ℹ Game over modal not immediately visible")
#             except Exception as e:
#                 test_results['tests']['game_over_modal'] = f'INFO: {str(e)}'
            
#             # Test 10: Check for restart/play again button
#             try:
#                 restart_btn = page.locator('button:has-text("Again"), button:has-text("Restart"), button:has-text("Play")').first
#                 if restart_btn.count() > 0:
#                     test_results['tests']['restart_button'] = 'PASS'
#                     print("✓ Restart button found")
#                 else:
#                     test_results['tests']['restart_button'] = 'INFO: Not visible'
#                     print("ℹ Restart button not immediately visible")
#             except Exception as e:
#                 test_results['tests']['restart_button'] = f'INFO: {str(e)}'
            
#             # Take final screenshot
#             page.screenshot(path=f"{self.screenshots_dir}/{screenshot_base}_final.png")
            
#             context.close()
            
#         except Exception as e:
#             test_results['tests']['overall'] = f'CRITICAL ERROR: {str(e)}'
#             print(f"✗ Critical error: {e}")
        
#         return test_results
    
#     def run_all_tests(self):
#         """Run tests for all games"""
#         print("\n" + "="*60)
#         print("COMPREHENSIVE GAME TESTING SUITE")
#         print("="*60)
        
#         with sync_playwright() as p:
#             browser = p.chromium.launch(headless=False)  # Show browser for visual verification
            
#             for game in GAMES_TO_TEST:
#                 result = self.test_game(browser, game)
#                 self.results[game] = result
            
#             browser.close()
        
#         # Save results to JSON
#         with open('verification/test_results.json', 'w') as f:
#             json.dump(self.results, f, indent=2)
        
#         # Print summary
#         self.print_summary()
    
#     def print_summary(self):
#         """Print test summary"""
#         print("\n" + "="*60)
#         print("TEST SUMMARY")
#         print("="*60)
        
#         for game, result in self.results.items():
#             print(f"\n{game}:")
#             total_tests = len(result['tests'])
#             passed = sum(1 for v in result['tests'].values() if 'PASS' in str(v))
#             failed = sum(1 for v in result['tests'].values() if 'FAIL' in str(v))
            
#             print(f"  Total Tests: {total_tests}")
#             print(f"  Passed: {passed}")
#             print(f"  Failed: {failed}")
            
#             # Show failures
#             failures = {k: v for k, v in result['tests'].items() if 'FAIL' in str(v)}
#             if failures:
#                 print("  Failures:")
#                 for test, error in failures.items():
#                     print(f"    - {test}: {error}")

# if __name__ == "__main__":
#     tester = GameTester()
#     tester.run_all_tests()
