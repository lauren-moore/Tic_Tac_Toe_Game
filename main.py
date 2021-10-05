from replit import clear

def make_move(board):
    """Asks a player for a move and adds the move to the board."""

    # asks user for their player #
    player_num = input("What is your player number? 1 or 2: ")
    print()

    # asks user for a row
    select_row = input("Which row? 1 to 3: ")
    select_row = int(select_row)
    print()

    # asks user for a column
    select_column = input("Which column? 1 to 3: ")
    select_column = int(select_column)
    print()

    # check if board at row and column has been taken, else put x or o there depending on player
    if board[select_row - 1][select_column - 1] != "-":
        print("This spot has been taken already")
    else:
        if player_num == "1":
            board[select_row - 1][select_column - 1] = "x"
        elif player_num == "2":
            board[select_row - 1][select_column - 1] = "o"


def print_board(board):
    """Prints board to show the players"""
    for row in board:
        print(row)


def cleared_board():
    board = [["-","-","-"],["-","-","-"],["-","-","-"]]
    return board

def check_win(board):
    """Checks board for a winner and returns winner"""

    # checks rows for win
    # check each item in row
        # if each item is x, player 1 wins
        # else each item is o, player 2 wins
    winner = ""
    for row in board:
        if row == ["x", "x", "x"]:
            winner = "1"
            return winner
        elif row == ["o", "o", "o"]:
            winner = "2"
            return winner


    # if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x":
    #     winner = "1"
    # if board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x":
    #     winner = "1"
    # if board[2][2] == "x" and board[2][1] == "x" and board[2][0] == "x":
    #     winner = "1"
    # if board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o":
    #     winner = "2"
    # if board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o":
    #     winner = "2"
    # if board[2][2] == "o" and board[2][1] == "o" and board[2][0] == "o":
    #     winner = "2"

    # checks columns for win

    if board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":
        winner = "1"
    if board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x":
        winner = "1"
    if board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x":
        winner = "1"
    if board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o":
        winner = "2"
    if board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "o":
        winner = "2"
    if board[0][2] == "o" and board[1][2] == "o" and board[2][22] == "o":
        winner = "2"

    # checks diagonals for win
    if board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
        winner = "1"
    if board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
        winner = "2"
    if board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
        winner = "1"
    if board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o":
        winner = "2"
    
    return winner


def check_tie(board):
    """Checks if board is full and there's a tie"""
    full_board = 0
    for row in board:
        for char in row:
            if char != "-":
                full_board += 1
    if full_board == 9:
        winner = "tie"
        return winner


def play(board):
    """Main REPL function to play the game"""
    
    while True:
        print("Welcome to Tic Tac Toe!")
        print()
        
        while True:
            print_board(board)
            print()
            make_move(board)

            winner = check_win(board)
            tie = check_tie(board) 
            
            if winner == "1" or winner == "2":
                break
            if tie == "tie":
                break
            input("Press return to continue")
            clear()
        if winner == "1":
            print("Player 1 won!")
            print()
        elif winner == "2":
            print("Player 2 won!")
            print()
        elif tie == "tie":
            print("GAME OVER! IT'S A TIEEEEEE!")
            print()
        input("Press RETURN to restart")
        board = cleared_board()
        clear()




#################################################################################
tic_tac_toe_board = [["-","-","-"],["-","-","-"],["-","-","-"]]
play(tic_tac_toe_board)