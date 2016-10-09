# Exercise 15 - Study Drill 4
# 4. Get rid of the part from lines 10-15 where you use raw_input and
#    try the script then.

# import the function argv from module sys
from sys import argv
# give argv variables to unpack
script, filename = argv
# assign var txt to open var filename
txt = open(filename)
# print string with raw format char with var filename
print "\nHere's your file %r:\n" % filename
# print var txt contents open(file.read)
print txt.read()
# print string
print "Type the filename again:"
# get user input, assign user input to var file_again
#file_again = raw_input("> ")
# open var filename, assign content to var txt_again
txt_again = open(filename)
# print txt_again contents using open(file.read)
print "\n" + txt_again.read()

