# Study Drills
# 6. Run pydoc file and scroll down until you see the read() command
#    (method/function). See all the other ones you can use? Skip the
#    ones that have __ (two underscores) in front because those are 
#    junk. Try some of the other commands.

txt = raw_input("Enter file to work with:")
txt_file = open(txt)

print "\nFile contents:"
print txt_file.read()

print "\nNow for some other commands.."

print "\nUsing file.seek() file.readline():"
txt_file.seek(0)
print "\t" + txt_file.readline(7),
txt_file.seek(27)
print txt_file.readline(35)


