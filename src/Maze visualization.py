import random

# here's like randomized feedback as if it's getting back left/right/straight at diff choices
choices = ["L", "R", "S"]
feedbackList = []

for i in range(49):
    feedback = random.choice(choices)
    feedbackList.append(feedback)

print(feedbackList)

# ideas of what kind of things I'd need to incorporate

# which direction on general board it's currently facing, updates based on turns
currentDirection = "right"

# oh wait each distance would like need a weight each time based on how long it went or smth..
# this is going to be a way oversimplified visualization rn, i will improve it soon

# will start with a set large matrix for now
board = {}
x = "░"

for i in range(30):
    board[i] = [x] * 30

def printboard():
    for row in board:
        temp = ""
        for i in range(30):
            temp = temp + ((board[row][i]) + " ")
        print(temp)

board[15][15] = "▓"

# now like figuring out movement
row = 15
col = 15
for i in range(len(feedbackList)):
    if currentDirection == "right":
        if feedbackList[i] == "S":
            col += 1
            board[row][col] = "▓"
        elif feedbackList[i] == "L":
            row -= 1
            board[row][col] = "▓"
            currentDirection = "up"
        elif feedbackList[i] == "R":
            row += 1
            board[row][col] = "▓"
            currentDirection = "down"

    elif currentDirection == "down":
        if feedbackList[i] == "S":
            row += 1
            board[row][col] = "▓"
        elif feedbackList[i] == "L":
            col += 1
            board[row][col] = "▓"
            currentDirection = "right"
        elif feedbackList[i] == "R":
            col -= 1
            board[row][col] = "▓"
            currentDirection = "left"

    elif currentDirection == "left":
        if feedbackList[i] == "S":
            col -= 1
            board[row][col] = "▓"
        elif feedbackList[i] == "L":
            row += 1
            board[row][col] = "▓"
            currentDirection = "down"
        elif feedbackList[i] == "R":
            row -= 1
            board[row][col] = "▓"
            currentDirection = "up"

    elif currentDirection == "up":
        if feedbackList[i] == "S":
            row -= 1
            board[row][col] = "▓"
        elif feedbackList[i] == "L":
            col -= 1
            board[row][col] = "▓"
            currentDirection = "left"
        elif feedbackList[i] == "R":
            col += 1
            board[row][col] = "▓"
            currentDirection = "right"

printboard()

