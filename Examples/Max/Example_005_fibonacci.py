import unittest


# https://en.wikipedia.org/wiki/Fibonacci_number
def calculatefibonacci(first_number, second_number, size_of_output):
    output = []
    output.append(first_number)
    output.append(second_number)
    for x in range(2, size_of_output):
        temp1 = output[output.__len__()-2]
        temp2 = output[output.__len__() - 1]
        output.append(temp1 + temp2)

    return output


class Test(unittest.TestCase):

    def test(self):
        answer = calculatefibonacci(2, 3, 5)
        self.assertEqual(answer.__len__(), 5)
        self.assertEqual(answer, [2, 3, 5, 8, 13])

        answer = calculatefibonacci(1, 10, 4)
        self.assertEqual(answer.__len__(), 4)
        self.assertEqual(answer, [1, 10, 11, 21])
