__author__ = 'Chris'

def add_move_to_column(board, move, piece):
    '''Given the current board, the column number of the move just made, and the piece to be inserted (O or X), this
    function will add the move to the correct column in the board (updating it) and return the new board.'''
    column = 0
    column += int(move)
    character = piece
    index1 = (board[column]).index(' ')
    board[column][index1] = character
    return board

board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], ['O', ' ', ' ', ' ', ' ', ' ', ' '], ['O', 'X', 'O', ' ', ' ', ' ', ' '], ['O', 'O', 'X', ' ', ' ', ' ', ' '], ['X', ' ', ' ', ' ', ' ', ' ', ' '], ['O', 'X', ' ', ' ', ' ', ' ', ' '], ['O', 'X', ' ', ' ', ' ', ' ', ' '], ['O', 'X', ' ', ' ', ' ', ' ', ' '], ['O', 'X', ' ', ' ', ' ', ' ', ' '], ]

starting_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def print_board (board):
    '''Given the current board, this function will print out the current board along with the numbers denoting the
    columns.'''
    row_0 = ''
    row_1 = ''
    row_2 = ''
    row_3 = ''
    row_4 = ''
    row_5 = ''
    row_6 = ''
    for i in range (0,9):
        row_0 += ' ' + board[i][0]
        row_1 += ' ' + board[i][1]
        row_2 += ' ' + board[i][2]
        row_3 += ' ' + board[i][3]
        row_4 += ' ' + board[i][4]
        row_5 += ' ' + board[i][5]
        row_6 += ' ' + board[i][6]

    print ' 0 1 2 3 4 5 6 7 8'
    print row_6
    print row_5
    print row_4
    print row_3
    print row_2
    print row_1
    print row_0



def play_game(board):
    for e in range (0, 63):
        if e%2 == 0:
            player = 'X'
            column0 = int(raw_input("Player {0}, what is your move (column 0-8)?". format(player)))
            if 0<= column0 <= 8 ==False:  # 1)
                for c in range (0,11):
                    if 0 <= c <= 9:
                        column0 = raw_input('Your input was invalid, please pick a number between 1 and 8.')
                    elif c >= 10:
                        print 'You chose incorrect input 10 times, therefore your turn has been forfeit'
                        player = ' '

            new_board = add_move_to_column(board, column0, player)
            print print_board(new_board)
            check_winner = winner(new_board)
            if check_winner == 1:
                return "Player X has won the game!"
            elif check_winner == 0:
                pass

        else:
            player = 'O'
            column1 = int(raw_input("Player {0}, what is your move (column 0-8)?". format(player)))
            new_board = add_move_to_column(board, column1, player)
            print print_board(new_board)
            check_winner = winner(new_board)
            if check_winner == 1:
                return "Player O has won the game!"
            elif check_winner == 0:
                pass

# 1) Write something here that will make it go to the next player's turn within the for loop in the play_game function. Maybe do something like add +1 to the index that is being loped over (the letter "e" in the case above), so that it moves the prompt to the next person? that might work.

'''this function needs to loop the print board function, the add move to board function, the winner function,
    and the end game function (which i still need to write, uses winner function to determine if there is a winner and
    also checks to see if a draw can be declared.'''


print play_game(starting_board)
