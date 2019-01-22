W = 200
H = 100
CELL_SIZE = 4
n_range = 3


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
    size(W * CELL_SIZE, H * CELL_SIZE)
    state = set_random_state()
    # frameRate(10)
    
def sum_neighbors(state, x, y):
    global state_key, n_range
    sum = [0]*len(state_key)
    
    for aux_x in range(-n_range, n_range+1):
        for aux_y in range(-n_range, n_range+1):
            if aux_x == aux_y == 0:
                pass
            else:
                i = return_state(x + aux_x, y + aux_y)
                sum[i] += 1

    return sum

def _x(x):
    global W
    return x % W

def _y(y):
    global H
    return y % H
    
def return_state(x, y):
    global state
    return state[_x(x)][_y(y)]      
    
    
def advance_state():
    global W, H, state, n_range
    new_state = [] 
    
    for x in range(W):
        new_state.append([])
                
        for y in range(H):
            
            current = return_state(x, y)
            neighbors = sum_neighbors(state, x, y)
            
            over = 9 * n_range
            birth = 1 * n_range
            
            # overcrowding
            if neighbors[1] + neighbors[2] > over:
                current = 0
            # sexual frustration rule                
            elif current == 1 and neighbors[1] == 0:
                current = 0
            elif current == 2 and neighbors[2] == 0:
                current = 0
            # birth rule
            elif neighbors[1] + neighbors[2] < birth:
                if neighbors[1] > neighbors[2]:
                    current = 1
                elif neighbors[2] > neighbors[1]:
                    current = 2
                
                        
            new_state[x].append(current)            
    state = new_state

def draw():
    global W, H, CELL_SIZE, state, state_key
    advance_state()
    for x in range(W):
        for y in range(H):
            fill(state_key[return_state(x, y)])
            rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
    
def keyReleased():
    global state
    state = set_random_state()

def mouseClicked(event):
    global CELL_SIZE, state
    if mouseButton == LEFT:
        c = 1
    else:
        c = 2
    x = mouseX // CELL_SIZE
    y = mouseY // CELL_SIZE
    
    for aux_x in range(-20,21):
        for aux_y in range(-20,21):
            if aux_x % 2 == 1:
                state[_x(x + aux_x)][_y(y + aux_y)] = c
                
def mousePressed():
    noLoop()  # Holding down the mouse activates looping

def mouseReleased():
    loop()  # Releasing the mouse stops looping draw()
