"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files/data.csv', 'r') as f:
        data = f.readlines()

    count = {}

    for i in data:
        letter = i.split(',')[0]
        value = int(i.split(',')[4])
        if letter in count:
            count[letter] += value
        else:
            count[letter] = value

    return count

