import re
#文字列の置換
names_regex = re.compile(r'Agent \w+')
print(names_regex.sub('CONSORED','Agent Alice gave the secret document to Agent Bob'))