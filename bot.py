import random
#1. load all 5 letter words
words = open('list', 'r').readline().split(' ')

def correct(position, letter):
	#remove all words have letter
	for word in list(words):
		if letter not in word[position]:
			words.remove(word)

def present(postion, letter):
	for word in list(words):
		#remove all words that dont have k[0]
		if letter not in word:
			words.remove(word)
			continue
		#remote all words that have k[0] in position,
		if letter in word[postion]:
			words.remove(word)

def absent(letter):
	#remove all words have letter
	for word in list(words):
		if letter in word:
			words.remove(word)

def checkWord(word, guess):
	position = 0
	for k in zip(word, guess):
		if k[1] == 0:
			correct(position, k[0])
		if k[1] == 1:
			present(position, k[0])
		if k[1] == 2:
			#unless the letter is correct in other position
			absent(k[0])
		position = position + 1

def correct2(position, letter):
	#remove all words have letter
	result = []
	for word in list(words):
		if letter in word[position]:
			result.append(word)
	#print(result)
	return result

def present2(postion, letter):
	result = []
	for word in list(words):
		#remove all words that dont have k[0]
		if letter in word:
			if letter not in word[postion]:
				result.append(word)
	print(result)			
	return result
	#remote all words that have k[0] in position,

def absent2(letter):
	result = []
	#remove all words have letter
	for word in list(words):
		if letter not in word:
			result.append(word)
	#print(result)
	return result

def checkWord2(word, guess):
	position = 0
	result = []
	for k in zip(word, guess):
		if k[1] == 0:
			result.append(correct2(position, k[0]))
		if k[1] == 1:
			result.append(present2(position, k[0]))
		if k[1] == 2:
			#unless the letter is correct in other position
			result.append(absent2(k[0]))
		position = position + 1
	#print(result)
	return result
#RATAL DEBUG 20222
#2. select random word
word = 'AGENE' #
word1 = '' # here may be a bug
word2 = ''
word3 = ''
word4 = ''
#3. send word to wordle
#4. get result from wordle
#change tuple to map of letter result

#What happens if the guess word has 
#the same letter twice, 
#but the real word has it once?

#print(len(words))
#query
word = 'AGENE' #
guess = [1,2,0,1,2]
checkWord(word, guess)
#print(words)

#print(len(words))
print(random.choice(words))


#5. process result
		# read array first line
			#if 0 nothing
			#if 1 add char to place[char, position] array
			#if 2 add char to miss[char, position] array
		# if place and miss are empty then print word of day, win and exit
		# if place not empty, remove all words that don't have the char or have it miss in position
		# if miss not empty, remove all words with char
#6 go to step 2
