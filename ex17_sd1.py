# Study Drills
# 1. This script is really annoying. There's no need to ask you before
#    doing the copy, and it prints too much out to the screen. Try to 
#    make the script more friendly to use by removing features.
#
# Description: Modified Exercise 17 script. Removed unnecessary lines
#              of code and cleaned it up. 


from sys import argv

script, from_file, to_file = argv

print "Copied data from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
