import hashlib
import sys
import getopt


def help():
    print(f'Hash Cracker using Python3')
    print(f'Project link: ')
    print(f'')
    print(f'Options:')
    print(f'-a [algorithm]              select algorithm')
    print(f'-h [hash]                   given hash to crack')
    print(f'-w [wordlist]               wordlist to use')
    print(f'')
    print(f'The hashing algorithms that can be selected are: md5, sha1, sha256, and sha512')


def main(hash_algorithm, given_hash, given_wordlist):
    print(f'[!] Algorithm chosen: {hash_algorithm}')
    print(f'[!] Given hash: {given_hash}')
    print(f'')

    for word in given_wordlist:
        word_process = hashlib.new(hash_algorithm)
        word_process.update(word.encode())

        if word_process.hexdigest().upper() == given_hash:
            print(f'[+] The hash has been cracked and found to be: {word}')
            break
        elif word_process.hexdigest().lower() == given_hash:
            print(f'[+] The hash has been cracked and found to be: {word}')
            break
        else:
            continue
    else:
        print(f'[-] The hash could not be cracked.')


if '__main__' == __name__:
    alg_choices = ['md5', 'sha1', 'sha256', 'sha512']
    algorithm = ''
    target_hash = ''
    wordlist_name = ''
    argument_list = sys.argv[1:]
    options = 'a:h:w:'
    arguments, values = getopt.getopt(argument_list, options, [])

    for given_argument, given_value in arguments:
        if given_argument in ('-a', ''):
            algorithm = given_value
        elif given_argument in ('-h', ''):
            target_hash = given_value
        elif given_argument in ('-w', ''):
            wordlist_name = given_value

    if algorithm.lower() not in alg_choices:
        help()
        exit(0)

    wordlist_file = open(wordlist_name, 'r')
    wordlist = wordlist_file.read().splitlines()
    wordlist_file.close()

    main(algorithm.lower(), target_hash, wordlist)

