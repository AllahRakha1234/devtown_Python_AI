
# CONSTRUCTOR FUNCTION FOR BOARD
def ConstBoard(board):
    print("Current State of the Board: \n\n")
    for i in range(0, 9):
        if (i % 3 == 0 and i > 0):
            print("\n")
        if (board[i] == 0):
            print("_", end="   ")
        elif (board[i] == 1):
            print("O", end="   ")
        elif (board[i] == -1):
            print("X", end="   ")
    print("\n\n")

# ANALYZER FUNCTION FOR BOARD
def analyzeBoard(board):
    cb = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    ]
    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][0]]
    return 0

# USER1 TURN FUNCTION
def User1Turn(board):
    pos = int(input("Enter the X's position from [1,2,3.....9]: "))
    if (board[pos - 1] != 0):
        print("Wrong Move")
        exit(0)
    board[pos - 1] = -1

# USER2 TURN FUNCTION
def User2Turn(board):
    pos = int(input("Enter the O's position from [1,2,3.....9]: "))
    if (board[pos - 1] != 0):
        print("Wrong Move")
        exit(0)
    board[pos - 1] = 1

# MINMAX FUNCTION
def minmax(board, player): # MinMax Algorithm (Player means whose chance to play)
    x = analyzeBoard(board)
    # print(f"Mixmax => x = {x} where player =  {player}")
    if(x != 0):
        return (x * player)   # If X wins, return -1, else return 1 (toggling)
    pos = -1
    value = -2
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = player
            score = -minmax(board, player * -1)
            board[i] = 0
            if (score > value):
                value = score
                pos = i
    # print(f"Mixmax => Score at i = {pos} is {value}")
    if (pos == -1):
        return 0
    return value

# COMPUTER TURN FUNCTION
def CompTurn(board): # Computer's Turn
    pos = -1
    value = -2
    for i in range(0, 9):
        if(board[i] == 0):
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if(score > value):
                # print(f"CompTurn => Score at i = {i} is {score}")
                value = score
                pos = i
    board[pos] = 1

# MAIN FUNCTION
def main():
    choic = int(input("Enter 1 for Single Player, 2 for Multiplayer: "))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (choic == 1):
        print("Computer: O Vs. You: X")
        player = int(input("Enter 1 to play 1(st) or 2 for 2(nd): "))
        for i in range(0, 9):
            if (analyzeBoard(board) != 0):
                break
            if ((i + player) % 2 == 0):
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)
    else:
        for i in range(0, 9):
            if (analyzeBoard(board) != 0):
                break
            if (i % 2 == 0):
                ConstBoard(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)

    x = analyzeBoard(board)
    if (x == 0):
        ConstBoard(board)
        print("Draw!")
    elif (x == 1):
        ConstBoard(board)
        print("Player O Wins !!! X Loses")
    elif (x == -1):
        ConstBoard(board)
        print("Player X Wins !!! O Loses")

# ENTRY POINT
if __name__ == '__main__':
    main()
