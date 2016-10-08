age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
# Study Drills
# 1. In Terminal, where you normally run pythong to run your scripts
#    type pydoc raw_input. Read what it say. If you're on Windows try
#    python -m pydoc raw_input instead.
#    - raw_input reads a string from standard input.
# 2. Get out of pydoc by typing q to quit.
# 3. Look online for what the pydoc command does.
# 	 - pydoc generates python documentation in HTML or text for interactive
# 	 use
# 4. Use pydoc to also read about open, file, os, and sys. It's alright if
#    you do not understand those; just read through and take notes about
#    interesting things.
# 	 - open(name[, mode[, buffering]]) -> file object:
#		Open a file using the file() type, returns a file object. This is
#		the preferred way to open a file.
#	 - file(name[, mode[, buffering]]) -> file object:
#		Open a file. 
#	 - os:
#		Performs OS commands depending on which system you are on like
#		path, current dir, parent dir. Programs using os stand a better
#		chance of being portable between different platforms.
#	 - sys:
#		Module provides access to objects used by the interpreter and
#		objects the interact with the interpreter.
