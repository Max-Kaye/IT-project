import datetime

start = datetime.datetime.now()

print "x|y"
print "==="
x = 0
while True:
    x = x + 1
    if x == 3:
        continue
    y = x * x + 3
    table = "{}|{}".format(x, y)
    print table

time_taken = datetime.datetime.now() - start

print("calculated results in:{}".format(time_taken))
