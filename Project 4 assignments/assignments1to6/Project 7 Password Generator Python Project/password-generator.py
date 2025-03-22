
import random

print('Welcome! Let’s generate your password.')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890)*(&^%$#@!)'

number = input('Amount of passwords to generate: ')
number = int(number)

length = input('Your password length: ')
length = int(length)

print('\nHere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):  
        passwords += random.choice(chars)
    print(passwords) 
