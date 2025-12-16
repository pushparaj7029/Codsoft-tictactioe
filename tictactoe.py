import math

# -----------------------------
# Save responses to file
# -----------------------------
def save_response(text):
    with open("response.txt", "a") as file:
        file.write(text + "\n")


# -----------------------------
# Print the board
# -----------------------------
def print_board(board):
    for i in range(3):
        print(board[3*i], "|", board[3*i+1], "|", board[3*i+2])
        if i < 2:
            print("---------")
    print()


# -----------------------------
# Check winner
# -----------------------------
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False


# -----------------------------
# Check draw
# -----------------------------
def is_draw(board):
    return " " not in board


# -----------------------------
# Minimax Algorithm
# -----------------------------
def minimax(board, isMaximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if isMaximizing:
        bestScore = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                bestScore = max(score, bestScore)
        return bestScore

    else:
        bestScore = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                bestScore = min(score, bestScore)
        return bestScore


# -----------------------------
# AI Move
# -----------------------------
def ai_move(board):
    bestScore = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > bestScore:
                bestScore = score
                move = i

    board[move] = "O"
    save_response(f"AI played at position {move}")


# -----------------------------
# Main Game Loop
# -----------------------------
def play_game():
    board = [" "] * 9
    print("You are X, AI is O")
    save_response("New Game Started")

    while True:
        print_board(board)

        # Human move
        try:
            move = int(input("Enter your move (0-8): "))
        except:
            print("Invalid input")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move")
            continue

        board[move] = "X"
        save_response(f"Human played at position {move}")

        if check_winner(board, "X"):
            print_board(board)
            print("You win!")
            save_response("Result: Human wins")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            save_response("Result: Draw")
            break

        # AI move
        ai_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            save_response("Result: AI wins")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            save_response("Result: Draw")
            break


# -----------------------------
# Start the game
# -----------------------------
play_game()