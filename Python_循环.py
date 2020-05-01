# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:41:15 2018

@author: xujia
"""

#This is a number guessing game.
import random
secretNumber = random.randint(1,20)
print ('我想了一个数，在1到20间。')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('猜猜看？')
    guess = int(input())
    
    if guess < secretNumber:
        print('小了。')
    elif guess > secretNumber:
        print('大了。')
    else:
        break    # This condition is the correct guess!
if guess == secretNumber:
    print('很好! 你用了' + str(guessesTaken) + '次猜中了!')
else:
    print('好吧。不难为你了，其实我想的数是' + str(secretNumber)+ '。')



