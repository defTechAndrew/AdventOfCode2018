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
        data.append((items[0][1:], offset, size))
    return data


class Rectangle(object):
    def __init__(self, parameters):
        self.index, offset, size = parameters
        self.top_left = Point(offset[0] + 1, offset[1] + 1)
        self.bottom_right = Point(self.top_left[0] + size[0], self.top_left[1] + size[1])

    def intersection(self, other):
        if self.top_left >= other.top_left:
            if self.top_left <= other.bottom_right:
                return True
        if self.bottom_right <= other.bottom_right:
            if self.bottom_right >= other.top_left:
                return True
        return False

    def __repr__(self):
        return 'Rectangle {0} {1}x{2}'.format(self.index, self.top_left, self.bottom_right)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return True if self.x == other.y and self.y == other.y else False

    def __gt__(self, other):
        return True if self.x > other.x and self.y > other.y else False

    def __ge__(self, other):
        return True if self.x >= other.x and self.y >= other.y else False

    def __lt__(self, other):
        return True if self.x < other.x and self.y < other.y else False

    def __le__(self, other):
        return True if self.x <= other.x and self.y <= other.y else False

    def __getitem__(self, item):
        return self.y if item else self.x

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
        intersections = [swatch.intersection(x) for x in swatches]
        if not all(intersections):
            return swatch
    return None


if __name__ == '__main__':
    unittest.main()
