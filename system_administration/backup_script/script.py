import datetime
import shutil
import getopt
import sys
import os
import string


def help():
    print(f'Project Link: https://github.com/angry-byte/' +
            'Python3-Projects/tree/main/system_administration/backup_script')
    print(f'')
    print(f'Options:                Description:')
    print(f'-b      --backup        select a single folder to backup')
    print(f'-h      --help          print out the help page')
    print(f'-m      --multiple      enable a prompt for backing up multiple folders')

    exit(0)


def backup_function(target_directory):
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    shutil.make_archive(current_date_time, 'zip', target_directory)

    print(f'[!] Name of backup file created: {current_date_time + ".zip"}')


def main(target_folder, multiple_condition):
    first_folder_prompt = True

    if multiple_condition:
        folders = []
        tmp_folder = os.mkdir('tmp_backup_folder')

        while True:
            try: 
                folder_count = int(input('Enter the number of folders you want to backup: '))
                break
            except:
                print(f'Error: you must enter a digital number for the number ' +
                        'of digital folders you want to backup')

        for folder in range(folder_count):
            if first_folder_prompt:
                folder_location = input('Enter the location of the folder to backup: ')
                print(f'')
                folders.append(folder_location)
                first_folder_prompt = False
            else:
                folder_location = input('Enter the location of another folder: ')
                print(f'')
                folders.append(folder_location)
        
        print(f'[!] Copying folders to backup...')
        for folder in folders:
            if folder[0] in string.ascii_uppercase and folder[1] == ':':
                folder = folder[2:]

            try:
                shutil.copytree(folder, 'tmp_backup_folder' + '/' + folder)
            except FileNotFoundError:
                print(f'[-] Error: file {folder} was not found.')
                print(f'[!] Continuing backup process...')
                print(f'')


        print(f'[!] Creating backup...')
        backup_function('tmp_backup_folder')
        shutil.rmtree('tmp_backup_folder')

    else:
        backup_function(target_folder)

    print(f'[+] Backup process complete!')
    exit(0)


if '__main__' == __name__:
    options_list = sys.argv[1:]
    short_options = 'b:hm'
    long_options = ['backup =', 'help', 'multiple']
    options, values = getopt.getopt(options_list, short_options, long_options)

    for given_argument, given_value in options:
        if given_argument in ('-h', '--help'):
            help()
        elif given_argument in ('-b', '--backup'):
            target_folder = given_value
            main(given_value, False)
        elif given_argument in ('-m', '--multiple'):
            main('', True)
    
    print(f'[!] Program exited without doing anything. Did you use a switch?')
