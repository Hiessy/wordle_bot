import random
#1. load all 5 letter words
wordsInit = open('list', 'r').readline().split(' ')

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
		#AMBAN
		#TANGA
		if letter in word[postion]:
			words.remove(word)
	return words

def absent(letter, words, position, let, correct):
	#remove all words have letter
	#AMBAN
	#pos 0 and let A
	for word in list(words):
		if letter == let:
			if letter in word and word.count(letter) != 1:
				if correct:
					if letter not in word[position]: 
						words.remove(word)
				else:
					if letter in word[position]: 
						words.remove(word)
		elif letter in word:
			words.remove(word)
	#
	#print('lenght ' + str(len(words)))
	#print('position ' + str(position))
	#print('leettter' + let)
	return words

def checkWord(word, guess, words):
	position = 0
	cor = 0
	letter = ''
	hit = False			 
	for k in zip(word, guess):
		if k[1] == 0:
			#SALPA bug
			if(word.count(k[0]) != 1):
				cor = position
				letter = k[0]
				hit = True
			words = correct(position, k[0], words)
		if k[1] == 1:
			#AMBAN
			if(word.count(k[0]) != 1):
				cor = position
				letter = k[0]
				hit = False
			words = present(position, k[0], words)
		if k[1] == 2:
			#unless the letter is correct in other position
			#print('processing word::::' + word)
			#print('processing letter::::' + k[0])
			words = absent(k[0], words, cor, letter, hit)
		position = position + 1
	return words