import csv

tile_size = 10
state = []
path = '/Users/calua/google_drive/Preface/Projetos/sbfoton/evento_2019/piv/sketches/game_of_life/output/'


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

def draw_pattern(pattern, x, y):
    if pattern == 1:
        fill(1,0,0)
    elif pattern == 2:
        fill(0,0,1)
    else:
        fill(0,0,0)
    rect(x*tile_size, y*tile_size, tile_size, tile_size)

def main():
    
    state = read_csv('0006d8be8e.csv')
    w = len(state)
    h = len(state[0])
    size(w*tile_size, h*tile_size)
    for x in range(len(state)):
        for y in range(len(state[x])):
            draw_pattern(state[x][y], x, y)
    
main()