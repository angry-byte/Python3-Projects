## Description

This is a Python3 script that copies a directory and then compresses the directory into zip file that is named by the current date on the operating system. The script can be modified to prompt for a password that would protect the zip file.

The archive is created with the date and time as the name of the file. The format is: yyyy-mm-dd HH-MM-SS

IMPORTANT: This script does not encrypt the zip archive using a password. To mitigate this security risk, set restrictive file permissions to prevent others from extracting it.

## Tested Platforms:

* Cinnamon Mint 20.3
* Windows 10

## Future Plans and Ideas

- [ ] Add switches to be enabled for manual backups
- [ ] Add password implementation, preferably with a native library
