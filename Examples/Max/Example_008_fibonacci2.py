import unittest


# https://en.wikipedia.org/wiki/Fibonacci_number
def calculatefibonacci(first_number, second_number, size_of_output):
    output = [first_number, second_number]
    while output.__len__() != size_of_output:
        third_number = first_number + second_number
        output.append(third_number)
        first_number = second_number
        second_number = third_number

    return output


answer = calculatefibonacci(2, 3, 5)

if answer.__len__() != 5:
    print "failed"
elif answer != [2, 3, 5, 8, 13]:
    print "failed"
else:
    print "all good!"
