import zipfile
import getopt
import sys


def main(zip_file, wordlist_file):
    password_wordlist = []
    zip_object = zipfile.ZipFile(zip_file)
    
    wordlist_file = open(wordlist, 'r')
    for password in wordlist_file.read().splitlines():
        password_wordlist.append(password)
    wordlist_file.close()

    for password in password_wordlist:
        try:
            zip_object.extractall(pwd=password.encode())
            print(f'[+] Zipfile has been cracked. The password is: {password}')
            break
        except RuntimeError:
            continue
    else:
        print(f'[-] Zipfile could not be cracked.')


if '__main__' == __name__:
    given_zip, wordlist = '',''
    arguments_list = sys.argv[1:]
    short_options = 't:w:'
    arguments, values = getopt.getopt(arguments_list, short_options, [])

    for given_argument, given_value in arguments:
        if given_argument in ('-t', ''):
            given_zip = given_value
        elif given_argument in ('-w', ''):
            wordlist = given_value

    main(given_zip, wordlist)

