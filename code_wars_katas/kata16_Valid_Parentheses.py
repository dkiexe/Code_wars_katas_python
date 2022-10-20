# Write a function that takes a string of parentheses, 
# and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# Examples:
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= input.length <= 100

# Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
# Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).

# My solution:
def valid_parentheses(string):
    if len(string) == 0:
        return True
    bracket_status = {}
    for pos,letter in enumerate(string):
        if letter == '(':
            bracket_status[letter+str(pos)] = False
        if letter == ')':
            did_closed_parentheses = False 
            for key in reversed(bracket_status.keys()):
                if bracket_status[key] == False:
                    bracket_status[key] = True
                    did_closed_parentheses = True
                    break
                else:
                    continue
            if did_closed_parentheses == False:
                return False
    return True if all(bracket_status.values()) and len(bracket_status.values()) != 0 else False

print(valid_parentheses("(dttcv)okzkvci)gj)ua((e))qcip"))