import unittest


class Day02Test(unittest.TestCase):
    def test_1(self):
        data = parse(open("02.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(5952, answer)

    def test_2(self):
        data = parse(open("02.txt"))
        answer = solve_2(data)
        print('Answer 02', answer)
        self.assertEqual(0, answer)


def parse(file):
    lines = file.read().splitlines()
    file.close()
    return lines


def solve_1(data):
    twos = 0
    threes = 0
    for line in data:
        count_dict = {c: line.count(c) for c in set(line)}
        if 3 in count_dict.values():
            threes += 1
        if 2 in count_dict.values():
            twos += 1
    return twos * threes


def solve_2(data):
    return None


if __name__ == '__main__':
    unittest.main()
