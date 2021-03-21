import random

initial_state = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0]]

symbols = {0:' ', 1:'x', -1:'o'}

def actions(state):
    act = []
    for i in reversed(range(6)):
        if i==5:
            for j,e in enumerate(state[i]):
                if e == 0:
                    act.append((i,j))
        if i<5:
            for j,e in enumerate(state[i]):
                if e == 0:
                    if (state[i+1][j] != 0):
                        act.append((i,j))
    random.shuffle(act)
    return act
    
def result(state,action):
    state[action[0]][action[1]] = player(state)
    return state

def player(state):
    s = 0
    for i in state:
        for e in i:
            s += e
    if s == 0:
        return 1
    if s == 1:
        return -1
        
def cutoff_test(state,depth):
    return ( depth == 0 or evalu(state) != 0 or len(actions(state)) == 0 )
    
def evalu(state):
    for i in range(6):
        for j in range(4):
            if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] ==  1 :
                return state[i][j]
            if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] ==  -1 :
                return state[i][j]
    for j in range(7):
        for i in range(3):
            if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] ==  1 :
                return state[i][j]
            if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] ==  -1 :
                return state[i][j]
    for j in range(4):
        for i in range(3):
            if state[i][j] == state[i+1][j+1] == state[i+2][j+2] == state[i+3][j+3] ==  1 :
                return state[i][j]
            if state[i][j] == state[i+1][j+1] == state[i+2][j+2] == state[i+3][j+3] ==  -1 :
                return state[i][j]
    for j in reversed(range(3,7)):
        for i in range(3):
            if state[i][j] == state[i+1][j-1] == state[i+2][j-2] == state[i+3][j-3] ==  1 :
                return state[i][j]
            if state[i][j] == state[i+1][j-1] == state[i+2][j-2] == state[i+3][j-3] ==  -1 :
                return state[i][j]
    return 0

def printBoard(state):
    print ("  ","0","1","2","3","4","5","6")
    print ("0", map(symbols.get, state[0]))
    print ("1", map(symbols.get, state[1]))
    print ("2", map(symbols.get, state[2]))
    print ("3", map(symbols.get, state[3]))
    print ("4", map(symbols.get, state[4]))
    print ("5", map(symbols.get, state[5]))
    print ''
    
def autoplay(state, depth):
    while not cutoff_test(state,depth):
        #action = input('> ')
        action, _ = alpha_beta_search(state, cutoff_test, player, evalu, result, actions, depth, -10000000, 10000000)
        state = result(state, action)
        print "Player 1"
        printBoard(state)
        if cutoff_test(state,depth):
            break
        action, _ = alpha_beta_search(state, cutoff_test, player, evalu, result, actions, depth, -10000000, 10000000)
        #action, _ = minimax(state, depth)
        state = result(state, action)
        print " "
        print "Player 2 "
        printBoard(state)
    return evalu(state)

# Game Library

def minimax(state, depth):

    if cutoff_test(state,depth) : return None, evalu(state)
    v, f = {-1:(10, min), 1:(-10, max)}.get(player(state))
    for a in actions(state):
        s = result(state, a)
        _,nv = minimax(s, depth-1)
        if f(v,nv) == nv:
            action, v = a, nv
    return action, v
    

    
def alpha_beta_search(state, cutoff_test, player, evalu, result, actions, depth, alpha, beta):
    
    if cutoff_test(state,depth):
        return None, evalu(state)
    action = None
    
    if player(state) == 1:
        v = -10000000 
        for a in actions(state):
            s = result(state,a)
            _, nv = alpha_beta_search(s, cutoff_test, player, evalu, result, actions, depth-1, alpha, beta) 
            if v <= nv:
                v = max(v,nv)
                action = a
            s[a[0]][a[1]] = 0
            if v >= beta:
                return action, v
            alpha = max(alpha,v)
        return action, v
        
    if player(state) == -1:
        v = 10000000
        for a in actions(state):
            s = result(state,a)
            _, nv = alpha_beta_search(s, cutoff_test, player, evalu, result, actions, depth-1, alpha, beta) 
            if v >= nv:
                v = min(v,nv)
                action = a
            s[a[0]][a[1]] = 0
            if v <= alpha:
                return action, v
            beta = min(beta,v)
        return action, v
        
        

    
# App

winner = autoplay(initial_state, 5)
print 'Winner', winner







