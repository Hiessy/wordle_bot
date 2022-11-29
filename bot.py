import random
#1. load all 5 letter words
wordsInit = open('list', 'r').readline().split(' ')


def getPosition(letter, t):
	count = 0
	for k in t:
		if k[0] == letter and (k[1] == 0 or k[1] == 1):
			return count
		count += 1
	return -1

def correct(position, letter, words):
	#remove all words have letter
	for word in list(words):
		if letter not in word[position]:
			words.remove(word)

	return words

def present(postion, letter, words):

	for word in list(words):
		#remove all words that dont have k[0]
		if letter not in word:
			words.remove(word)
		elif letter in word[postion]:
			words.remove(word)
	return words

def absent(letter, words, position, t):
	correctPos = getPosition(letter, t)
	print(correctPos)
	for word in list(words):
		if letter in word:
			if correctPos > -1:
				if word[correctPos] == letter:
				 	if word[correctPos] != letter:
							words.remove(word)
			else:
				words.remove(word)
	return words


# have to pass another parameter that would be hits
# if tuple on word and guess and then 
def checkWord(word, guess, words):
	#tuple and paass
	print(guess)
	print(word)
	position = 0
	t = zip(word, guess)		 
	for k in t:
		if k[1] == 0:
			#SALPA bug
			words = correct(position, k[0], words)
		if k[1] == 1:
			#AMBAN
			words = present(position, k[0], words)
		if k[1] == 2:
			words = absent(k[0], words, position, zip(word, guess))
		position = position + 1

	return words