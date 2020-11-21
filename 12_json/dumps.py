import json

json_data = {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}

s = json.dumps(json_data)
print(s)