# Simple Tic-Tac-Toe 

board = [' ']*9

def print_board():
    print()
    print(f" {board[0]}  | {board[1]}  | {board[2]} ")
    print("----+----+----")
    print(f" {board[3]}  | {board[4]}  | {board[5]} ")
    print("----+----+----")
    print(f" {board[6]}  | {board[7]}  | {board[8]} ")
    print()

def winner(b, p):
    win = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(b[i]==p for i in line) for line in win)

def minimax(b, player):
    if winner(b, 'O'): return 1
    if winner(b, 'X'): return -1
    if ' ' not in b: return 0
    moves = []
    for i in range(9):
        if b[i] == ' ':
            b[i] = player
            score = minimax(b, 'O' if player == 'X' else 'X')
            moves.append(score)
            b[i] = ' '
    return max(moves) if player == 'O' else min(moves)

def ai_move():
    best = -2
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 'X')
            board[i] = ' '
            if score > best:
                best = score
                move = i
    return move

print("Tic-Tac-Toe (you='X', AI='O')")
while True:
    print_board()
    pos = int(input("Choose your move (1-9): ")) - 1
    if board[pos] != ' ':
        print("Invalid.")
        continue
    board[pos] = 'X'
    if winner(board, 'X'):
        print_board()
        print("You win!")
        break
    if ' ' not in board:
        print_board()
        print("Draw!")
        break
    move = ai_move()
    board[move] = 'O'
    if winner(board, 'O'):
        print_board()
        print("AI wins!")
        break
    if ' ' not in board:
        print_board()
        print("Draw!")
        break