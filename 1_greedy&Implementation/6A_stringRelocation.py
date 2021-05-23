'''
A string consisting only of uppercase alphabetic characters and numbers (0-9) is given.
Print all alphabets are sorted in ascending order, followed by all numbers added.

(e.g., K1KA5CB7 -> ABCKK13 )
'''


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
