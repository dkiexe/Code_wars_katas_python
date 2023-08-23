# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]

def snail(matrix : list):
    top_layer = right_side = bottom = left_side = []
    try:
        top_layer = matrix.pop(0)
        right_side = [l.pop(-1) for l in matrix]
        bottom = matrix.pop(-1)[::-1]
        left_side = [l.pop(0) for l in matrix][::-1]
    except IndexError:
        ...
    finally:
        final_l = [*top_layer, *right_side, *bottom, *left_side]
        if len(matrix) != 0:
            final_l += snail(matrix)
        return final_l


snail_map = [
    ['A1', 'A2', 'A3', 'A4'],
    ['B1', 'B2', 'B3', 'B4'],
    ['C1', 'C2', 'C3', 'C4'],
    ['D1', 'D2', 'D3', 'D4']
]

print(snail(snail_map))