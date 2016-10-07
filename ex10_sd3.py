# this will print out a mock folder using escape sequences and format
# characters learned so far.

# assign variables strings to use in folder
folder_title = "lpthw-exercises"

folder_type = "folder"
folder_modified = "Today"

folder1 = "google-python-exercises"
folder1_size = "4.1kb"

folder2 = "lpthw-exercises"
folder2_size = "4.1kb"

print "-" * 75
print "|\t\t\t%s - File Manager\t\t\t  |" % folder_title
print "-" * 75
print "| Name\t\t\t  |Size\t  |Type\t   | Date Modified\t\t  |"
print "-" * 75
print "| %s | %s | %s | %s \t\t\t  |" % (
	folder1, folder1_size, folder_type, folder_modified
)
print "| %s \t  | %s | %s | %s \t\t\t  |" % (
	folder2, folder2_size, folder_type, folder_modified
)
print "| \t\t\t\t\t\t\t\t\t  |\n" * 5
print "-" * 75
