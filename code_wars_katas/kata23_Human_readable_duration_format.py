# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(seconds): # FORMAT: 1 year, 2 days, 3 hours, 4 minutes and 5 seconds
    if seconds == 0:
        return 'now'
    take_first_digit = lambda num: int(str(num).split('.')[0])
    sec_in_a_year = 31536000
    sec_in_a_day = 86400
    sec_in_a_hour = 3600
    sec_in_a_minute = 60
    years = take_first_digit(seconds / sec_in_a_year) if seconds >= sec_in_a_year else 0
    days = take_first_digit((seconds - sec_in_a_year * years) / sec_in_a_day)\
        if seconds >= sec_in_a_day else 0
    hours = take_first_digit((seconds - sec_in_a_year * years - sec_in_a_day * days) / sec_in_a_hour)\
        if seconds >= sec_in_a_hour else 0
    minutes = take_first_digit(
        (seconds - sec_in_a_year * years - sec_in_a_day * days - sec_in_a_hour * hours) / sec_in_a_minute
        ) if seconds >= sec_in_a_minute else 0
    secs = seconds - sec_in_a_year * years - sec_in_a_day * days - sec_in_a_hour * hours - sec_in_a_minute * minutes
    vals_tuple = (years, days, hours, minutes, secs)
    names_tuple = ('year', 'day', 'hour', 'minute', 'second')
    last_val = next(reversed([y for x,y in zip(vals_tuple, names_tuple) if x != 0]))
    final = []
    for val, name in zip(vals_tuple, names_tuple):
        filtered_list = [x for x in final if x != '']
        res = f"{' and' if name == last_val and val != 0 and len(filtered_list) != 0 else ''}"
        res += f"{' ' + (str(val) + ' ' + name) if val >= 1 else ''}{'s' if val >= 2 else ''}"
        final.append(res)
    final = [x for x in final if x != '']
    final = ",".join(final[:-1]).strip(',') + final[-1]
    final = final.replace(' ', '', 1)
    return final