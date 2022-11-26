import bot
import random
#RATAL DEBUG 20222
#

word1 = 'ALIVE' # here may be a bug
word2 = 'ROJIS'
word3 = 'PUTTI'
#word4 = 'PALET'
#word5 = 'WALTZ'
#TODO poner la funcion directamente en vez del nro
guess1 = [2, 2, 1, 2, 2] ## should be read from the webpage
guess2 = [2, 2, 2, 1, 2]## should be read from the webpage
guess3 = [2, 2, 1, 2, 1] ## should be read from the webpage
#guess4 = [2,0,0,2,2] ## should be read from the webpage
#guess5 = [2,0,0,2,1] ## should be read from the webpage


#print('testing ' + word1)
result2 = bot.checkWord(word1, guess1, open('list', 'r').readline().split(' '))
print(len(result2))
print(random.choice(result2))
result3 = bot.checkWord(word2, guess2, result2)
print(len(result3))
print(random.choice(result2))
result4 = bot.checkWord(word3, guess3, result3)
print(len(result4))
print(random.choice(result4))
#result5 = checkWord(word4, guess4, result4)
#result6 = checkWord(word5, guess5, result5)

