#Add module to script from Python feature set
from sys import argv

#"Unpack argv and assign to variables
script, filename = argv

#Use open function to return file object by assigning to variable txt
txt = open(filename)

#Print statement displaying filename
print "Here's your file %r:" % filename
#Use read function to return string containing all characters in the file
print txt.read()

#Print statement asking for user input and assigning that input to new variable
print "Type the filename again:"
file_again = raw_input("> ")

#Use open function to a return file object assigned to new variable txt_again
#This time, the argument assigned to open function is user input
txt_again = open(file_again)

#Once again, use read function to return string containing all characters in the file
print txt_again.read()

#Study Drills:
#1. Commenting above each piece of code. Getting the hang of describing what my code actually does.