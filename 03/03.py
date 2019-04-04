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
        self.assertEqual(412, answer)


def parse(file):
    lines = file.read().splitlines()
    file.close()
    data = []
    for line in lines:
        items = line.split(' ')
        offset = tuple(map(int, items[-2][:-1].split(',')))
        size = tuple(map(int, items[-1].split('x')))
        data.append((int(items[0][1:]), offset, size))
    return data


class Rectangle(object):
    def __init__(self, parameters):
        self.index, offset, size = parameters
        self.top_left = Point(offset[0], offset[1])
        self.bottom_right = Point(offset[0] + size[0], offset[1] + size[1])

    def intersection(self, other):
        return not (self.top_left.x > other.bottom_right.x or
                    self.bottom_right.x < other.top_left.x or
                    self.top_left.y > other.bottom_right.y or
                    self.bottom_right.y < other.top_left.y)

    def __repr__(self):
        return 'Rectangle {0} {1}x{2}'.format(self.index, self.top_left, self.bottom_right)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({0},{1})'.format(self.x, self.y)


def solve_1(data):
    # Build quadrants
    quads = []
    for _, offset, size in data:
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
    swatches = tuple(map(Rectangle, data))
    for swatch in swatches:
        intersections = [swatch.intersection(x) for x in swatches if swatch != x]
        if not any(intersections):
            return swatch.index


if __name__ == '__main__':
    unittest.main()
