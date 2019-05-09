from dists import dists as d
from dists import straight_line_dists_from_bucharest as lr
from sys import argv as arg

def a_star(start, goal='Bucharest'):
    """
    Retorna uma lista com o caminho de start ate 
    goal segundo o algoritmo A*
    """
    x,_ = min([(x, y + lr[x]) for x, y in d[start]], key = lambda x: x[1])
    if x not in lista_final:
        lista_final.append(x)
    else:
        x,_ = sorted([(x, y + lr[x]) for x, y in d[start]],key=lambda x: x[1])[1]
        lista_final.append(x)
        
    if 'Bucharest' not in lista_final:
        a_star(lista_final[-1])
    return(lista_final)

cidade_inicial = arg
if cidade_inicial[1] in [x for x in lr]:
    print("Inicia em: " + cidade_inicial[1])
    lista_final = []
    lista_final.append(cidade_inicial[1])
    print(a_star(cidade_inicial[1]))
else:
    print("Digite como argumento uma dessas cidades:")
    print([x for x in lr])
