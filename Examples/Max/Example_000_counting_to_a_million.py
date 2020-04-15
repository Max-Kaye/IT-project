
import datetime

start = datetime.datetime.now()
count = 0
# for number in range(1, 100000000000000000001): doesnt work with HUGE numbers
for number in range(1, 1000001):  # counts from one to one less than 1'000'001
    count = count + 1  # this could also be written as just `count++`
    if number % 100000 == 0:  # only print every one hundred thousanth number, that is ten times between one and a mill
        print(number)

timeTaken = datetime.datetime.now() - start
print("counted to {} in {}".format(count, timeTaken))
