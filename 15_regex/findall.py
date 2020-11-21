import re
#findall
phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo1 = phone_number_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)

phone_number_regex_g = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo2 = phone_number_regex_g.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)
