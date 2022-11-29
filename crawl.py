from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.action_chains import ActionChains
import time
import bot

def openWordle():
	driver = webdriver.Firefox()
	driver.get("https://www.nytimes.com/games/wordle/index.html")
	assert "Wordle - The New York Times" in driver.title
	close = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Close']")))
	time.sleep(0.25)
	close.click()
	return driver


def chooseRandomWord():
	words = open('list', 'r').readline().split(' ')
	word = random.choice(words)
	return word

def typeWord(word, driver):
	actions = ActionChains(driver)
	for l in word:
		actions.send_keys(l)
	actions.perform()
	actions.send_keys(Keys.RETURN)
	actions.perform()


driver = openWordle()
time.sleep(0.25) #sleep for 250 milliseconds
word = 'ALIVE'#chooseRandomWord()
typeWord(word, driver)
time.sleep(2.25) 

result = open('list', 'r').readline().split(' ')
for x in range (1, 7):
	label = (f"[aria-label='Row {x}']")
	elems_row1 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, label))).find_elements(By.CSS_SELECTOR, "div")
	guess = []
	for el in elems_row1:
		if el.get_attribute("data-state") == 'absent':
			guess.append(2)	
		if el.get_attribute("data-state") == 'correct':
			guess.append(0)	
		if el.get_attribute("data-state") == 'present':
			guess.append(1)
	result = bot.checkWord(word, guess, result)
	print(len(result))
	word = random.choice(result)
	typeWord(word, driver)
	time.sleep(2)
