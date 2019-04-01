import unittest


class DayTemplateTest(unittest.TestCase):
    def test_1(self):
        data = parse(open("Template.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(0, answer)

    def test_2(self):
        data = parse(open("Template.txt"))
        answer = solve_2(data)
        print('Answer 02', answer)
        self.assertEqual(0, answer)


def parse(file):
    lines = file.read().splitlines()
    file.close()
    return lines


def solve_1(data):
    return None


def solve_2(data):
    return None


if __name__ == '__main__':
    unittest.main()
