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
	#		
	return words

def checkWord(word, guess, words):
	position = 0
	cor = 0
	letter = ''
	for k in zip(word, guess):
		#print(position)
		if k[1] == 0:
			#SALPA bug
			if(word.count(k[0]) != 1):
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
 #word = 'AGENE'
word1 = 'LINEN' # here may be a bug
word2 = 'SALPA'
word3 = 'BALOO'
word4 = 'RALLY'
word5 = 'GALUT'

guess1 = [1,2,2,2,2] ## should be read from the webpage
guess2 = [2,0,0,2,2] ## should be read from the webpage
guess3 = [2,0,0,2,2] ## should be read from the webpage
guess4 = [2,0,0,2,2] ## should be read from the webpage
guess5 = [2,0,0,2,1] ## should be read from the webpage


result2 = checkWord(word1, guess1, wordsInit)
result3 = checkWord(word2, guess2, result2)
result4 = checkWord(word3, guess3, result3)
result5 = checkWord(word4, guess4, result4)
result6 = checkWord(word5, guess5, result5)

print(len(result6))
print(random.choice(result6))