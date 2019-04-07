import datetime
import re
import unittest


class Day04Test(unittest.TestCase):
    def test_1(self):
        data = parse(open("04.txt"))
        answer = solve_1(data)
        print('Answer 01', answer)
        self.assertEqual(109659, answer)

    def test_2(self):
        data = parse(open("04.txt"))
        answer = solve_2(data)
        print('Answer 02', answer)
        self.assertEqual(36371, answer)


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
    """
    Generator to build guard shifts.
    """
    guard_event = 0
    for i, time in enumerate(l):
        if time.event.startswith('Guard') and i != guard_event:
            yield l[guard_event:i]
            guard_event = i


def merge_guard_ids(guard_shifts):
    """
    Merge event_sets into dictionary keyed by guard IDs.
    """
    guard_times = dict()
    for event_set in guard_shifts:
        guard_id = int(re.search(r'\d+', event_set[0].event).group(0))
        if guard_id in guard_times:
            guard_times[guard_id].extend(pair(event_set[1:]))
        else:
            guard_times[guard_id] = pair(event_set[1:])
    return guard_times


def pair(times):
    """
    Turns sequential list into pairs of start and stop.
    """
    time_iter = iter(times)
    return list(zip(time_iter, time_iter))


class DateTime(datetime.datetime):
    def __new__(cls, *args, **kwargs):
        dt = datetime.datetime.__new__(cls, *args)
        dt.event = kwargs['event']
        return dt


def total_minutes_slept(time_ranges):
    """
    Find total minutes slept in all time ranges.
    """
    result = 0
    for start, end in time_ranges:
        result += end.minute - start.minute
    return result


def most_overlap(time_ranges):
    """
    Find instances of range overlaps and the minute it happens on.
    """
    minutes = 60
    overlap = [0] * minutes
    for minute in range(minutes):
        for start, end in time_ranges:
            if all([minute >= start.minute, minute < end.minute]):
                overlap[minute] += 1

    max_value = max(overlap)
    return max_value, overlap.index(max_value)


def solve_1(data):
    guard_dict = merge_guard_ids(data)
    max_slept = 0
    sleepiest_guard = None

    for guard, time_ranges in guard_dict.items():
        total = total_minutes_slept(time_ranges)
        if total > max_slept:
            max_slept = total
            sleepiest_guard = guard

    _, overlap_minute = most_overlap(guard_dict[sleepiest_guard])
    return sleepiest_guard * overlap_minute


def solve_2(data):
    guard_dict = merge_guard_ids(data)
    most_overlap_times = 0
    sleepiest_guard = None

    for guard, time_ranges in guard_dict.items():
        overlap, overlap_min = most_overlap(time_ranges)
        if overlap > most_overlap_times:
            most_overlap_times = overlap
            sleepiest_guard = (guard, overlap_min)

    return sleepiest_guard[0] * sleepiest_guard[1]


if __name__ == '__main__':
    unittest.main()
