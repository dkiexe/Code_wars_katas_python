# ALGORITHMS LISTS DYNAMIC PROGRAMMING FUNDAMENTALS
# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
# If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# kata link : https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

# My solution
def max_sequence(arr):
    list_of_subarr = []
    if len(arr) <= 0: return 0
    for substring_len in range(len(arr)+1):
        for index,elem in enumerate(arr):
            list_of_subarr.append(arr[index: index + substring_len])
    return sum(max(list_of_subarr, key=sum))

print(max_sequence())