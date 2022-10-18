# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# My solution
def domain_name(url):
    # Replacing ('www.') ('https://') or ('http://') with empty string
    url = url.replace('https://','') if 'https://' in url else url.replace('http://','')
    url = url.replace('www.','') if 'www.' in url else url
    domain_final = ''
    # Iterating over chars in url when encountering a dot('.') breaking
    for char in url:
        if char == '.':
            break
        domain_final += char
    # Returning final resault
    return domain_final

print(domain_name("http://github.com/carbonfive/raygun"))