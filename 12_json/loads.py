import json

s = '{"name":"Zophie","isCat":true,"miceCaught":0,"felineIQ":null}'

json_data = json.loads(s)
print(json_data)