# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
# Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# The following are examples of expected output values:

# My solution
def rgb(r, g, b):
    final_hex_str = ''
    hex_replace = {10 : 'A', 11: 'B', 12: 'C', 13 : 'D' , 14: 'E' , 15 : 'F'}
    for rgb_num in (r, g, b):
        if rgb_num <= 0:
            final_hex_str += '00'
            continue
        if rgb_num >= 255:
            final_hex_str += 'FF'
            continue
        operation1 = int(rgb_num) / 16
        final_hex_str += f'{int(operation1) if int(operation1) not in hex_replace.keys() else hex_replace[int(operation1)]}'
        operation2 = (operation1 - int(operation1)) * 16
        final_hex_str += f'{int(operation2) if int(operation2) not in hex_replace.keys() else hex_replace[int(operation2)]}'
    return final_hex_str