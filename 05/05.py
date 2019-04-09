import re
import unittest


class Day05Test(unittest.TestCase):
    def test_1(self):
        data = parse(open("05.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(13114, answer)

    # def test_2(self):
    #     data = parse(open("05.txt"))
    #     answer = solve_2(data)
    #     print('Answer 02', answer)
    #     self.assertEqual(0, answer)


def parse(file):
    data = file.read()
    file.close()
    return data


def get_collapsible(letter_string):
    double_letter = re.compile(r'(.)\1', re.IGNORECASE)
    case = re.compile(r'[A-Z][a-z]|[a-z][A-Z]')
    letter_iter = double_letter.finditer(letter_string)

    for pair in letter_iter:
        case_search = case.search(pair.group())
        if case_search:
            # print(pair.start(), pair.end())
            return pair

    return None


def solve_1(data):
    while get_collapsible(data):
        index = get_collapsible(data)
        if index:
            data = data[:index.start()] + data[index.end():]

    return len(data)


def solve_2(data):
    return None


if __name__ == '__main__':
    unittest.main()
