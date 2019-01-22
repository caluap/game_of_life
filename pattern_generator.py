import csv

tile_size = 3
state = []
path = '/Users/calua/google_drive/Preface/Projetos/sbfoton/evento_2019/piv/sketches/game_of_life/output/'

w = h = -1


def read_csv(filename):
    aux = []
    with open(path + filename, 'rt') as f:
        reader = csv.reader(f)
        for __ in list(reader):
            for line in __:         
                aux.append([])
                # removes [, ] and splits by ,
                d = line[1:-1].split(',')
                for c in d:
                    aux[len(aux)-1].append(int(c.strip()))
    return aux
    
def hex2rgb(c):    
    c = c.strip('#')
    return tuple(int(c[i:i+2], 16)/255 for i in (0, 2, 4))
    
def stroke_hex(c):
    c2 = hex2rgb(c)
    stroke(c2[0], c2[1], c2[2])
    
def fill_hex(c):
    c2 = hex2rgb(c)
    fill(c2[0], c2[1], c2[2])

def read_pattern(x, y):
    return state[x % w][h - 1 - y % h]
    
def draw_diagonals(pattern, patterns, x, y, stro, c, mode):
    nw = ne = sw = se = False
    if read_pattern(x-1, y-1) in patterns: nw = True    
    if read_pattern(x+1, y-1) in patterns: ne = True    
    if read_pattern(x-1, y+1) in patterns: sw = True    
    if read_pattern(x+1, y+1) in patterns: se = True
    
    center = (x*tile_size + tile_size/2, y*tile_size + tile_size/2)

    strokeWidth(stro)
    if pattern == 1:
        stroke_hex(c[0])
    elif pattern == 2:
        stroke_hex(c[1])
        
    if mode == 1:
        if ne and se:
            line((x*tile_size + tile_size, y*tile_size), center)
            line((x*tile_size + tile_size, (y+1)*tile_size), center)
    else:
        if nw: line((x*tile_size, y*tile_size), center)
        if ne: line((x*tile_size + tile_size, y*tile_size), center)
        if sw: line((x*tile_size, (y+1)*tile_size), center)
        if se: line((x*tile_size + tile_size, (y+1)*tile_size), center)

    
def draw_ortogonals(pattern, patterns,  x, y, stro, c, mode):
    n = e = w = s = False
    if read_pattern(x, y-1) in patterns: n = True    
    if read_pattern(x-1, y) in patterns: w = True    
    if read_pattern(x+1, y) in patterns: e = True    
    if read_pattern(x, y+1) in patterns: s = True 
    
    center = (x*tile_size + tile_size/2, y*tile_size + tile_size/2)

    strokeWidth(stro)
    if pattern == 1:
        stroke_hex(c[0])
    elif pattern == 2:
        stroke_hex(c[1])    
        
    if mode == 1:
        if n and s: 
            line((x*tile_size + tile_size/2, y*tile_size), center)
            line((x*tile_size + tile_size/2, (y+1)*tile_size), center)
    else: 
        if mode == 2:
            if n and s and w and e: 
                return
        if mode == 3:
            if n:
                oval((x+0.25)*tile_size, (y-0.25)*tile_size, tile_size/2, tile_size/2)
            if s: 
                oval((x+0.25)*tile_size, (y+0.75)*tile_size, tile_size/2, tile_size/2)

        else:            
            if n: line((x*tile_size + tile_size/2, y*tile_size), center)    
            if s: line((x*tile_size + tile_size/2, (y+1)*tile_size), center)
            if w: line((x*tile_size, y*tile_size + tile_size/2), center)
            if e: line((x*tile_size + tile_size, y*tile_size + tile_size/2), center)


def draw_pattern(pattern, x, y):
    if pattern == 0:
        return
    draw_diagonals(pattern, [1, 2], x, y, 0.5, ['#FF0054','#FFFEEA'], 0)   
    draw_ortogonals(pattern, [1, 2], x, y, 0.5, ['#FF0054','#FFFEEA'], 0)
    

def main():
    global h, w, state
    files = ['3aa4cd061d', '0db91342a4', 'a973da1aaf', '3e0bbf4369', '4c25a17e6d', 'ca970ad966', 'de4fddafec', 'db9c349fd3', 'acffa5f7ed', '59d61a1a87', 'fddc3ae8c6']
    

    # setup     
    state = read_csv(files[7] + '.csv')
    w = len(state)
    h = len(state[0])
    size(w*tile_size, h*tile_size)
    lineCap("round")
    fill_hex('#381300')
    rect(0,0,width(),height())
    
    for x in range(len(state)):
        for y in range(len(state[x])):
            draw_pattern(read_pattern(x, y), x, y)
    
main()