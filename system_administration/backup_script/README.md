## Description

This is a Python3 script that copies a directory and then compresses the directory into zip file that is named by the current date on the operating system. The archive is created with the date and time as the name of the file. The file name format is: yyyy-mm-dd HH-MM-SS.zip

IMPORTANT: This script does not encrypt the zip archive using a password. To mitigate this security risk, set restrictive file permissions to prevent others from extracting it.


## How to Use

Execute the script using python. If you want to backup a single folder, use the -b or --backup switch. If you want to backup multiple folders, use the -m or --multiple switch and you will be prompted to enter the locations of all the folders you want to backup. 

If the folder is in the same directory as the script, just enter the folder name. Otherwise, you will need to provide the full path of the folder.


## Tested Platforms:

* Cinnamon Mint 20.3
* Windows 10


## Future Plans and Ideas

- [x] Add switches to be enabled for manual backups
- [ ] Implement zip password protection, preferably with a native library
