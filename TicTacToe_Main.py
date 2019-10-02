# Define board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

# Define Markers
marker_x = "X"
marker_o = "O"
marker_null = " "


# Draw Board
def draw_board():
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("--+---+--")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("--+---+--")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    return ""
# Place Marker
def place_marker(row, col, input_marker):
    board[row][col] = input_marker

def check_win(marker):
    winner = False

    if board[0][0] == marker and board[0][1] == marker and board[0][2] == marker:
        winner = True
    if board[1][0] == marker and board[1][1] == marker and board[1][2] == marker:
        winner = True
    if board[2][0] == marker and board[2][1] == marker and board[2][2] == marker:
        winner = True
    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        winner = True
    if board[0][2] == marker and board[1][1] == marker and board[2][0] == marker:
        winner = True
    if board[0][0] == marker and board[1][0] == marker and board[2][0] == marker:
        winner = True
    if board[0][1] == marker and board[1][1] == marker and board[2][1] == marker:
        winner = True
    if board[0][2] == marker and board[1][2] == marker and board[2][2] == marker:
        winner = True

    return winner


def tic_tac_toe():
    current_turn = marker_x
    print(draw_board())

    while True:
        print("It is " + current_turn + "'s turn.")

        try:
            player_row = int(input("Enter a row: "))
            player_col = int(input("Enter a col: "))

            if board[player_row][player_col] == marker_null:
                place_marker(player_row, player_col, current_turn)
                print(draw_board())

                if check_win(current_turn):
                    break

                if current_turn == marker_o:
                    current_turn = marker_x
                else:
                    current_turn = marker_o
            else:
                print("Location is occupied. Please enter a different location.")
                print(draw_board())

        except ValueError:
            print("That is not a valid input!")
            print(draw_board())

        except IndexError:
            print("Location out of range!")
            print(draw_board())

    return "Game Over! Player " + current_turn + " wins!"

print(tic_tac_toe())
input("Press any key to continue...")

