#Add module to script from Python feature set
from sys import argv

#Unpack argv and assign to variables
script, filename = argv

#Print statements
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Asking for user input
raw_input ("?")

print "Opening the file..."
#Opens file, with a 'w' parameter I'm not familiar with yet
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#Truncates the file
target.truncate()

print "Now I'm going to ask you for three lines."

#Asking for user input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#Uses write function to write user input received in variables line1, line2, and line3
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#Use write function to write user input received in variables line1, line2, 
#and line3 but use one command instead of six
target.write('%r\n%r\n%r\n' % (line1, line2, line3))

#Close the file
print "And finally, we close it."
target.close()

### STUDY DRILL NOTES ###
#4: 'w' parameter is passed to specifically write to a file. 'r' is passed for reading. 'a' is for append.
#5: after reading the Python documentation on the open function,
#using 'w+' as the mode will truncate the file, 
#therefore target.truncate() is not needed.