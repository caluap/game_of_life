import csv

W = 108/2
H = 108/2
CELL_SIZE = 6*2
n_range = 3
is_looping = True


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
            
            
            # chaos city
            # n_range = 3
            # over = 9.1 * n_range
            # birth = 0.6 * n_range
            
            # thicky wormy
            n_range = 3
            over = 9.5 * n_range
            birth = 8.5 * n_range
            
            # blob city
            # n_range = 5
            # over = 20 * n_range
            # birth = 16 * n_range
            
            # somewhat orderly city
            # n_range = 3
            # over = 9.5 * n_range #9.5
            # birth = 3.8 * n_range #3.8
            
            
            # maze
            # n_range = 1
            # over = 6 * n_range
            # birth = 4 * n_range
            
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
    global state, is_looping
    if keyCode == 32:
        import hashlib
        h = hashlib.md5()
        h.update(str(random(9999)))
        f = h.hexdigest()[:10]
        
        print(f)
        path = '/Users/calua/google_drive/Preface/Projetos/sbfoton/evento_2019/piv/sketches/game_of_life'
        
        f1 = path + '/output/' + f + '.png'
        f2 = path + '/output/' + f + '.csv'
        
        with open(f2, 'wb') as csv_file:
            wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            wr.writerow(state)
            
        save(f1)
        
    else:
        if is_looping:
            noLoop()
        else:
            loop()
        is_looping = not is_looping

def mouseClicked():
    global state
    state = set_random_state()
