import getopt
import sys
import string
import random


def eval(given_password):
    upper_letter = False
    lower_letter = False
    numbers = False
    special = False
    points = 0

    if len(given_password) < 9:
        points -= 1000000000
    elif len(given_password) > 8 and len(given_password) < 15:
        points += 10
    elif len(given_password) > 14 and len(given_password) < 20:
        points += 20
    elif len(given_password) > 30:
            points += 30

    for letter in given_password:
        if letter in string.ascii_uppercase and upper_letter == False:
            points += 10
            upper_letter = True
        elif letter in string.ascii_lowercase and lower_letter == False:
            points += 10
            lower_letter = True
        elif letter in string.digits and numbers == False:
            points += 10
            numbers = True
        elif letter in string.punctuation and special == False:
            points += 20
            special = True

    if points < 40:
        print(f'[-] Your password is weak. Consider changing it.')
    elif points >= 40 and points < 60:
        print(f'[+] Your password isn\'t bad but could use some improvements.')
    elif points >= 60:
        print(f'[+] Your password is very strong and very unlikely to be cracked.')


def gen():
    acceptable_chars = ''
    resulting_password = ''
    pass_length = int(input('How many characters do you want your password to have? '))

    special_condition = input('Can your password include special characters? (y/n) ')

    if special_condition.lower() == 'y':
        acceptable_chars += string.digits + string.ascii_letters + string.punctuation
    else: 
        acceptable_chars += string.digits + string.ascii_letters

    for char in range(0, pass_length):
        resulting_password += random.choice(acceptable_chars)
    
    print(f'')
    print(f'[+] Your generated password is: {resulting_password}')
    print(f'')


if '__main__' == __name__:
    argument_list = sys.argv[1:]
    short_options = 'e:g'
    long_options = ['evaluate=', 'generate']
    arguments, values = getopt.getopt(argument_list, short_options, long_options)

    for given_argument, given_value in arguments:
        if given_argument in ('-e', '--evaluate'):
            eval(given_value)
        elif given_argument in ('-g', '--generate'):
            gen()

