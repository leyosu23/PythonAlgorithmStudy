# K1KA5CB7 -> ABCKK13
dataInput = input()
temp = []
sum = 0
result = ''
for data in dataInput:
    # if data is alphabet      x.isalpha() is an alternative
    if int(ord(data)) - int(ord('A')) >= 0:
        temp.append(data)
    else:
        sum += int(data)

temp.sort()

for data in temp:
    result+= data

result += str(sum)
print(result)
