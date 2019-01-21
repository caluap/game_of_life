import pprint

W = 200
H = 150
CELL_SIZE = 5


state = []


def set_random_state():
    global W, H
    aux_state = []
    for x in range(W):
        aux_state.append([])
        for y in range(H):
            aux_state[x].append(int(random(2)))
    return aux_state
    



def setup():
    global W, H, CELL_SIZE, state
    size((W-2) * CELL_SIZE, (H-2) * CELL_SIZE)
    state = set_random_state()
    
def sum_neighbors(state, x, y):
    sum = 0
    
    sum += state[x - 1][y - 1]
    sum += state[x - 1][y]
    sum += state[x - 1][y + 1]
    
    sum += state[x][y - 1]
    sum += state[x][y + 1]
    
    sum += state[x + 1][y - 1]
    sum += state[x + 1][y]
    sum += state[x + 1][y + 1]
    
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
                if current == 1:
                    # underpopulation or overpopulation will kill a live cell
                    if neighbors < 2 or neighbors > 3:
                        current = 0
                elif current == 0:
                    # reproduction!
                    if neighbors == 3:
                        current = 1
                        
            new_state[x].append(current)            
    state = new_state

def draw():
    global W, H, CELL_SIZE, state
    for x in range(1, W-1):
        for y in range(1, H-1):
            if state[x][y] == 1:
                f = 0
            else:
                f = 1
                
            noStroke()                            
            fill([0,255][f])
            rect((x-1) * CELL_SIZE, (y-1) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
    advance_state()

def keyReleased():
    global state
    state = set_random_state()
