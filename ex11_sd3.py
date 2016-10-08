# Exercise 11, Study Drill 3
# 3. Write another form like this to ask some other questions

print "\nHow old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How many siblings do you have?",
siblings = raw_input()

print "Are you the youngest, middle or oldest child?",
which_child = raw_input()

print "\nSo.. you are %s, about %s tall, you have %s sibling(s) and you are the %s child." % (age, height, siblings, which_child)
