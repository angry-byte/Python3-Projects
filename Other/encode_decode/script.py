import base64


def start():
    print(f'Options: ')
    print(f'1) Decode string')
    print(f'2) Encode string')

    while True:
        user_select = input('Select a number: ')
        if user_select == '1' or user_select == '2':
            return user_select
        print(f'Incorrect option.')


def decode_string(given_string):
    given_string = given_string.encode()
    functions_list = [base64.b16decode, base64.b32decode, base64.b64decode, base64.a85decode]
    options = {0: 'base16', 1: 'base32', 2: 'base64', 3: 'base85'}

    print(f'Decoding...')

    for i, scheme in enumerate((functions_list)):
        try:
            result = scheme(given_string)
            print(f'[+] String decoded. The decoded string is: {result.decode()}')
            print(f'[+] The decoding scheme used was: {options[i]}')
            break
        except:
            continue
    else:
        print(f'[-] Could not decode the string. Doesn\'t look to be base encoded.')


def encode_string(given_string):
    options = {1: base64.b16encode, 2: base64.b32encode, 3: base64.b64encode, 4: base64.a85encode}
    given_string = given_string.encode()

    print(f'Options: ')
    print(f'1) base16')
    print(f'2) base32')
    print(f'3) base64')
    print(f'4) base85')
    user_select = int(input('Select the encoding scheme you want to use: '))
    
    while user_select not in options.keys():
        print(f'Error. Incorrect option.')
        user_select = input('Select the encoding scheme you want to use: ')

    for i, scheme in enumerate((options.values())):
        if (i) == (user_select - 1):
            result = scheme(given_string).decode()
            print(f'[+] String has been encoded. Result: {result}')
            break
        else:
            continue


if __name__ == "__main__":
    selected_option = start()

    if selected_option == '1':
        target_string = input('Enter the string of data you want to decode: ')
        print(f'')
        decode_string(target_string)
    elif selected_option == '2':
        user_string = input('Enter the string of data you want to encode: ')
        print(f'')
        encode_string(user_string)

