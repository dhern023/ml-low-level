import itertools
from collections import Counter

def list_to_frequency_dict(_list):
    """ 
    creates a dictionary form a list and the values 
    are the counts of each unique item
    """
    frequency_dictionary = {}
    for i in _list:
        if i in frequency_dictionary:
            frequency_dictionary[i]+=1
        else:
            frequency_dictionary[i] = 1
    return frequency_dictionary