import datetime
import shutil


if '__main__' == __name__:
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    target_directory = input('Enter the name/full path of the folder to copy and archive: ')

    shutil.make_archive(current_date_time, 'zip', target_directory)

