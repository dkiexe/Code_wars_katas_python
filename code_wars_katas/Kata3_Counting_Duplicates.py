# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters 
# and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) 
# and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# kata link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

# My solution
def duplicate_count(text):
    """
    This function countes the dupe characters inside the text(string) argument using 2 lists and a for loop
    at the end it returns an int with the count of the dupe characters in the text(string) argument.
    """
    counted_dupes = 0
    used_chars_list = []
    dupe_chars= []
    for char in text:
        char= char.casefold()
        if char in used_chars_list and char not in dupe_chars:
            dupe_chars.append(char)
            counted_dupes += 1
        else:
            used_chars_list.append(char)
    return counted_dupes

print(duplicate_count('abcdeaa'))