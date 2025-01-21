__author__ = 'Chris'

# Christopher Powell

# cspowell@ucsc.edu

# Assignment 05: Connect 5

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
    row_list = [row_0, row_1, row_2, row_3, row_4, row_5, row_6]
    print ' 0 1 2 3 4 5 6 7 8'
    print row_list[6]
    print row_list[5]
    print row_list[4]
    print row_list[3]
    print row_list[2]
    print row_list[1]
    print row_list[0]


def add_move_to_column(board, move, piece):
    '''Given the current board, the column number of the move just made, and the piece to be inserted (O or X), this
    function will add the move to the correct column in the board (updating it) and return the new board.'''
    column = 0
    column += int(move)
    character = piece
    index1 = (board[column]).index(' ')
    board[column][index1] = character
    return board


def check_winner_vertical (board):
    '''Given the current board, this function will check all columns to see if there is a "vertical win". Returns a 1
    or a 0.'''
    winner = 0
    count = ['']*9
    for i in range (0,9):
        for z in range (0,7):
            count[i] += str(board[i][z])
    for k in range (0,9):
        if 'OOOOO' in count[k]:
            winner += 1
        elif 'XXXXX' in count[k]:
            winner += 1
        else:
            winner += 0
    return winner


def check_winner_horizontal (board):
    '''Given the current board, this function will check all rows to see if there is a "horizontal win". Returns a 1
    or a 0.'''
    winner = 0
    count = ['']*7
    for i in range (0,7):
        for z in range (0,9):
            count[i] += str(board[z][i])
    for k in range (0,7):
        if 'OOOOO' in count[k]:
            winner += 1
        elif 'XXXXX' in count[k]:
            winner += 1
        else:
            winner += 0
    return winner


def check_winner_diagonal (board):
    '''Given the current board, this function will check all rows and columns to see if there is a "diagonal win".
    Returns a 1 or a 0.'''
    winner = 0
    count0 = [''] * 7
    for i in range (0,7):
        count0[0] += str(board[i][i])
    for j in range (0,7):
        count0[1] += str(board[j+1][j])
    for k in range (0,7):
        count0[2] += str(board[k+2][k])
    for l in range (0,6):
        count0[3] += str(board[l+3][l])
    for m in range (0,5):
        count0[4] += str(board[m+4][m])
    for n in range (0,6):
        count0[5] += str(board[n][n+1])
    for o in range (0,5):
        count0[6] += str(board[o][o+2])

    count1 = [''] * 7
    for p in range (1,6):
        count1[0] += str(board[p-1][-p-2])
    for q in range (1,7):
        count1[1] += str(board[q-1][-q-1])
    for r in range (1,8):
        count1[2] += str(board[r-1][-r])
    for s in range (1,8):
        count1[3] += str(board[s][-s])
    for t in range (2,8):
        count1[4] += str(board[t][-t+1])
    for u in range (2,8):
        count1[5] += str(board[u+1][-u+1])
    for v in range (2,7):
        count1[6] += str(board[v+2][-v+1])

    for a in range (0,7):
        if 'OOOOO' in count0[a]:
            winner += 1
        elif 'XXXXX' in count0[a]:
            winner += 1
        else:
            winner += 0
    for b in range (0,7):
        if 'OOOOO' in count1[b]:
            winner += 1
        elif 'XXXXX' in count1[b]:
            winner += 1
        else:
            winner += 0
    return winner


def winner(board):
    '''This function takes the three "check_winner" components and combines them to check for all possible methods of
    winning (vertically, horizontally or diagonally).'''
    winner = 0
    if check_winner_horizontal(board) == 1:
        winner += 1
    elif check_winner_vertical(board) == 1:
        winner += 1
    elif check_winner_diagonal(board) == 1:
        winner += 1
    else:
        winner = 0
    return winner

def play_game(board):
    '''This function takes all of the other functions involved and uses them to play the game. It runs loops the game,
    reprinting the board after each turn. It also checks to see if the input for a move is valid, and if not returns an
    error message. If a player enters incorrect input 10 times their turn is forfeit. The game is declared a draw when
    the entire board is full, and nobody has connected 5.'''
    for e in range (0, 200):
        if e%2 == 0:
            player = 'X'
            column0 = str(raw_input("Player {0}, what is your move (column 0-8)?". format(player)))
            column1 = column0.strip()

            if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                    column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                    if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                        column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                        if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                            column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                            if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                                column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                                    column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                    if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                                        column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                        if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                                            column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                            if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                                                column1 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                                if len(column1)>1 or ord(column1)>56 or ord(column1)<48 or board[int(column1)][6]!=' ':
                                                    print 'You chose incorrect input 10 times, therefore your turn has been forfeit!'
                                                    column1 = 0
                                                    player = ' '

                                                    new_board = add_move_to_column(board, column1, player)
                                                    print print_board(new_board)
                                                    check_winner = winner(new_board)
                                                    if check_winner == 1:
                                                        return "Player X has won the game!"
                                                    elif check_winner == 0:
                                                        pass
                                                else:
                                                    new_board = add_move_to_column(board, column1, player)
                                                    print print_board(new_board)
                                                    check_winner = winner(new_board)
                                                    if check_winner == 1:
                                                        return "Player X has won the game!"
                                                    elif check_winner == 0:
                                                        pass
                                            else:
                                                new_board = add_move_to_column(board, column1, player)
                                                print print_board(new_board)
                                                check_winner = winner(new_board)
                                                if check_winner == 1:
                                                    return "Player X has won the game!"
                                                elif check_winner == 0:
                                                    pass
                                        else:
                                            new_board = add_move_to_column(board, column1, player)
                                            print print_board(new_board)
                                            check_winner = winner(new_board)
                                            if check_winner == 1:
                                                return "Player X has won the game!"
                                            elif check_winner == 0:
                                                pass
                                    else:
                                        new_board = add_move_to_column(board, column1, player)
                                        print print_board(new_board)
                                        check_winner = winner(new_board)
                                        if check_winner == 1:
                                            return "Player X has won the game!"
                                        elif check_winner == 0:
                                            pass
                                else:
                                   new_board = add_move_to_column(board, column1, player)
                                   print print_board(new_board)
                                   check_winner = winner(new_board)
                                   if check_winner == 1:
                                       return "Player X has won the game!"
                                   elif check_winner == 0:
                                     pass
                            else:
                                new_board = add_move_to_column(board, column1, player)
                                print print_board(new_board)
                                check_winner = winner(new_board)
                                if check_winner == 1:
                                    return "Player X has won the game!"
                                elif check_winner == 0:
                                    pass
                        else:
                            new_board = add_move_to_column(board, column1, player)
                            print print_board(new_board)
                            check_winner = winner(new_board)
                            if check_winner == 1:
                                return "Player X has won the game!"
                            elif check_winner == 0:
                                pass
                    else:
                        new_board = add_move_to_column(board, column1, player)
                        print print_board(new_board)
                        check_winner = winner(new_board)
                        if check_winner == 1:
                            return "Player X has won the game!"
                        elif check_winner == 0:
                            pass
                else:
                    new_board = add_move_to_column(board, column1, player)
                    print print_board(new_board)
                    check_winner = winner(new_board)
                    if check_winner == 1:
                        return "Player X has won the game!"
                    elif check_winner == 0:
                        pass


            else:
                new_board = add_move_to_column(board, column1, player)
                print print_board(new_board)
                check_winner = winner(new_board)
                if check_winner == 1:
                    return "Player X has won the game!"
                elif check_winner == 0:
                    pass

        else:
            player = 'O'
            column2 = str(raw_input("Player {0}, what is your move (column 0-8)?". format(player)))
            column3 = column2.strip()
            if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                    column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                    if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                        column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                        if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                            column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                            if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                                column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                                    column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                    if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                                        column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                        if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                                            column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                            if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                                                column3 = raw_input('Your input was invalid, please select an unfilled column 0-8.')

                                                if len(column3)>1 or ord(column3)>56 or ord(column3)<48 or board[int(column3)][6]!=' ':
                                                    print 'You chose incorrect input 10 times, therefore your turn has been forfeit!'
                                                    column3 = 0
                                                    player = ' '

                                                    new_board = add_move_to_column(board, column3, player)
                                                    print print_board(new_board)
                                                    check_winner = winner(new_board)
                                                    if check_winner == 1:
                                                        return "Player O has won the game!"
                                                    elif check_winner == 0:
                                                        pass
                                                else:
                                                    new_board = add_move_to_column(board, column3, player)
                                                    print print_board(new_board)
                                                    check_winner = winner(new_board)
                                                    if check_winner == 1:
                                                        return "Player O has won the game!"
                                                    elif check_winner == 0:
                                                        pass
                                            else:
                                                new_board = add_move_to_column(board, column3, player)
                                                print print_board(new_board)
                                                check_winner = winner(new_board)
                                                if check_winner == 1:
                                                    return "Player O has won the game!"
                                                elif check_winner == 0:
                                                    pass
                                        else:
                                            new_board = add_move_to_column(board, column3, player)
                                            print print_board(new_board)
                                            check_winner = winner(new_board)
                                            if check_winner == 1:
                                                return "Player O has won the game!"
                                            elif check_winner == 0:
                                                pass
                                    else:
                                        new_board = add_move_to_column(board, column3, player)
                                        print print_board(new_board)
                                        check_winner = winner(new_board)
                                        if check_winner == 1:
                                            return "Player O has won the game!"
                                        elif check_winner == 0:
                                            pass
                                else:
                                   new_board = add_move_to_column(board, column3, player)
                                   print print_board(new_board)
                                   check_winner = winner(new_board)
                                   if check_winner == 1:
                                       return "Player O has won the game!"
                                   elif check_winner == 0:
                                     pass
                            else:
                                new_board = add_move_to_column(board, column3, player)
                                print print_board(new_board)
                                check_winner = winner(new_board)
                                if check_winner == 1:
                                    return "Player O has won the game!"
                                elif check_winner == 0:
                                    pass
                        else:
                            new_board = add_move_to_column(board, column3, player)
                            print print_board(new_board)
                            check_winner = winner(new_board)
                            if check_winner == 1:
                                return "Player O has won the game!"
                            elif check_winner == 0:
                                pass
                    else:
                        new_board = add_move_to_column(board, column3, player)
                        print print_board(new_board)
                        check_winner = winner(new_board)
                        if check_winner == 1:
                            return "Player O has won the game!"
                        elif check_winner == 0:
                            pass
                else:
                    new_board = add_move_to_column(board, column3, player)
                    print print_board(new_board)
                    check_winner = winner(new_board)
                    if check_winner == 1:
                        return "Player O has won the game!"
                    elif check_winner == 0:
                        pass


            else:
                new_board = add_move_to_column(board, column3, player)
                print print_board(new_board)
                check_winner = winner(new_board)
                if check_winner == 1:
                    return "Player O has won the game!"
                elif check_winner == 0:
                    pass

        if board[0][6] != ' ' and board[1][6] != ' ' and board[2][6] != ' ' and board[3][6] != ' ' and \
                        board[4][6] != ' ' and board[5][6] != ' ' and board[6][6] != ' ' and board[7][6] != ' ' \
                and board[8][6] != ' ':
            return "The game is a draw!"
        else:
            pass

print play_game(starting_board)