"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open('files/data.csv', 'r') as f:
        data = f.readlines()

    count = {}

    for i in data:
        letter = i.split(',')[3]
        value = int(i.split(',')[1])
        if letter in count:
            count[letter] += value
        else:
            count[letter] = value
    
    count = dict(sorted(count.items()))

    return count

