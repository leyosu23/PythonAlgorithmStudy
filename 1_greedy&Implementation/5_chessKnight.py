'''
Print out the number of cases in which a night can move
given its position in an 8 x 8 coordinate plane.
Row is expressed from to 1 to 8 from the top, and column is expressed from a to h from the left.
A string consisting of two characters (e.g., a1, c6) is entered.
'''

data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1
cnt = 0
knightSteps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(-1,2),(1,-2),(-1,-2)]

for i in range(len(knightSteps)):
    dx = row + int(knightSteps[i][0])
    dy = column + int(knightSteps[i][1])
    if dx < 1 or dy < 1 or dx > 8 or dy > 8 :
        continue
    cnt += 1

print(cnt)