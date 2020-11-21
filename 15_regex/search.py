import re
#search
phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo1 = phone_number_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())

phone_number_regex_g = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo2 = phone_number_regex_g.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)
print(mo2.group())
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(3))