#Prompt the user for the name of the directory in which they want to save a file. - 15%
#Prompt the user for the name of the file they want to save to the directory in requirement 1. - 15%
#If the directory from requirement 1 doesn't exist the program must create the specified directory. - 20%
#The program will prompt the user for their name, address, and phone number and write that data as a line of comma separated values to the file using the directory and filename from requirements 1 and 2. (example: John Smith, 123 Main St,402-555-1212) - 20%
#After the data has been written to the file your program must open the file, read the contents, and display the contents to the user as program output. - 20%
#Create a GitHub Respository for Assignment 10.1 - 5%
#Submit a link to the respository from requirement 6 as your assignment submission. - 5%

import os

#Getting the files from the OS

def main():

	directory = input("Which directory would you like to save the file to?: ")

	filename = input("Enter the name of the file: ")

	name = input("Please enter your name: ")

	address = input("Enter your address here: ")

	phone_number = input("Please enter your phone number: ")

	#checking if the directory exists

	if os.path.isdir(directory):

		#Creating the file to write to write to and opening it.

		writeFile = open(os.path.join(directory,filename),'w') #writing the data by comma seperated writeFile.write(name+','+address+','+phone_number+'\n')

		#Now we close the file once finished.

		writeFile.close()

		print("Here are the file contents: \n----------------------")

		#Now we will proofread the file before storing it.

		readFile = open(os.path.join(directory,filename),'r')

		for line in readFile:

			print(line)

		readFile.close()

	else:

		print("Please try again. That file does not exist.")

main()