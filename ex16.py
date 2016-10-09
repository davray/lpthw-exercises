# import function argv from module sys
from sys import argv
# give argv two variables to unpack
script, filename = argv
# print string, raw format char, input var filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# use raw_input to catch user response
raw_input(" ")
# print string
print "Opening file..."
# open var filename with write flag, assign data to var target
target = open(filename, 'w')
# print string
print "Truncating file. Au revoir!"
# truncate (clear) var target data
target.truncate()
# print string
print "Please enter up to 3 lines of text."
# get user input
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")
# print string with new line escape sequence
print "\nI'm going to write these to the file."
# write user input data to var target
target.write(line1 + "\n" + line2 + "\n" + line3)
# print string
print "\nClosing file..."
# close data in var target
target.close()

# Study Drills
# 1. If you feel you do not understand this, go back through and use the
#    comment trick to get it squared away in your mind. One simple
#    English comment above each line will help you understand or at
#    least let you know what you need to research more.
#	 - Commented code
# 2. Write a script similar to the last exercise that uses read and 
#    argv to read the file you just created.
#	 - File: ex16_sd2.py, ex16_sd2
# 3. There's too much repition in this file. Use strings, formats, and
#    escapes to print out line1, line2, and line3 with just one
#    target.write() command instead of six.
#	 - Fixed Line 28 to reflect study drill.
# 4. Find out why we had to pass a 'w' as an extra parameter to open.
#    Hint: open tries to be safe by making you explicitly say you want
#    to write a file.
#	 - There are flags you should pass when using the open function.
#	 They tell the interpreter if the file is going to be read,
#	 written to, truncated and/or other things.
# 5. If you open the file with 'w' mode, then do you really need the
#    target.truncate()? Go read docs for Python's open function and see
#    if that's true.
#	 - When you open in write mode (w) the file is already truncated so
#	 target.truncate() isn't needed in this instance.
