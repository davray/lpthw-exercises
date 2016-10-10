# import function argv from module sys
from sys import argv
# give argv two variables to unpack
script, input_file = argv
# define function
def print_all(f):
	# print file contents
	print f.read()
# define function
def rewind(f):
	# move to byte 0 in file
	f.seek(0)
# define function with two variables	
def print_a_line(line_count, f):
	# print line position then print line
	print line_count, f.readline(),
# open file from argv var, assign to new var
current_file = open(input_file)
# print string with new line escape sequence
print "First let's print the whole file:\n"
# call function with var current_file
print_all(current_file)
# print string
print "Now let's rewind, kind of like a tape."
# call function with var
rewind(current_file)
# print string
print "Let's print three lines:"
# give var value of 1
current_line = 1 # 1
# call function with variables
print_a_line(current_line, current_file)
# add a value of 1 to current value
current_line += 1 # 2
# call function with variables
print_a_line(current_line, current_file)
# add a value of 1 to current value
current_line += 1 # 3
# call function with variables
print_a_line(current_line, current_file)

# Study Drills
# 1. Go through and write English comments for each line to understand
#    what's going on.
# 2. Each time print_a_line is run, you are passing in a variable 
#    current_line. Write out what current_line is equal to on each 
#    function call, and trace how it becomes line_count in print_line.
# 3. Find each place a function is used, and go check it's def to make
#    sure that you are giving it the right arguments.
# 4. Research online what the seek function for file does. Try	
#    pydoc file and see if you can figure it out from there.
#	 - file.seek moves to new file position.
# 5. Research the shorthand notation += and rewrite the script.
