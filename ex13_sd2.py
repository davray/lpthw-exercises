# Exercise 13 - Study Drill 2
# 2. Write a script that has fewer arguments and one that has more.
#
# This script calls 3 arguments for argv to unpack


from sys import argv

script, first_name, last_name = argv

print "\nScript %s opened successfully!\n" % script

print "Welcome %s %s." % (first_name, last_name)
