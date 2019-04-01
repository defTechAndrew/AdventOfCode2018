import unittest


class Day03Test(unittest.TestCase):
    def test_1(self):
        data = parse(open("03.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(118223, answer)

    def test_2(self):
        data = parse(open("03.txt"))
        answer = solve_2(data)
        print('Answer 02', answer)
        self.assertEqual(0, answer)


def parse(file):
    lines = file.read().splitlines()
    file.close()
    data = []
    for line in lines:
        items = line.split(' ')
        offset = tuple(map(int, items[-2][:-1].split(',')))
        size = tuple(map(int, items[-1].split('x')))
        data.append((offset, size))
    return data


class Rectangle(object):
    def __init__(self, offset, size):
        self.top_left = (offset[0] + 1, offset[1] +1)
        self.bottom_right = (self.top_left[0] + size[0], self.top_left[1] + size[1])

    def intersection(self, other):
        pass


def solve_1(data):
    # Build quadrants
    quads = []
    for offset, size in data:
        for w in range(size[0]):
            x = offset[0] + w
            for h in range(size[1]):
                y = offset[1] + h
                quads.append((x, y))

    # Check for overlap
    seen = set()
    duplicates = set()
    for quad in quads:
        if quad not in seen:
            seen.add(quad)
        else:
            duplicates.add(quad)

    return len(duplicates)


def solve_2(data):
    return None


if __name__ == '__main__':
    unittest.main()
