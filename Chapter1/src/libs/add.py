'''
    Add numbers in the list
'''

from typing import List

def add_numbers(num: List) -> int:

    '''
        Defines a method to add numbers in the list

        params:
            num: List of only numbers
    '''
    result = sum(num)
    return result
