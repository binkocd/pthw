i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

<<<<<<< HEAD
=======
print "Study Drill 1"

def while_loop(limit):
  i = 0
  while i < 6:
    print "At the top i is %d" % i 
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

limit = 4
while_loop(limit)
>>>>>>> 37e8f9135cecd9a0ebf69c814f229bb70465ee5f
