#! python3
# 2048.py - automates play of 2048 game using selenium. 
# Practice project from chapter 12 of 'Automate the boring stuff' by Al Sweigart.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# open Firefox and go to web page to play 2048.
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
# Save elements for pop-ups to variables for quick access.
GOTIT = (By.LINK_TEXT, 'Got it!')
X = (By.CSS_SELECTOR, '.ezmob-footer-close')
# Have the browser wait until the pop-up elements appear and are removed.
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(GOTIT)).click()
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(X)).click()
# Select the html element to interact with the game.
htmlEl = browser.find_element_by_tag_name('html')
# Save pattern of key presses to tuple.
keys_to_send = (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
# Find the game-over message element.
gameoverEl = browser.find_element_by_css_selector('.game-message > p:nth-child(1)')
# Using the is_displayed() method allows us to know when the game has ended.
while not gameoverEl.is_displayed():
    # Send the pattern of key presses while the game is ongoing.
    for key in keys_to_send:
        htmlEl.send_keys(key)
        time.sleep(0.2)
