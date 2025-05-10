import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bot

file_path = 'list'


def open_wordle():
    driver = webdriver.Firefox()
    driver.get("https://www.nytimes.com/games/wordle/index.html")

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="Play"]'))
    ).click()

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[data-testid='icon-close']"))
    ).click()

    return driver


def load_words():
    with open(file_path, 'r') as f:
        return f.readline().upper().strip().split()


def remove_word(word_to_remove):
    print(f"Removing {word_to_remove}")
    with open(file_path, "r+") as file:
        content = file.read()
        words = content.split()
        filtered_words = [w for w in words if w != word_to_remove.lower()]
        file.seek(0)
        file.write(" ".join(filtered_words))
        file.truncate()

def type_word(word, driver):
    element = driver.find_element(By.TAG_NAME, 'body')
    element.send_keys(word + Keys.RETURN)


def read_feedback(driver, row_number):
    """
    Returns a list representing the feedback:
    0 - correct, 1 - present, 2 - absent
    """
    row_selector = f"[aria-label='Row {row_number}']"
    row_elem = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, row_selector))
    )
    tiles = row_elem.find_elements(By.CSS_SELECTOR, "div")

    feedback = []
    for tile in tiles:
        state = tile.get_attribute("data-state")
        if state == 'correct':
            feedback.append(0)
        elif state == 'present':
            feedback.append(1)
        elif state == 'absent':
            feedback.append(2)
    return feedback


def play_game():
    words = load_words()
    driver = open_wordle()
    time.sleep(0.5)  # Ensure full page load
    word = 'CRANE'  # Starting word

    for attempt in range(1, 7):
        type_word(word, driver)
        time.sleep(2.0)

        feedback = read_feedback(driver, attempt)
        print(f"Attempt {attempt}: {word} -> {feedback}")

        if sum(feedback) == 0:
            print("Word guessed correctly!")
            remove_word(word)
            break

        words = bot.check_word(word, feedback, words)
        if not words:
            print("No valid words left.")
            break

        word = random.choice(words)


if __name__ == "__main__":
    play_game()
