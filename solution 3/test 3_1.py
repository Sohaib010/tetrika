def to_intervals(lst):
    s=[(lst[i], lst[i+1]) for i in range(0, len(lst), 2)]

    return s
def clip_intervals(intervals, lesson):
    clipped = []
    for start, end in intervals:
        if end <= lesson[0] or start >= lesson[1]:
            continue
        clipped.append((max(start, lesson[0]), min(end, lesson[1])))
    return clipped

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    return merged

def intersect_intervals(pupil, tutor):
    result = []
    i = j = 0
    while i < len(pupil) and j < len(tutor):
        a_start, a_end = pupil[i]
        b_start, b_end = tutor[j]
        start = max(a_start, b_start)
        end = min(a_end, b_end)
        if start < end:
            result.append((start, end))
        if a_end < b_end:
            i += 1
        else:
            j += 1
    return result

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson = intervals['lesson']
    pupil_intervals = to_intervals(intervals['pupil'])
    tutor_intervals = to_intervals(intervals['tutor'])

    pupil_clipped = clip_intervals(pupil_intervals, lesson)
    tutor_clipped = clip_intervals(tutor_intervals, lesson)

    pupil_merged = merge_intervals(pupil_clipped)
    tutor_merged = merge_intervals(tutor_clipped)

    intersected = intersect_intervals(pupil_merged, tutor_merged)
    return sum(end - start for start, end in intersected)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

