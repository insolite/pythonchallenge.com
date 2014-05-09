'''Abstract problem class'''
import os


class Problem(object):
    '''Abstract problem'''

    def __init__(self):
        '''Load problem data'''
        module_name = self.__class__.__name__.lower()
        data_file_path = os.path.join('data',
                                      str.format('{0}.txt', module_name))
        if os.path.isfile(data_file_path):
            with open(data_file_path) as data_file:
                self.data = data_file.read()

    def solve(self):
        '''Abstract solve method'''
        raise NotImplementedError
