'''problem 3 class'''
from problem import Problem

import re


class Problem3(Problem):
    '''http://www.pythonchallenge.com/pc/def/equality.html'''

    def __init__(self):
        '''constructor'''
        Problem.__init__(self)

    def solve(self):
        '''solve problem'''
        return ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',
                                  self.data))
