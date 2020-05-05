import unittest


# https://en.wikipedia.org/wiki/Fibonacci_number
def calculatefibonacci(first_number=1, second_number=1, size_of_output=3):
    output = []

    def max_range(minimum, maximum):

    return output


class Test(unittest.TestCase):

    def test(self):
        answer = calculateFibonacci(2, 3, 5)
        self.assertEqual(answer.__len__(), 5)
        self.assertEqual(answer, [2, 3, 5, 8, 11])

        answer = calculateFibonacci(1, 10, 4)
        self.assertEqual(answer.__len__(), 4)
        self.assertEqual(answer, [1, 10, 11, 21])
