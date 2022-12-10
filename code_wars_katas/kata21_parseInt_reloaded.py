# In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

# Examples:

# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:

# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them

# KATA LINK : https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python

# My solution:
from functools import reduce
def parse_int(string):
    translation_list = []
    string_to_list = string.split(' ')
    text_to_num_dict = {'on': '1', 'tw': '2', 'th': '3', 'fo': '4', 'fi': '5', 'si': '6', 'se': '7', 'ei': '8', 'ni': '9'}
    unique_num_names = {'ten': '10', 'eleven' : '11', 'twelve': '12'}
    zero_adders = {'hundred' : '00', 'thousand' : '000', "million" : "000000"}
    # checkpoint #1 identifing the numbers + zero adders
    for sub_str in string_to_list:
        if sub_str == 'zero' or len(string) == 0:
            return 0
        if '-' in sub_str:
            first_part, second_part = sub_str.split('-')
            translation_list.append(text_to_num_dict[first_part[:2]] + text_to_num_dict[second_part[:2]])
            continue
        if sub_str in unique_num_names.keys():
            translation_list.append(unique_num_names[sub_str])
            continue
        if sub_str[:2] in text_to_num_dict.keys() and sub_str != 'thousand':
            if sub_str.endswith('teen'):
                translation_list.append('1'+text_to_num_dict[sub_str[:2]])
                continue
            if sub_str.endswith('ty'):
                translation_list.append(text_to_num_dict[sub_str[:2]] + '0')
                continue
            translation_list.append(text_to_num_dict[sub_str[:2]])
        if sub_str in zero_adders.keys():
            translation_list.append(zero_adders[sub_str])
    # checkpoint #2 striping the zeros after adding them to numbers
    index_of_last_valid_number = 0
    for index, val in enumerate(translation_list):
        if not val.startswith('0'):
            index_of_last_valid_number = index
            continue
        else:
            translation_list[index_of_last_valid_number] = translation_list[index_of_last_valid_number] + val
    zero_stripped_translation = [val for val in translation_list if val not in zero_adders.values()]
    # checkpoint #3 making sure the list is in decending order
    last_number_in_string = 'this is a test string lul'
    for index, val in enumerate(zero_stripped_translation):
        if len(val) > len(last_number_in_string):
            try:
                zero_stripped_translation[index -1] = zero_stripped_translation[index -1] + '0' * val.count('0') 
                last_number_in_string = zero_stripped_translation[index -1]
            except:
                continue
        else:
            last_number_in_string = val
    final_result = reduce(lambda x,y: int(x) + int(y), zero_stripped_translation)
    return int(final_result)

print(parse_int("two hundred three thousand fifty-two"))