import unittest
import sys

# https://en.wikipedia.org/wiki/Fibonacci_number
def calculatefibonacci(first_number, second_number, size_of_output):
    output = [first_number, second_number]
    while output.__len__() != size_of_output:
        third_number = first_number + second_number
        output.append(third_number)
        first_number = second_number
        second_number = third_number

    return output


input1 = input("enter your first number: ")
input2 = input("enter your second number: ")
input3 = input("enter how many results you want: ")
if input3 <= 2:
    sys.exit("that is unacceptable")

answer = calculatefibonacci(input1, input2, input3)
print answer
if answer.__len__() != input3:
    print "failed"
else:
    print "all good!"
