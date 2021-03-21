import random

# Tic Tac Toe

rules = ((0,1,2), (3,4,5), (6,7,8), # Horizontal
         (0,3,6), (1,4,7), (2,5,8), # Vertical
         (0,4,8), (2,4,6)) # Diagonal

symbols = {0:' ', 1:'x', -1:'o'}

def actions(state):
    action = [i for i, e in enumerate(state) if e == 0]
    random.shuffle(action)
    return action

def result(state,action):
    new_state = state[:]
    new_state[action] = player(state)
    new_state[-1] *= -1
    return new_state

def player(state):
    return state[-1]


def terminal_test(state):
    return len(actions(state)) == 0 or utility(state) != 0

def utility(state):
    for idxs in rules:
        s = sum(state[i] for i in idxs)
        if abs(s) == 3:
            return s/3
    return 0

def printBoard(state):
    print map(symbols.get, state[0:3])
    print map(symbols.get, state[3:6])
    print map(symbols.get, state[6:9])
    print ''


def autoplay(state):
    while not terminal_test(state):
        action = input('> ')
        state = result(state, action)
        printBoard(state)
        if terminal_test(state):
            break
        action, _ = minimax(state, terminal_test, player, utility,result, actions)
        state = result(state, action)
        printBoard(state)

    return utility(state)

# Game Library

def minimax(state, terminalTest, player, utility, result, actions):
    """
        state -> (action, value)
    """
    if terminalTest(state): return None, utility(state)
    v, f = {-1:(10, min), 1:(-10, max)}.get(player(state))
    for a in actions(state):
        s = result(state, a)
        _,nv = minimax(s, terminalTest, player, utility, result, actions)
        if f(v,nv) == nv:
            action, v = a, nv
    return action, v


# App

winner = autoplay([0]*9 + [1])
print 'Winner', winner


