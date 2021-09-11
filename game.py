def display(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


r = [' ']*10
display(r)


def user_input():
    m = input("player1 choose 'x' or '0': ")
    while m != 'x' and m != '0':
        m = input("player1 choose 'x' or '0': ")
    return m


# user input position
def user_position():
    p = int(input('choose a position from (1,9): '))
    while p not in range(0, 10) or r[p] != ' ':
        p = int(input('choose a position from (1,9): '))
    return p


def game(board):
    board[user_position()] = user_input()
    return display(board)


def win_check(board):
    if board[1] == board[2] == board[3] == 'x' or board[4] == board[5] == board[6] == 'x' or \
        board[7] == board[8] == board[9] == 'x' or board[1] == board[4] == board[7] == 'x' or \
        board[2] == board[5] == board[8] == 'x' or board[3] == board[6] == board[9] == 'x' or \
            board[1] == board[5] == board[9] == 'x' or board[3] == board[5] == board[7] == 'x':
        return True
    elif board[1] == board[2] == board[3] == '0' or board[4] == board[5] == board[6] == '0' or \
        board[7] == board[8] == board[9] == '0' or board[1] == board[4] == board[7] == '0' or \
        board[2] == board[5] == board[8] == '0' or board[3] == board[6] == board[9] == '0' or \
            board[1] == board[5] == board[9] == '0' or board[3] == board[5] == board[7] == '0':
        return True


def tie_check(board):
    if board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8] and board[9] != ' ':
        return True


rst = True
while rst:
    game(r)
    if win_check(r) is True:
        print("game over : player wins")
        rst = False
    elif tie_check(r) == True:
        print("its a tie")
        rst = False

