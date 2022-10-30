from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.get("https://www.nytimes.com/games/wordle/index.html")
assert "Wordle - The New York Times" in driver.title

close = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
words = open('list', 'r').readline().split(' ')
close.click()
word = random.choice(words)
assert len(word) == 5
time.sleep(0.25) #sleep for 250 milliseconds
actions = ActionChains(driver)
for l in word:
	actions.send_keys(l)
actions.perform()
actions.send_keys(Keys.RETURN)
actions.perform()
first = "//*[contains(text(), '"
last = "')]"
w = word[0].lower()
va = str(first + w + last)

row1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Row 1']")))
print(row1)
print(driver.find_element(By.XPATH, va))