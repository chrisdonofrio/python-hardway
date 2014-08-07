#Add module to script from Python feature set
from sys import argv

#"Unpack argv and assign to variables
script, filename = argv

#Use open function to return file object by assigning to variable txt
txt = open(filename)

#Print statement displaying filename
print "Here's your file %r:" % filename
#Use read function to return string containing all characters in the file
print txt.readlines()

#Print statement asking for user input and assigning that input to new variable
print "Type the filename again:"
file_again = raw_input("> ")

#Use open function to a return file object assigned to new variable txt_again
#This time, the argument assigned to open function is user input
txt_again = open(file_again)

#Once again, use read function to return string containing all characters in the file
print txt_again.readlines()

#Study Drills:
#1. Commenting above each piece of code. Getting the hang of describing what my code actually does.
#2. Get the hang of using Google. For instance, searching "Python [name of function]" will often return 
#valuable information explaining what that function does.
#3. Already have a good idea of what functions or methods do.
#4. Comment out lines 10-15 (or 16-24 in my script) and run script again.
#5. Uncomment lines 10-15 and comment out code NOT related to raw_input.
#6. Found 'read' function in pydoc (entered "python -m pydoc file" in powershell)
#Testing readline() & readlines() functions
#readline(9) printed everything up until the 9th character in the first line of code
#readlines(9) seemed to print the contents of the entire file with \n to signify line breaks
#OK. tried both functions again without number arguments.
#readline() reads only the first line and readlines() reads all lines and splits them by line delimiter
