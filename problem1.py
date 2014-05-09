'''problem 1 class'''
from problem import Problem


def shift_char(char):
    '''shift character to the right by 2'''
    if char.isalpha():
        return chr((ord(char) - Problem1.LETTER_OFFSET + 2) %
                   26 + Problem1.LETTER_OFFSET)
    return char


class Problem1(Problem):
    '''http://www.pythonchallenge.com/pc/def/map.html'''

    LETTER_OFFSET = 97

    def __init__(self):
        '''constructor'''
        Problem.__init__(self)

    def solve(self):
        '''solve problem'''
        return ''.join(map(shift_char, list(self.data)))
