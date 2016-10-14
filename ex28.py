test = "test"
testing = "testing"
Python = "Python"
Zed = "Zed"
cool_guy = "Cool Guy"
chunky = "chunky"
bacon = "bacon"
fun = "Fun"

print "True and True is", True and True
print "False and True is", False and True
print "1 == 1 and 2 == 1 is", 1 == 1 and 2 == 1
print "test == test is", test == test
print "1 == 1 or 2 != 1 is", 1 == 1 or 2 != 1
print "True and 1 == 1 is", True and 1 == 1
print "False and 0 != 0 is ", False and 0 != 0
print "True or 1 == 1 is", True or 1 == 1
print "test == testing is", test == testing
print "1 != 0 and 2 == 1 is", 1 != 0 and 2 == 1
print "test != testing is", test != testing
print "test == 1 is", test == 1	
print "not (True and False) is", not (True and False)
print "not (1 == 1 and 0 != 1) is", not (1 == 1 and 0 != 1)
print "not (10 == 1 or 1000 == 1000) is", not (10 == 1 or 1000 == 1000)
print "not (1 != 10 or 3 == 4) is", not (1 != 10 or 3 == 4)

print "not (testing == testing and Zed == cool_guy) is", not (
testing == testing and Zed == cool_guy)

print "1 == 1 and (not (testing == 1 or 1 == 0)) is", 1 == 1 and (
not (testing == 1 or 1 == 0))

print "chunky == bacon and (not (3 == 4 or 3 == 3)) is", chunky == bacon and(not (3 == 4 or 3 == 3))

print "3 == 3 and (not (testing == testing or Python == Fun)) is", 3 == 3 and (not (testing == testing or Python == Fun))
