import csv
import random

tile_size = 10
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


def find_neighbors(pattern, patterns, x, y):
    n = e = w = s = nw = ne = sw = se = False
    if read_pattern(x, y-1) in patterns: n = True    
    if read_pattern(x-1, y) in patterns: w = True    
    if read_pattern(x+1, y) in patterns: e = True    
    if read_pattern(x, y+1) in patterns: s = True  

    if read_pattern(x-1, y-1) in patterns: nw = True    
    if read_pattern(x+1, y-1) in patterns: ne = True    
    if read_pattern(x-1, y+1) in patterns: sw = True    
    if read_pattern(x+1, y+1) in patterns: se = True
    
    return ne, e, se, s, sw, w, nw, n
    

def draw_pattern_2(pattern, x, y):
    patterns = [1, 2]
    # begins at 45º (considering the center as (0,0))
    deltas = [(1, -1),
            (1, 0), 
            (1, 1), 
            (0, 1), 
            (-1, 1), 
            (-1, 0), 
            (-1, -1), 
            (0, -1)]
    neigh = find_neighbors(pattern, patterns, x, y)
    
    # divides each tile in 9 sub_modules (3x3)
    sub_module = tile_size / 3
    # many points will be placed inside each sub_module? (max and min)
    max_points = 3
    min_points = 1

    points = []
    for i in range(len(deltas)):
        if neigh[i]:
            n_points = round(random.uniform(min_points, max_points))
            for _ in range(n_points):
                rand_x = random.random() * sub_module + (deltas[i][0]+1) * sub_module
                rand_y = random.random() * sub_module + (deltas[i][1]+1) * sub_module
                points.append((
                    rand_x, rand_y
                    ))
    
    center = (x*tile_size + tile_size/2, y*tile_size + tile_size/2)
    strokeWidth(0)
    
    c = ['#FF0054','#FFFEEA']
    if pattern == 1:
        stroke_hex(c[0])
        fill_hex(c[0])
    elif pattern == 2:
        stroke_hex(c[1])
        fill_hex(c[1])
        
    s = 4
    
    # path = BezierPath()
    # path.moveTo((center[0], center[1]))
    
    for i in range(len(points)):
        # path.lineTo((points[i][0] + center[0] - s/2, points[i][1] + center[1] - s/2))
        oval(points[i][0] + center[0] - s/2, points[i][1] + center[1] - s/2, s, s)
    
    # path.closePath()
    # drawPath(path)
        


def draw_pattern(pattern, x, y):    
    patterns = [1,2]
    ne, e, se, s, sw, w, nw, n = find_neighbors(pattern, patterns, x, y)    
    
    if pattern == 0:
        return
    
    delta_x = 0
    delta_y = 0
    
    if n:
        delta_x += 0
        delta_y += -1    
    if s:
        delta_x += 0
        delta_y += 1   
    if e:
        delta_x += 1
        delta_y += 0    
    if w:
        delta_x += -1
        delta_y += 0
    
    if ne:
        delta_x += 1
        delta_y += -1    
    if nw:
        delta_x += -1
        delta_y += -1   
    if se:
        delta_x += 1
        delta_y += 1    
    if sw:
        delta_x += -1
        delta_y += 1
        
    c = ['#FF0054','#FF0054']

    strokeWidth(0)
 
    path = BezierPath()
    
    path.moveTo((x * tile_size, y * tile_size))
    path.lineTo((x * tile_size, (y + 1) * tile_size))
    path.lineTo(((x + 1) * tile_size, (y + 1) * tile_size))
    path.lineTo(((x + 1) * tile_size, y * tile_size))
    path.lineTo((x + 1 * tile_size, y * tile_size))
    path.closePath()
    
    fill_hex('#333333')

    # drawPath(path)
    
    if pattern == 1:
        fill_hex(c[0])
    elif pattern == 2:
        fill_hex(c[1])

    center = (x*tile_size + tile_size/2, y*tile_size + tile_size/2)
    
    s = abs(2 * delta_x + 2)
    
    with savedState():
        clipPath(path)
        oval(center[0] - s/2, center[1] - s/2, s, s)
    
    

def main():
    global h, w, state
    files = ['5bb7c9af74', '281d9f0815']
    

    # setup
    for f in files:
        state = read_csv(f + '.csv')
        w = len(state)
        h = len(state[0])
        newPage(w*tile_size, h*tile_size)
        lineCap("round")
        fill_hex('#381300')
        rect(0,0,width(),height())
    
        for x in range(len(state)):
            for y in range(len(state[x])):
                draw_pattern_2(read_pattern(x, y), x, y)
                # draw_pattern(read_pattern(x, y), x, y)
    
main()