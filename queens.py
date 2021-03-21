import search

initial_state=(1,2,0,3)

up = -1
down = +1

def actions(state):
    act=[]
    for i, j in enumerate(state):
        if j == 0:
            act.append((i,down))
        elif j == 3:
            act.append((i,up))
        else:
            act.append((i,down))
            act.append((i,up))
    return act
        
def result(state,action):
    s = list(state)
    s[action[0]] += action[1]
    return tuple(s)

def goal_test(state):
    for i in range(len(state)-1):
        if state[i] == (state[i+1]+1) or state[i] == (state[i+1]-1): return ((4 == len(set(state))) and False)
    return   ((4 == len(set(state))) and True)

solution=search.bfs(initial_state,goal_test,result,actions)
print solution




