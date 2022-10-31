import bot
import random
#RATAL DEBUG 20222
#

word1 = 'HASTE' # here may be a bug
word2 = 'DATTO'
#word3 = ''
#word4 = ''
#word5 = ''
#
guess1 = [2,0,2,0,2] ## should be read from the webpage
guess2 = [2,0,2,0,2] ## should be read from the webpage
#guess3 = [2,0,0,2,2] ## should be read from the webpage
#guess4 = [2,0,0,2,2] ## should be read from the webpage
#guess5 = [2,0,0,2,1] ## should be read from the webpage


result2 = bot.checkWord(word1, guess1, open('list', 'r').readline().split(' '))
print(len(result2))
result3 = bot.checkWord(word2, guess2, result2)
print(len(result3))
print(random.choice(result3))
#result4 = checkWord(word3, guess3, result3)
#result5 = checkWord(word4, guess4, result4)
#result6 = checkWord(word5, guess5, result5)

#print(len(result3))
#print(random.choice(result3))