# How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. 
# Maybe you can decipher it? According to Wikipedia, 
# ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

# Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

# Test examples:
# "EBG13 rknzcyr." --> "ROT13 example."
# "This is my first ROT13 excercise!" --> "Guvf vf zl svefg EBG13 rkprepvfr!"

# kata link: https://www.codewars.com/kata/52223df9e8f98c7aa7000062

# My solution
import string
def rot13(message):
    all_lower = string.ascii_lowercase
    all_upper = string.ascii_uppercase
    positions = [
        all_lower.index(char) +13 if char.islower() and char.isalpha() else all_upper.index(char) + 13 if char.isupper() and char.isalpha() else None for char in message
        ]
    final_msg = "".join([
        all_lower[pos_index % len(all_lower)] if char.isalpha() and char.islower() else all_upper[pos_index % len(all_upper)] if char.isupper() and char.isalpha() else char for pos_index, char in zip(positions, message) 
    ])
    return final_msg

# Note!
# Because i solved this on kata 6 using a for loop i decided to try and solve this using list comprihentions and one line if statements,
# for practice :)