'''problem 0 class'''
from problem import Problem


class Problem0(Problem):
    '''http://www.pythonchallenge.com/pc/def/0.html'''

    def __init__(self):
        '''constructor'''
        Problem.__init__(self)

    def solve(self):
        '''solve problem'''
        return 2 ** 38
