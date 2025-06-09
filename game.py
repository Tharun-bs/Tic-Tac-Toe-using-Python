from random import randrange

# Initialize the board with numbers 1–9
board = [[str(3 * r + c + 1) for c in range(3)] for r in range(3)]

# Computer makes the first move in the center
board[1][1] = 'X'

def display_board(board):
    line = '+-------+-------+-------+'
    for row in board:
        print(line)
        print("|       " * 3 + "|")
        print("|  " + "  |  ".join(row) + "  |")
        print("|       " * 3 + "|")
    print(line)

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if move < 1 or move > 9:
                print("Invalid move. Choose 1-9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ['X', 'O']:
                print("That square is already taken.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Please enter a number.")

def make_list_of_free_fields(board):
    free = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free.append((r, c))
    return free

def victory_for(board, sign):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or \
           all(board[j][i] == sign for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == sign for i in range(3)) or \
       all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    if free:
        r, c = free[randrange(len(free))]
        board[r][c] = 'X'

# Main game loop
while True:
    display_board(board)
    
    if victory_for(board, 'X'):
        print("Computer won!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
    
    enter_move(board)
    display_board(board)
    
    if victory_for(board, 'O'):
        print("You won!")
        break
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
    
    draw_move(board)
