#文字の出現回数を数える
message = 'Those using ReportLab PLUS benefit from developer support hours built in as standard'
count = {}
for character in message:
    count.setdefault(character,0)
    count[character] += 1
    print(count)
print(count)