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