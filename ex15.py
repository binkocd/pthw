#Pulles argv from modeule sys
from sys import argv
#agrs
script, filename = argv
#set txt to open a file
txt = open(filename)
#print the file name
print "Here's your file %r: " % filename
#reads then prints the file
print txt.read()
txt.close()

print "Type the filename again:"
#set the file to whatever is input
file_again = raw_input("> ")
#opens the file
txt_again = open(file_again)
#prints the file
print txt_again.read()
txt_again.close()