import unittest
import itertools


class Day01Test(unittest.TestCase):
    def test_1(self):
        data = parse(open("01.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(454, answer)

    def test_2(self):
        data = parse(open("01.txt"))
        answer = solve_2(data)
        print('Answer 02', answer)
        self.assertEqual(566, answer)


def parse(file):
    lines = file.read().splitlines()
    file.close()
    lines = map(int, lines)
    return lines


def solve_1(data):
    return sum(data)


def solve_2(data):
    value = 0
    results = {value}
    while True:
        for x in itertools.cycle(data):
            results.add(value)
            value += x
            if value in results:
                return value


if __name__ == '__main__':
    unittest.main()
