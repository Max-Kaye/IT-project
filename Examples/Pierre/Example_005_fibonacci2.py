import unittest
import sys
from termcolor import colored, cprint


# https://en.wikipedia.org/wiki/Fibonacci_number
def calculatefibonacci(first_number, second_number, size_of_output):
    output = [first_number, second_number]
    while output.__len__() != size_of_output:
        third_number = first_number + second_number
        output.append(third_number)
        first_number = second_number
        second_number = third_number
        cprint(str(third_number), "green")
    return output


input1 = eval(input("Enter your first number: "))
input2 = eval(input("Enter your second number: "))
input3 = eval(input("How many results would you like: "))
if int(input3) <= 2:
    sys.exit("You need a minimum of 3 results")
answer = calculatefibonacci(input1, input2, input3)
if answer.__len__() != input3:
    print("failed")
else:
    print("Calculation has Finished")
