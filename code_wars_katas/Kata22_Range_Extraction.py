# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

# Example:

# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20

from functools import reduce

def solution(args) -> None:
    last_inta = None
    def simple_ranges(string : str, inta : int):
        nonlocal last_inta
        if isinstance(string, int):
            if string - inta == -1:
                string = f'{string}-{inta},'
            else:
                string = f'{string},{inta}'
        else:
            if string.endswith(','): # last values were a range
                if last_inta - inta == -1: 
                    to_replace_string = string.split(',')[-2]
                    new_string = to_replace_string.replace(str(last_inta), str(inta))
                    string = string.replace(to_replace_string, new_string)
                else:
                    current_range = string.split(',')[-2]
                    split_up_range = [x if x != '' else '-' for x in current_range.split('-')]
                    check_l = [int(x) for x in current_range.split('-') if x.isnumeric()]
                    if check_l[0] - check_l[1] == 1 or check_l[1] - check_l[0] == 1:
                        split_up_range.insert(len(split_up_range)//2, ',')
                        string = string.replace(current_range, "".join(split_up_range))
                    string += f'{inta}'
            else: # last values weren't a range
                if last_inta - inta == -1:
                    string += f'-{inta},'
                else:
                    string += f',{inta}'
        last_inta = inta
        return string
    res = reduce(simple_ranges, args)
    if res.endswith(','):
        res = res[:-1]
    current_range = res.split(',')[-1]
    split_up_range = [x if x != '' else '-' for x in current_range.split('-')]
    check_l = [int(x) for x in current_range.split('-') if x.isnumeric()]
    if len(check_l) >=2:
        if check_l[0] - check_l[1] == 1 or check_l[1] - check_l[0] == 1:
            split_up_range.insert(len(split_up_range)//2, ',')
            res = res.replace(current_range, "".join(split_up_range))
    return res