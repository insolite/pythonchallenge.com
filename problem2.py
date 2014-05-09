'''problem 2 class'''
from problem import Problem


class Problem2(Problem):
    '''http://www.pythonchallenge.com/pc/def/ocr.html'''

    def __init__(self):
        '''constructor'''
        Problem.__init__(self)

    def solve(self):
        '''solve problem'''
        chars = [ char for char in set(self.data)
                  if self.data.count(char) == 1 ]
        sorted_chars = sorted(zip([self.data.index(char) for char in chars],
                                  chars))
        return ''.join([char for (index, char) in sorted_chars])
