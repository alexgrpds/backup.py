import os
import sys  
import time 
import zipfile


def main(): 
	# current file directory  
	path = os.getcwd()

	# make a string with the time and date
	# it will be used as a name for the backup file 
	filename = time.strftime("%d-%m-%Y-%H-%M-%S") + ".zip"

	# list of accepted arguments 
	args = ['backup', 'add', 'rm', 'list', 'clear', 'help']

	# print help when the argument is passed 
	help_list = [
		' -> backs up all listed directories',
		' + <directory>: adds directory to the list',
		' + <directory>: removes directory from the list',
		' -> lists all directories to be backed up', 
		' -> clears all listed directories'
	]

	# handle not arguments at all 
	if len(sys.argv) < 2: 
		helper(args, help_list)

	# handle argument that is not in the list and/or no arguments 
	if sys.argv[1] not in args:
		helper(args, help_list) 

	# handle add and rm commands without directory 
	if (sys.argv[1] == 'add') and (len(sys.argv) < 3): 
		print("The 'add' argument must be followed by a directory")
		sys.exit(0)
	elif (sys.argv[1] == 'rm') and (len(sys.argv) < 3): 
		print("The 'rm' argument must be followed by a directory")
		sys.exit(0)

	# open or create the directory list file 
	file = open("dirs", "a+").close()

	if sys.argv[1] == 'list': 
		listdirs()
	if sys.argv[1] == 'add':  
		add(sys.argv[2])
	if sys.argv[1] == 'rm':
		remove(sys.argv[2])
	if sys.argv[1] == 'backup':
		backup(filename)
	if sys.argv[1] == 'help':
		helper(args, help_list)
	if sys.argv[1] == 'clear': 
		clear_file()



# add given directory to the list of directories to be backed up 
def add(d): 

	# first we open the file to get all it's contents in a list 
	list_of_dirs = getfolders()

	# check if the directory is already in the list 
	for line in list_of_dirs: 
		if line.strip("\n") == d:
			print("\nDirectory already exists in the list")
			sys.exit(0) 

	# append given directory to the list 
	if os.path.isdir(d): 
		try: 
			with open("dirs", "a+") as file: 
				file.write(str(d) + '\n')

		except IOError as e: 
			print(e)
			sys.exit(0)
	else: 
		print("\nFolder does not exist or access is forbidden")



# remove given directory from list of directories to back up  
def remove(d): 

	# first the file to get all it's contents in a list 
	list_of_dirs = getfolders()

	# open file to write the contents back, without the line we want to delete 
	try: 
		with open("dirs", "w") as file: 
			for line in list_of_dirs:
				if line.strip("\n") != d: 
					file.write(line)

	except IOError as e: 
		print(e)
		sys.exit(0)



# list currently tracked directories for backup 
def listdirs(): 
	
	# open dirs file and print it's contents 
	try: 
		# check if the file is empty 
		with open("dirs", "r") as file: 
			if file.read() == "": 
				print("\nNo directories to back up")
				sys.exit(0) 
		
		# open the file again to get contents 
		file = open("dirs", "r")

		print("\nList of directories to back up:\n")
		for row in file:
			print(row, end='')

		# close the file 
		file.close()

	except IOError as e: 
		print(e)
		sys.exit(0)



# backup files 
def backup(filename): 

	list_of_dirs = getfolders()

	print("\nFolders to be backed up: \n")
	for d in list_of_dirs: 
		print(d, end='')

	procceed = input("\nWould you like to procceed? <y/n>\n")

	if procceed in ['y', 'Y', 'yes', 'YES']: 
		# make a zipfile handle 
		zipf = zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED)

		for directory in list_of_dirs:	
			if os.path.isdir(directory.strip("\n")):
				# strip the '\n' at the end or else os.walk() doesn't work 	
				for root, dirs, files in os.walk(directory.strip("\n")):
					for file in files: 
						zipf.write(os.path.join(root, file))
			else: 
				print("'{0}' directory does not exist or access is forbidden".format(directory.strip("\n")))
	else: 
		sys.exit(0)



# get the list of folders in dirs file 
def getfolders(): 

	# open file to read contents and then return them as a list 
	try: 
		file = open("dirs", "r")
		list_dirs = file.readlines()
		# and then close it 
		file.close()

	except IOError as e: 
		print(e)
		sys.exit(0)

	return list_dirs



# print help 
def helper(arguments, help_list):

	c = 0 
	print("\nBasic arguments and functionality of 'backup.py': \n")
	# exclude the last item of help list, which is 'help', otherwise it'll get out of bounds 
	for args in arguments[:len(arguments) - 1]: 
		print('backup.py + ' , end='')
		print(args + help_list[c])
		c = c + 1 

	sys.exit(0)



# empty the file by opening it with 'w' access 
def clear_file(): 
	file = open("dirs", "w").close()
	sys.exit(0)



if __name__ == "__main__":
	main()
