# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

# kata link : https://www.codewars.com/kata/54e6533c92449cc251001667

# My solution
def unique_in_order(iterable):
    """
    This function filters out the repeating characters in a iterable using a for loop.
    
    Returns: list of filtered items from the iterable
    Return-Type: list
    Arguments: A iterable
    """
    final_list = []
    last_item = ''
    for item in iterable:
        if item != last_item:
            final_list.append(item)
            last_item = item
        else:
            continue
    return final_list