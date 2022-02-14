#proměnné
dvojta_cara = "=" * 40
cara = "-" * 40
game_rules = """GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row"""

#game board
ohraniceni = "+---+---+---+"
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# Hra stále běží
game_still_going = True

# Kdo vyhrál
winner = None

# Kdo je na řadě
current_player = "X"

def display_board():
    print(ohraniceni)
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print(ohraniceni)
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print(ohraniceni)
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print(ohraniceni)

def handle_turn(player):
    print(dvojta_cara)
    position = input("Player " + player + " | Please enter your move number: ")
    print(dvojta_cara)

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Input needs to be in range 1-9 | Player " + player + " | Please enter your move number: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("This move is already taken. Go again")

    board[position] = player
    print(dvojta_cara)
    display_board()

def play_game():
    # display board
    display_board()

    # while hra stále běží
    while game_still_going:
        handle_turn(current_player)

        # Hra stále běží
        check_if_game_over()

        #změna hráče
        flip_player()

    # hra skončila
    if winner == "X" or winner == "O":
        print(dvojta_cara)
        print("Congratulations, the player " + winner + " WON!")
        print(dvojta_cara)
    elif winner == None:
        print(dvojta_cara)
        print("It's a tie!")
        print(dvojta_cara)

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    # kontrola řádků pro výhru
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # pokud výhra, ukonči hru
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    # kontrola řádků pro výhru
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # pokud výhra, ukonči hru
    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    # kontrola řádků pro výhru
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # pokud výhra, ukonči hru
    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

print(f"Welcome to Tic Tac Toe\n{dvojta_cara}\n{game_rules}\n{dvojta_cara}\nLet's start the game\n{cara}")

play_game()
