import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    if len(string)<=1:
        return set([string])
    last=string[:-1]
    # print("last-",last)
    lastchar=string[-1]
    # print("lastchar--",lastchar)
    permutations=get_permutations(last)
    # print("permutations---",permutations)
    perms=set()
    for i in permutations:
        for j in range(len(last)+1):
            # print(i,"   ",j)
            # print("i[:j]----",i[:j])
            # print("i[j:]-----",i[j:])
            per=i[:j]+lastchar+i[j:]
            perms.add(per)
            # print("perms------",perms)
    return perms


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)