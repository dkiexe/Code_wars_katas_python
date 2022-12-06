# KATA LINK : https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

# A 1x1 matrix |a| has determinant a.

# A 2x2 matrix [ [a, b], [c, d] ] or

# |a  b|
# |c  d|
# has determinant: a*d - b*c.

# The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

# For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

# |a b c|  
# |d e f|  
# |g h i|  
# the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) 
# refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

# |- - -|
# |- e f|
# |- h i|  
# Note the alternation of signs.

# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

# det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)

# My solution:
import os
import numpy
import time

os.system('cls')

start = time.perf_counter()

def determinant(matrix):
    total = 0
    if len(matrix) == 0:
        return 1
    if len(matrix) == 1:
        return matrix[0][0] # single degit matrix would allways return the same digit.
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] # solving a 2x2 matrix.
    for current_index in range(len(matrix[0])):
        remove_horizontal_tuple = list(zip(*matrix[1:]))[current_index] # removing a tuple based off the index.
        new_matrix = list(zip(*[x for x in list(zip(*matrix[1:])) if x != remove_horizontal_tuple])) # creating a new matrix based on the rejected one.
        sign = (-1) ** (current_index % 2) # switching signs based on the (+-+-) format.
        total += matrix[0][current_index] * determinant(new_matrix) * sign # calculating the final result.
    return total

mat = [
[5 ,0 ,5 ,5 ,6 ,1 ,0 ,4 ,4 ,4],
[5 ,8 ,0 ,5 ,7 ,4 ,0 ,1 ,0 ,0],
[4 ,9 ,1 ,2 ,5 ,1 ,0 ,4 ,4 ,0],
[7 ,8 ,5 ,8 ,9 ,1 ,2 ,2 ,0 ,0],
[6 ,2 ,9 ,4 ,9 ,1 ,2 ,3 ,0 ,9],
[9 ,3 ,3 ,8 ,1 ,8 ,4 ,6 ,6 ,9],
[1 ,2 ,7 ,9 ,3 ,8 ,5 ,0 ,4 ,0],
[4 ,8 ,5 ,6 ,7 ,5 ,6 ,0 ,6 ,8],
[1 ,4 ,8 ,0 ,8 ,0 ,7 ,9 ,2 ,2],
[7 ,8 ,3 ,8 ,8 ,6 ,7 ,1 ,7 ,9]
]



print(determinant(mat))
print(numpy.linalg.det(mat))
stop = time.perf_counter()
print(f"time took: {round(stop-start, 2)}")