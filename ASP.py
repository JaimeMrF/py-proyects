def crearASP(tamaño):
    alfabeto = [chr(ord('a')+i) for i in range(tamaño)]
    graph = { char: [other for other in alfabeto if other != char] for char in alfabeto}
    def recorrer(u,x):    
        while graph[u]:
           v = graph[u].pop()
           x = recorrer(v, x)
        x += 1  
        return x
    return recorrer(alfabeto[0],0)  
while True:
    try:
        tamaño = int(input('Introduzca el tamaño del alfabeto: '))
        print(f'El tamaño máximo de ASP para un alfabeto con longitud {tamaño} es: {crearASP(tamaño)}')
    except:
        break
