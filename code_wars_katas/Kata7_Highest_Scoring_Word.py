# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

# kata link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

# My Solution
import string
def high(x):
    lowered_str = x.lower().split(' ')
    scores_dict= {}
    scores_list = []
    for number_score, letter in enumerate(string.ascii_lowercase, 1):
        scores_dict[letter] = number_score
    for word in lowered_str:
        # suming the word based on its alphabetical position.
        scores_list.append(sum([scores_dict[char] for char in word if char in string.ascii_letters]))
    big_index = scores_list.index(max(scores_list))
    return lowered_str[big_index]

print(high('man i need a taxi up to ubud'))