import unittest


def sort_scores(unsorted_scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score+1)
    for score in unsorted_scores:
        score_counts[score] += 1
    sorted_scores = []
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]
        for time in range(count):
            sorted_scores.append(score)
    return sorted_scores


















# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)