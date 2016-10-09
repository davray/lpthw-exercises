# Study Drill
# 5. Use only raw_input and try the script that way. Think of why one way
#   of getting the filename would be better than another.

txt = raw_input("Enter file to read: ")
txt_file = open(txt)
# print string with raw format char with var filename
print "\nHere's your file %r:" % txt
# print var txt contents open(file.read)
print txt_file.read()
# print string
# get user input, assign user input to var file_again
file_again = raw_input("Enter file name again: ")
# open var filename, assign content to var txt_again
txt_again = open(file_again)
# print txt_again contents using open(file.read)
print "\n" + txt_again.read()

