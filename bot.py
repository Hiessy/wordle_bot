import random
#1. load all 5 letter words
words2 = open('list', 'r').readline().split(' ')

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
			continue
		#remote all words that have k[0] in position,
		if letter in word[postion]:
			words.remove(word)
	return words

def absent(letter, words, position, let):
	#remove all words have letter
	for word in list(words):
		if letter == let:
			if letter in word and (letter not in word[position] or word.count(letter) != 1):
				words.remove(word)
		elif letter in word:
			words.remove(word)
	#print(words)		
	return words

def checkWord(word, guess, words):
	position = 0
	cor = 0
	letter = ''
	for k in zip(word, guess):
		if k[1] == 0:
			cor = position
			letter = k[0]
			words = correct(position, k[0], words)
		if k[1] == 1:
			words = present(position, k[0], words)
		if k[1] == 2:
			#unless the letter is correct in other position
			words = absent(k[0], words, cor, letter)
		position = position + 1
	return words

#RATAL DEBUG 20222
#2. select random word
word = 'AGENE' #
word1 = '' # here may be a bug
word2 = ''
word3 = ''
word4 = ''

guess = [1,2,0,1,2] ## should be read from the webpage

result = checkWord(word, guess, words2)


print(result)