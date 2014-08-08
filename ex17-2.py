from sys import argv
from os.path import exists

script, from_file, to_file = argv

with open(from_file, 'r') as inFile, open(to_file, 'w') as outFile:
	indata = inFile.read()
	outFile.write(indata)