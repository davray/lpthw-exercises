# Exercise 13 - Study Drill 3
# 2. Write a script that has fewer arguments and one that has more.
#
# This script calls 6 arguments for argv to unpack and also prompts a 
# user for some information.


from sys import argv

script, first_name, last_name, user_age, user_height, user_weight = argv

print "\nScript %s opened successfully!\n" % script

print "Welcome %s %s.\n" % (first_name, last_name)

print "Going by the information you entered:"
print "\tAge: %s" % user_age
print "\tHeight: %s feet tall" % user_height
print "\tWeight: %s" % user_weight

print "\nI'd have to say, you seem like a healthy chap!"

user_answer = raw_input("\nDo you think you're healthy? ")

