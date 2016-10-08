from sys import argv

script, user_name, current_date= argv
prompt = 'Response: '

print "\nHi %s. I'm the %s script. Beautiful %s isn't it?" % (
	user_name, script, current_date)
	
print "\nI'd like to ask you a few questions."
print "\nDo you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
So %s, today is %s.
And you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (user_name, current_date,likes, lives, computer)

# Study Drills
# 1. Find out what Zork and Adventure were. Try to find a copy and play.
# 2. Change the prompt variable to some else entirely.
# 	 - Changed prompt to Response: 
# 3. Add another arguement and use it in your script.
#	 - Added arg current_date
# 4. Make sure you understand how I combind a """ style multiline string
#    with the % format activator as the last print
