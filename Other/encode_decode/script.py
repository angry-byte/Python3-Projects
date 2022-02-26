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
    decode_condition = False
    given_string = given_string.encode()
    options = {'1': 'base16', '2': 'base32', '3': 'base64', '4': 'base85'}

    print(f'Decoding...')
    while True:
        try:
            result = base64.b16decode(given_string)
            scheme_used = '1'
            decode_condition = True
            break
        except:
            decode_condition = False
        try:
            result = base64.b32decode(given_string)
            scheme_used = '2'
            decode_condition = True
            break
        except:
           decode_condition = False
        try:
            result = base64.b64decode(given_string)
            scheme_used = '3'
            decode_condition = True
            break
        except:
            decode_condition = False
        try:
            result = base64.a85decode(given_string)
            scheme_used = '4'
            decode_condition = True
            break
        except:
            decode_condition = False
            break

    if decode_condition:
        for i in options:
            if i == scheme_used:
                print(f'[+] The encoding scheme used on the string was: {options[i]}')
        result = result.decode()
        print(f'The result of the string decoded is: {result}')
    else:
        print(f'[-] Couldn\'t decode string. Doesn\'t look to be base encoded.')


def encode_string(given_string):
    options = ['1', '2', '3', '4']
    given_string = given_string.encode()

    print(f'Options: ')
    print(f'1) base16')
    print(f'2) base32')
    print(f'3) base64')
    print(f'4) base85')
    user_select = input('Select the encoding scheme you want to use: ')
    
    while user_select not in options:
        print(f'Error. Incorrect option.')
        user_select = input('Select the encoding scheme you want to use: ')

    if user_select == '1':
        converted_string = base64.b16encode(given_string)
    elif user_select == '2':
        converted_string = base64.b32encode(given_string)
    elif user_select == '3':
        converted_string = base64.b64encode(given_string)
    elif user_select == '4':
        converted_string = base64.a85encode(given_string)
        

    resulting_string = converted_string.decode()

    print(f'')
    print(f'[+] String has been encoded. Result: {resulting_string}')


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
