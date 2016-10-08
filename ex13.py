from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study Drill
# 1. Try giving fewer than three arguments to your script. See that error?
#    See if you can explain it.
# 	 - python ex13.py this that
#	 - Traceback (most recent call last):
#	 -   File "ex13.py", line 3, in <module>
#	 -     script, first, second, third = argv
#	 - ValueError: need more than 3 values to unpack
#
#	 - In my script ex13.py there is a ValueError in Line 3. I told argv
#	 - that it needs 4 values to unpack the rest of the code.
# 2. Write a script that has fewer arguments and one that has more. Make
#    sure you give the unpacked variables good names.
#	 - File: ex13_sd2.py and e13_sd2_2.py
# 3. Combine raw_input with argv to make a script that gets more
#    input from a user.
#	 - File: ex13_sd3.py
# 4. Remember that modules give you features. Modules. Modules. Remember
#   this because we'll need it later.
