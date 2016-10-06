# assigning var the value 100
cars = 100
# assigning var the value 4
space_in_a_car = 4
# assigning var the value 30
drivers = 30
# assigning var the value 90
passengers = 90
# assigning var the difference of cars and drivers
cars_not_driven = cars - drivers
# assigning var the value of the variable drivers
cars_driven = drivers
# assigning var the product of cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# assigning var the quotient of passengers and cars_driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We an transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drills
# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens
#    if it's just 4?
#	 - For this script it isn't necessary, but for a script that
#	 requires a more accurate product then a floating point is needed.
# 2. Remember thhat 4.0 is a "floating point" number. Find out what that
#    means.
#	 - Floating point number is a number that has no fixed value before
#	 or after the decimal.
# 3. Write comments above each of the variables assignments.
#	 - Comments added.
# 4. Make sure you know what = is called (equals) and that it's making
#    names for things.
#	 - = is equals.
# 5. Remember tat _ is an underscore character.
#	 - Noted.
# 6. Try running Python as a calculator like you did before and use
#    variable names to do your calculations. Popular variable names
#    are also i, x, j.
#	 - >>> i = 1
#	 - >>> x = 2
#	 - >>> print i + x
#	 - 3
#	 - >>>
