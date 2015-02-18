#Sets x equal to string and gives it a number
x = "There are %d types of people." % 10
#Sets binary to binary
binary = "binary"
#Sets do_not to don't
do_not = "don't"
#Sets y to a string, then passes 2 variables.
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluuation ="Isn't that joke so funny? %r"

print joke_evaluuation % hilarious

w = "This is the left side of ..."
e = "a stirng with a right side."

print w + e