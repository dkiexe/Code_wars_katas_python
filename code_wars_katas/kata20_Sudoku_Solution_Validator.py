# Sudoku Background
# Sudoku is a game played on a 9x9 grid. 
# The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row,
#  and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, 
# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, 
# which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

# Examples
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]); // => true
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]); // => false

# kata link: https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python

# My solution
def sequence_check(iterable):
    sorted_iterable = sorted(iterable)
    sequence = [1,2,3,4,5,6,7,8,9]
    return sequence == sorted_iterable

def valid_solution(board):
    row_test = True
    column_test = True
    block_test = True
    # testing rows
    for row in board:
        sequence_check_result = sequence_check(row)
        if sequence_check_result == False:
            row_test = False
            break
    # setup for columns
    column_list = [] #each element represents a column
    for column_index in range(9):
        list_of_rows = [row for row in board]
        one_column = [row[column_index] for row in list_of_rows]
        column_list.append(one_column)
    # column test
    for column in column_list:
        sequence_check_result = sequence_check(column)
        if sequence_check_result == False:
            column_test = False
            break
    # setup for blocks
    block_list_scrabled = [] #each element represents a block row of a block.
    block_list_ordered = [] #all block rows in the right block order
    block_list_final = [] # final block list
    for row in board:
        for number in range(0, len(row)+1, 3):
            if number == 0:
                continue
            block_list_scrabled.append(row[number-3: number])
    # ordering
    for number in range(0,3):
        block_list_ordered.append(block_list_scrabled[number::3])
    # combining
    block_list_ordered = [item for sublist in block_list_ordered for item in sublist] # flatning the list one time
    for number in range(0, len(block_list_ordered), 3):
        block_list_final.append(sum(block_list_ordered[number:number + 3],[])) # this combines all blocks to one
    # block test
    for block in block_list_final:
        sequence_check_result = sequence_check(block)
        if sequence_check_result == False:
            block_test = False
            break
    return all((row_test, column_test, block_test))


valid_solution([                 [5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]])