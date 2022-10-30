import random

first = "//*[contains(text(), '"
last = "')]"
words = open('list', 'r').readline().split(' ')
word = random.choice(words)
print(first + word[0].lower() + last)