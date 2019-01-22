import csv

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

def main():
    state = read_csv('0006d8be8e.csv')
    
main()