"""
Will provide the low-level version in some cases
"""

import itertools
from collections import Counter

def iter_to_dict_frequency(iterable):
    """ 
    creates a dictionary form a list and the values 
    are the counts of each unique item
    """
    dict_frequency = {}
    for item in iterable:
        dict_frequency.setdefault(item, 0)
        dict_frequency[item]+=1

    return dict_frequency

check_iter_strings = lambda iterable: all([isinstance(i, str) for i in iterable])

check_iter_bools = lambda iterable: all([isinstance(i, bool) for i in iterable])

def check_iters_equal_on_indices(iter1, iter2, iter_indices):
    """
    Checks if any list's items are not equal with respect to given indices.
    """
    return all([iter1[index] == iter2[index] for index in iter_indices])

def iter_to_list_unique_pairs(iterable):
    """
    returns list of two-cycles

    list_pairs = []
    for i in range(len(iterable)):
        #upper triangular
        for j in range(i+1, len(iterable)): #avoids diagonal
            list_pairs.append((iterable[i],iterable[j]))
    return list_pairs

    """
    return list(itertools.combinations(iterable,2))

# set of elements which are in A or in B or in both
iter_union = lambda iter1, iter2: list(set(itertools.chain(iter1, iter2)))


def iter_remove_item(item, iterable):
    """ I think == should be != """
    unequal = lambda x, item: x == item
    return filter(unequal, iterable)

def iter_remove_items(iterable, iter_remove):
    """
    left_bool = any(x in filter_list for x in filtered_list)
    right_bool = any(x in filtered_list for x in filter_list)
    if left_bool or right_bool:
        return [x for x in filtered_list if x not in filter_list]
    return filtered_list
    """
    return [*itertools.filterfalse(lambda i: i in iter_remove, iterable)]

