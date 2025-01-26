"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/data.csv', 'r') as f:
        data = f.readlines()

    count = {}
    for i in data:
        letter = i.split(',')[0]
        value = int(i.split(',')[1])
        if letter in count:
            count[letter].append(value)
        else:
            count[letter] = [value]

    result = []
    for k, v in count.items():
        result.append((k, max(v), min(v)))

    return sorted(result)