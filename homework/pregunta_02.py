"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('files/input/data.csv', 'r') as f:
        data = f.readlines()

    count = {}

    for i in data:
        letter = i.split()[0]
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    count = sorted(count.items())

    return count

print(pregunta_02())