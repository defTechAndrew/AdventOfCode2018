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


def solve_1(data):
    # Build quadrants
    quads = []
    for offset, size in data:
        for w in range(size[0]):
            x = offset[0] + w
            for h in range(size[1]):
                y = offset[1] + h
                quads.append((x, y))
    print(quads[0:30])
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
