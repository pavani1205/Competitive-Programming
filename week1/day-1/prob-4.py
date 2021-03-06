import unittest


def merge_ranges(meetings):

    # Merge meeting ranges
    meetings.sort()
    new_list = []
    for i in range(len(meetings)):
        # print(type(list(meetings[i])), "\n")
        meetings[i] = list(meetings[i])
    new_list.append(meetings[0])
    for current in meetings[1:]:
        if current[0]<=new_list[len(new_list)-1][1]:
            new_list[len(new_list)-1][1] = max(current[1],new_list[len(new_list)-1][1])
        else:
            new_list.append(current)
    # print(meetings, "\n")
    for i in range(len(new_list)):
        # print(type(list(meetings[i])), "\n")
        new_list[i] = tuple(new_list[i])
    # print(new_list, "\n")
    return new_list


















# Tests

class Test(unittest.TestCase):

    # def test_meetings_overlap(self):
    #     actual = merge_ranges([(1, 3), (2, 4)])
    #     expected = [(1, 4)]
    #     self.assertEqual(actual, expected)

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 5), (2, 3)])
        expected = [(1, 5)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)