'''
    Tests for testing add_numbers method
'''
import pytest
from src.libs.add import add_numbers

def test_add_numbers():

    '''
        Test to check the true value
    '''
    nums = [1,2,3]
    assert add_numbers(nums) == 6

def test_add_numbers_str():

    '''
        Test to check error while providing a string value
    '''
    num_str = [1,2,3,'hey']
    
    with pytest.raises(TypeError) as exc:
        add_numbers(num_str)


