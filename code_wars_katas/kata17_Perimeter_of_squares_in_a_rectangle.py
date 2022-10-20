# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. 
# It's easy to see that the sum of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 

# Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed in 
# the same manner as in the drawing:

# image link : http://i.imgur.com/EYcuB1wm.jpg

# alternative text

# Hint:
# See Fibonacci sequence

# Ref:
# http://oeis.org/A000045

# The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n) and 
# returns the total perimeter of all the squares.

# perimeter(5)  should return 80
# perimeter(7)  should return 216

# kata link: https://www.codewars.com/kata/559a28007caad2ac4e000083/solutions/python

# My solution.
def perimeter(n):
    seq = [1, 1, 2, 3, 5, 8]
    final_seq = seq
    while True:
        if len(final_seq) >= n+1:
            break
        final_seq.append(final_seq[len(final_seq)-1] + final_seq[len(final_seq)-2])
    return sum(final_seq)*4