from sys import argv

script, filename = argv

#Open file with read privileges
readTarget = open(filename, 'r')

#Read file
print "You wrote..."
print readTarget.read()

#Close file
readTarget.close()
