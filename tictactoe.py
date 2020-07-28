"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    boarlist = [x for l in board for x in l]
    x_count = boarlist.count('X')
    o_count = boarlist.count('O')
    if(o_count < x_count):
        return O
    return X


def actions(board):
    actions_set = set()
    for a in range(3):
        for b in range(3):
            if(board[a][b] == EMPTY):
                actions_set.add((a, b))
            pass
        pass

    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    result = copy.deepcopy(board)

    if(result[i][j] != EMPTY):
        raise NotImplementedError

    result[i][j] = player(result)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    player = X
    """
    Checkin Vertical line by line
    """
    for i in range(3):
        player = board[i][0]
        for j in range(3):
            if(player == EMPTY):
                break
            if(player != board[i][j]):
                break
            if(j == 2):
                return player

    """
    Checking horizontal line by line
    """
    for j in range(3):
        player = board[0][j]
        for i in range(3):
            if(player == EMPTY):
                break
            if(player != board[i][j]):
                break
            if(i == 2):
                return player

    """
    Checkin diagonals
    """
    player = board[0][0]
    dig = {(1, 1), (2, 2)}
    for i, j in dig:
        if(player == EMPTY):
            break
        if(player != board[i][j]):
            break
        if(i == 2):
            return player

    player = board[0][2]
    dig = {(1, 1), (2, 0)}
    for i, j in dig:
        if(player == EMPTY):
            break
        if(player != board[i][j]):
            break
        if(i == 2):
            return player
    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    boarlist = [x for l in board for x in l]
    if(winner(board) != EMPTY or boarlist.count(EMPTY) == 0):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == X):
        return 1
    if(winner(board) == O):
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None

    if X == player(board):
        maximizing_player = True
    else:
        maximizing_player = False
    opt_action = None
    opt_value = -2
    for a in actions(board):
        if maximizing_player:
            value = max(board, a)
            if opt_value == -2 or value > opt_value:
                opt_value = value
                opt_action = a
        else:
            value = mini(board, a)
            if opt_value == -2 or value < opt_value:
                opt_value = value
                opt_action = a
        # value = minimaxalgo(board, a, maximizing_player)
        # if (maximizing_player and value == 1) or ((not maximizing_player) and value == -1):
        #     return a

        # if opt_value == -2 or (maximizing_player and value > opt_value) or ((not maximizing_player) and value < opt_value):
        #     opt_value = value
        #     opt_action = a

    return opt_action


# def minimaxalgo(board, action, maximizing_player):
#     steps = 0
#     result_board = result(board, action)

#     if terminal(result_board):
#         return (steps+1, utility(result_board))
#     opt_value = -2
#     for a in actions(result_board):
#         steps, value = minimaxalgo(result_board, a, maximizing_player)
#         if (maximizing_player and value == 1) or ((not maximizing_player) and value == -1):
#             return (steps+1, value)
#         if opt_value == -2 or value == 0:
#             opt_value = value

#     return opt_value


def mini(board, action):
    result_board = result(board, action)

    if terminal(result_board):
        return utility(result_board)
    opt_value = -2
    for a in actions(result_board):
        value = max(result_board, a)
        if opt_value == -2 or value < opt_value:
            opt_value = value

    return opt_value


def max(board, action):
    result_board = result(board, action)

    if terminal(result_board):
        return utility(result_board)
    opt_value = -2
    for a in actions(result_board):
        value = mini(result_board, a)
        if opt_value == -2 or value > opt_value:
            opt_value = value

    return opt_value
