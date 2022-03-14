# import paramiko                   # SSH Function not build yet
import ftplib
import threading


def brute_force_ssh():
    print("Nothing here for now...")


def brute_force_ftp(target_host, port, username, password):
    for name in username:
        for passwd in password:
            try:
                server.connect(target_host, port, timeout=5)
                server.login(user, passwd)

                print(f'[+] Valid credentials discovered.')
                print(f'Username: {name}')
                print(f'Password: {passwd}')
            except ftplib.error_perm:
                pass


if __name__ == '__main__':
    usr_name_list = []

    username = input('Enter username: ')
    password = input('Enter the filename containing passowrds: ')
    hostname = input('Enter hostname: ')
    port = input('Enter port number: ')

    usr_name_list += username

    passwd_file = open(password, 'r')
    passwd_list = passwd_file.read().splitlines()
    passwd_file.close()

    brute_force_ftp(hostname, port, usr_name_list, passwd_list)

