lista = [2, 3, 4]

for numbers in lista:
    lista[numbers.__index__()] = numbers * 2
