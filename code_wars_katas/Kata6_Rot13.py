# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

# kata link: https://www.codewars.com/kata/530e15517bc88ac656000716

# My solution
import string
def rot13(message):
    final_msg = ''
    # Creating two strings containing all lowercase and uppercase letters
    all_letters_lowercase= string.ascii_lowercase
    all_letters_uppercase= string.ascii_uppercase
    for char in message:
        # Checking if a char is a in lowercase and and if its a alpha character
        if char.islower() and char.isalpha():
            # Adding 13 to the char index
            index = all_letters_lowercase.index(char) + 13
            # Wrapping around the iterable using the % operator
            final_msg += all_letters_lowercase[index % len(all_letters_lowercase)]
        # Checking if a char is a in upper and and if its a alpha character
        elif char.isupper() and char.isalpha():
            # Adding 13 to the char index
            index = all_letters_uppercase.index(char) + 13
            # Wrapping around the iterable using the % operator
            final_msg += all_letters_uppercase[index % len(all_letters_uppercase)]
        # Non alpha chars get added here
        else:
            final_msg += char
    return final_msg