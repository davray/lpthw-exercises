formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Study Drills
# 1. Do your checks of your work, write down your mistakes, and try not to
#    make them on the next exercise.
#	 - No errors.
# 2. Notice that the last line of output uses both single-quotes and 
#    double-quotes for individual pieces. Why do you think that is?
#	 - The interpeter is being told to print out things at their raw
#	 value. When it read " ' " it might of realized that the we are
#	 using double-quotes.
