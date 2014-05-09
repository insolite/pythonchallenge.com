'''unittests'''
import unittest


def get_solution(number):
    '''get solution for certain problem'''
    problem_cls_name = str.format('Problem{0}', number)
    module_name = problem_cls_name.lower()
    problem_cls = __import__(module_name).__dict__[problem_cls_name]
    return problem_cls().solve()


class TestProblemSolutions(unittest.TestCase):
    '''tests for problem solutions'''

    def test_problem0(self):
        '''test problem 0 solution'''
        self.assertEqual(get_solution(0), 274877906944)

    def test_problem1(self):
        '''test problem 1 solution'''
        self.assertEqual(get_solution(1), "i hope you didnt translate it "
                                          "by hand. thats what computers "
                                          "are for. doing it in by hand "
                                          "is inefficient and that's why "
                                          "this text is so long. using "
                                          "string.maketrans() is "
                                          "recommended. now apply on "
                                          "the url.")

    def test_problem2(self):
        '''test problem 2 solution'''
        self.assertEqual(get_solution(2), "equality")

    def test_problem3(self):
        '''test problem 3 solution'''
        self.assertEqual(get_solution(3), "linkedlist")

    def test_problem4(self):
        '''test problem 4 solution'''
        self.assertEqual(get_solution(4), "peak.html")

if __name__ == '__main__':
    unittest.main()
