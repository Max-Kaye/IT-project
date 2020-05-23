import datetime

start = datetime.datetime.now()

print "x|y"
print "==="

xs = range(1, 1000001)
for x in xs:
    y = x * x + 3
    table = "{}|{}".format(x, y)
    print table

time_taken = datetime.datetime.now() - start

print("calculated results in:{}".format(time_taken))

# fastest time: 3.996 Seconds
