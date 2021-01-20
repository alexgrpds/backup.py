# backup.py
A python script for simple folder-based backups 

## Usage 
Program parameters are: 
'backup', 'add', 'rm', 'list', 'clear', 'help'

./backup.py	+ backup: backs up all listed directories
./backup.py	+ add: adds directory to the list
./backup.py	+ rm: removes directory from the list
./backup.py	+ list: lists all directories to be backed up 
./backup.py	+ clear: clears all listed directories

The script makes a "dirs.txt" file in the folder it's run 
from, storing any given directory by the 'add' command. 

It makes a .zip file, named after the time it was created,
containing the folders in the 'dirs.txt' file. 

## Disclaimer 
Use this program at your own risk! It hasn't been tested on a 
variety of hardware and/or operating systems. 

## Licence 
This script comes free of any licence, you can freely modfify 
and use it. Consider leaving a credit if you do! 
