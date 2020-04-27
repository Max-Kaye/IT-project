import datetime


def max_range(minimum, maximum):
    maxlist = []
    i = minimum
    while True:
        maxlist.append(i)
        i = i + 1
        if i == maximum:
            break
    return maxlist


start = datetime.datetime.now()

print "x|y"
print "==="
x = max_range(1, 10)
print x
"""
while True:
    x = x + 1
    if x == 3:
        continue
    y = x * x + 3
    table = "{}|{}".format(x, y)
    print table
    if x == 10:
        break

time_taken = datetime.datetime.now() - start

"""
