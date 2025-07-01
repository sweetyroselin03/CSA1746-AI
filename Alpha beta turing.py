import copy

# Check if a player has won
def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the game is over
def game_over(board):
    return check_winner(board, "X") or check_winner(board, "O") or \
           all(cell != " " for row in board for cell in row)

# Evaluate the board
def evaluate(board):
    if check_winner(board, "X"):
        return 1
    elif check_winner(board, "O"):
        return -1
    else:
        return 0

# Get possible moves
def get_possible_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

# Apply move
def make_move(board, move, player):
    new_board = copy.deepcopy(board)
    new_board[move[0]][move[1]] = player
    return new_board

# Alpha-Beta pruning algorithm
def alpha_beta(board, depth, alpha, beta, player):
    if game_over(board) or depth == 0:
        return evaluate(board), None

    if player == "X":  # Maximizing
        max_score = float('-inf')
        best_move = None
        for move in get_possible_moves(board):
            new_board = make_move(board, move, player)
            score, _ = alpha_beta(new_board, depth - 1, alpha, beta, "O")
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score, best_move
    else:  # Minimizing
        min_score = float('inf')
        best_move = None
        for move in get_possible_moves(board):
            new_board = make_move(board, move, player)
            score, _ = alpha_beta(new_board, depth - 1, alpha, beta, "X")
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score, best_move

# Print board
def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

# Sample board state
board = [
    ["X", "O", "X"],
    [" ", "X", " "],
    ["O", " ", " "]
]

print("Current Board:")
print_board(board)

# Call Alpha-Beta search
score, move = alpha_beta(board, depth=5, alpha=float('-inf'), beta=float('inf'), player="X")

print(f"Best Move for 'X': {move}")
print(f"Score: {score}")

# Show resulting board
if move:
    new_board = make_move(board, move, "X")
    print("Board after move:")
    print_board(new_board)
