def to_jaden_case(string):
    list_map= list(map(lambda word: word[0].upper()+word[1:], string.split()))
    return " ".join(list_map)

print(to_jaden_case('hello wankers'))