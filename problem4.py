'''problem 4 class'''
from problem import Problem

import re
import http.client


class NothingValueError(Exception):
    '''Something bad happened during the getting nothing value'''
    pass


class Problem4(Problem):
    '''http://www.pythonchallenge.com/pc/def/linkedlist.html'''

    def __init__(self):
        '''constructor'''
        Problem.__init__(self)
        self.connection = None

    def get_next_nothing_value(self, url, previous_value):
        '''get the next "nothing" value via http'''
        self.connection.request("GET", url)
        response = self.connection.getresponse()
        if response.status != 200:
            raise NothingValueError
        response_text = response.read().decode()
        if response_text == 'Yes. Divide by two and keep going.':
            return previous_value / 2
        else:
            try:
                return int(re.findall('[0-9]+', response_text)[-1])
            except IndexError:
                return response_text

    def solve(self):
        '''solve problem'''
        try:
            site_url = 'www.pythonchallenge.com'
            self.connection = http.client.HTTPConnection(site_url)
            nothing_value = 12345 # the last is 66831
            while True:
                url = str.format('/pc/def/linkedlist.php?nothing={0}',
                                 nothing_value)
                nothing_value = self.get_next_nothing_value(url, nothing_value)
                if type(nothing_value) == str:
                    return nothing_value
        finally:
            self.connection.close()
