# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

# kata link : https://www.codewars.com/kata/54a91a4883a7de5d7800009c

# My_solution
def increment_string(strng):
    then_number = ''
    if len(strng) > 0:
        for x in strng[::-1]:
            if not x.isnumeric():
                break
            then_number += x
        if then_number == '':
            return strng + '1'
        strng_no_number = strng[::-1].replace(then_number, '', 1)[::-1]
        number_inc = str(int(then_number[::-1])+1)
        return strng_no_number + number_inc.zfill(len(then_number))
    else:
        return '1'