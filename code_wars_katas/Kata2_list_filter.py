# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# kata link : https://www.codewars.com/kata/53dbd5315a3c69eed20002dd

# My solution
def filter_list(l):
    """
    This function filters the l(list) argument by using the filter function.
    Inside the filter function we use a lambda function, 
    in lambda function we can see a isinstance() function
    this function recives an element from the l(argument) iterable
    by the filter function and each time tests to see if its a string.
    note that we are using the not operator next to the isinstance() function 
    in order to reverse the result, this makes it so that if the isinstance()
    would find a string it would return a True the not operaor would reverse it to
    False and the filter function wount add it to its final returned iterator object.
    """
    return list(filter(lambda elem: not isinstance(elem, str), l))