'''
The adventurer A is  on the space the size of N x N square, this space is divided into 1 x 1 squares.
Traveler A can travel, UP, DOWN, LEFT, RIGHT directions and the start coordinate is always (1, 1).
Traveler A is given a plan to travel with him.
If any movement outside the square space given by traveler is ignored.

The first line is given an N representing the size of the space. ( 1<= N <= 100)
In the second row, traveler A is given a plan to move
For example, "R R R U D D" with a separated alphabets (1 <= travel count<=100)
print out the coordinates (X,Y) of the final destination by separating them into spaces.
'''

n = int(input())
x,y= 1,1
plans = input().split()

#     L R U D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
moveTypes = ['L','R','U','D']

for plan in plans:
    for i in range(len(moveTypes)):
        if plan == moveTypes[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx>n or ny>n:
        continue
    x,y = nx, ny
print(x,y)


