import csv

tile_size = 5
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

def draw_pattern(pattern, x, y):
    n = ne = e = se = s = sw = w = nw = False
    patterns = [1, 2]
    
    if read_pattern(x-1, y-1) in patterns: nw = True    
    if read_pattern(x, y-1) in patterns: n = True    
    if read_pattern(x+1, y-1) in patterns: ne = True    
    
    if read_pattern(x-1, y) in patterns: w = True    
    if read_pattern(x+1, y) in patterns: e = True    
    
    if read_pattern(x-1, y+1) in patterns: sw = True    
    if read_pattern(x, y+1) in patterns: s = True    
    if read_pattern(x+1, y+1) in patterns: se = True
    
    if pattern == 0:
        return

    # paints background of each tile
    if False:        
        strokeWidth(0)        
        if pattern == 1:
            fill(0.1,0,0)
        elif pattern == 2:
            fill(0,0,0.1)        
        rect(x*tile_size, y*tile_size, tile_size, tile_size)
        
    
    strokeWidth(0.5)
    if pattern == 1:
        # stroke_hex('#9EC6EC')
        stroke_hex('#FF0054')
    elif pattern == 2:
        stroke_hex('#6BB7FF')
        stroke_hex('#FFFEEA')
    
    center = (x*tile_size + tile_size/2, y*tile_size + tile_size/2)
    
    if nw: line((x*tile_size, y*tile_size), center)
    if n: line((x*tile_size + tile_size/2, y*tile_size), center)
    if ne: line((x*tile_size + tile_size, y*tile_size), center)
    
    if sw: line((x*tile_size, (y+1)*tile_size), center)
    if s: line((x*tile_size + tile_size/2, (y+1)*tile_size), center)
    if se: line((x*tile_size + tile_size, (y+1)*tile_size), center)
        
    if w: line((x*tile_size, y*tile_size + tile_size/2), center)
    if e: line((x*tile_size + tile_size, y*tile_size + tile_size/2), center)

def main():
    global h, w, state
    files = ['3aa4cd061d', '0db91342a4', 'a973da1aaf', '3e0bbf4369', '4c25a17e6d', 'ca970ad966']
    

    # setup     
    state = read_csv(files[4] + '.csv')
    w = len(state)
    h = len(state[0])
    size(w*tile_size, h*tile_size)

    fill_hex('#381300')
    rect(0,0,width(),height())
    
    for x in range(len(state)):
        for y in range(len(state[x])):
            draw_pattern(read_pattern(x, y), x, y)
    
main()