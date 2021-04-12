# # 1. Madlibs

# prompt1 = input('Name: ')
# prompt2 = input('Adjective: ')
# prompt3 = input('Location: ')

# madlib = f'Hi! My name is {prompt1} and I am the {prompt2} kid in town. I usually chill and smoke in the alley behind the {prompt3}.' # changed madlib to variable after reviewing footage

# print(madlib)

# # 2. Guess the Number

# import random

# def guess(x):
#   secret = random.randint(1,x)
#   guess  = 0
#   while (guess != secret):
#     guess = int(input('Guess a number: '))
#     if (guess > secret):
#       print('Lower!')
#     elif (guess < secret):
#       print('Higher!')
#   print('Look at that! Well done.')

# guess(100)

# # 3. Guess the number (computer)

# import random

# def guesser(x):
#   defined_number = int(input('Choose a number: '))
#   guessed_number = 0
#   attempts = 0
#   while(guessed_number != defined_number):
#     guessed_number = random.randint(1,x)
#     attempts += 1
#     print(guessed_number)  
#   print(f'Attempts: {attempts}')
# guesser(10)

# with hints:

import random

defined_number = int(input('Choose a number: '))

