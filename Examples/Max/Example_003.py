import datetime

start = datetime.datetime.now()

f = open("calc.results.txt", "a+")


def find_where_to_start():
    try:
        f.seek(-1000, 2)
        s = f.read(1000)
        print s
        i = s.rfind("\n", 0, s.rfind("\n"))
        s = s[i + 1:]
        s = s[0:s.find("|")]
        return int(s)
    except:
        return 0


x = find_where_to_start()

while True:
    x = x + 1
    if x == 3:
        continue
    y = x * x + 3
    table = "{}|{}\n".format(x, y)
    # print table
    f.write(table)
    if x % 1000000 == 0:
        print table

time_taken = datetime.datetime.now() - start

print("calculated results in:{}".format(time_taken))
