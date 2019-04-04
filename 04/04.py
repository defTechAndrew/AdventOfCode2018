import unittest
import datetime


class Day04Test(unittest.TestCase):
    def test_1(self):
        data = parse(open("04.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(0, answer)

    # def test_2(self):
    #     data = parse(open("04.txt"))
    #     answer = solve_2(data)
    #     print('Answer 02', answer)
    #     self.assertEqual(0, answer)


def parse(file):
    lines = file.read().splitlines()
    file.close()
    times = []
    for line in lines:
        date_and_time, event = line.split(']')
        date, hour_minute = date_and_time[1:].split()
        time_args = date.split('-') + hour_minute.split(':')
        time_args = tuple(map(int, time_args))
        dt = DateTime(*time_args, event=event[1:])
        times.append(dt)

    return event_sets(sorted(times))


def event_sets(l):
    guard_event = 0
    for i, time in enumerate(l):
        if time.event.startswith('Guard') and i != guard_event:
            yield l[guard_event:i]
            guard_event = i


def merge_guard_ids(guard_shifts):
    guard_times = dict()
    for event_set in guard_shifts:
        guard_id = event_set[0].event.split()[1][1:]
        if guard_id in guard_times:
            guard_times[guard_id].extend(event_set[1:])
        else:
            guard_times[guard_id] = event_set[1:]
    return guard_times


class DateTime(datetime.datetime):
    def __new__(cls, *args, **kwargs):
        dt = datetime.datetime.__new__(cls, *args)
        dt.event = kwargs['event']
        return dt


def solve_1(data):
    guard_dict = merge_guard_ids(data)
    for key, value in guard_dict.items():
        print(key, value)

    return None


def solve_2(data):
    return None


if __name__ == '__main__':
    unittest.main()
