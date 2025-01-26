"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open('files/data.csv', 'r') as f:
        data = f.readlines()

    count = []
    for i in data:
        letter = i.split(',')[0]
        value_1 = int(i.split(',')[3])
        value_2 = int(i.split(',')[4])
        count.append((letter, value_1, value_2))

    return count


