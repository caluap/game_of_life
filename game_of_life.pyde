W = 200
H = 200
CELL_SIZE = 4

state_key = [color(0,0,0), color(255,0,128), color(0,128,255)]
state = []


def set_random_state():
    global W, H, state_key
    aux_state = []
    for x in range(W):
        aux_state.append([])
        for y in range(H):
            s = int(random(len(state_key)))
            aux_state[x].append(s)
    return aux_state    



def setup():
    global W, H, CELL_SIZE, state
    noStroke()
    size((W-2) * CELL_SIZE, (H-2) * CELL_SIZE)
    state = set_random_state()
    # frameRate(4)
    
def sum_neighbors(state, x, y):
    global state_key
    sum = [0]*len(state_key)
    
    sum[state[x - 1][y - 1]] += 1 
    sum[state[x - 1][y]] += 1
    sum[state[x - 1][y + 1]] += 1
    
    sum[state[x][y - 1]] += 1
    sum[state[x][y + 1]] += 1
    
    sum[state[x + 1][y - 1]] += 1
    sum[state[x + 1][y]] += 1
    sum[state[x + 1][y + 1]] += 1

    return sum
    
    
    
def advance_state():
    global W, H, state
    new_state = [] 
    
    for x in range(W):
        new_state.append([])
                
        for y in range(H):
            current = state[x][y]
            
            # border
            if x == 0 or x == W-1 or y == 0 or y == H-1:
                pass
            else:
                neighbors = sum_neighbors(state, x, y)
                current = state[x][y]
                # overcrowding
                if neighbors[1] + neighbors[2] >= 4:
                    current = 0
                # sexual frustration rule                
                elif (current == 1 and neighbors[1] == 0) or (current == 2 and neighbors[2] == 0):
                    current = 0
                # birth rule
                elif neighbors[1] + neighbors[2] == 3:
                    if neighbors[1] > neighbors[2]:
                        current = 1
                    else:
                        current = 2
                
                        
            new_state[x].append(current)            
    state = new_state

def draw():
    global W, H, CELL_SIZE, state, state_key
    advance_state()
    for x in range(1, W-1):
        for y in range(1, H-1):
            fill(state_key[state[x][y]])
            rect((x-1) * CELL_SIZE, (y-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
    

def keyReleased():
    global state
    state = set_random_state()
