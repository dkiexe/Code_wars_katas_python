def unique_in_order(iterable):
    """
    This function filters out the repeating characters in a iterable using a for loop.
    
    Returns: list of filtered items from the iterable
    Return-Type: list
    Arguments: A iterable
    """
    final_list = []
    last_item = ''
    for item in iterable:
        if item != last_item:
            final_list.append(item)
            last_item = item
        else:
            continue
    return final_list