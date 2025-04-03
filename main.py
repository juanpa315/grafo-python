from grafo import Grafo

lista_aristas = [
    (0,1,2), (0,2,4), (0,4,-2), (0,5,1), (0,6,5),
    (2,3,3), (2,4,2), (3,8,-4), (4,3,5), (4,8,1),
    (4,7,2), (5,7,-1), (5,8,-3), (6,7,6), (7,8,2)
]
vertices = [0,1,2,3,4,5,6,7,8]


objgrafo = Grafo()
grafo_creado = objgrafo.crear_grafo(lista_aristas)

#1. Vertice alcanzable por el mayor numero de aristas desde el vertice 0
vertice_mas_alcanzable = objgrafo.encontrar_vertice_mayormente_alcanzable(grafo_creado, vertices)
print(f'\n1. El vertice mayormente alcanzable desde el nodo 0 es: {vertice_mas_alcanzable[0]} con un total de {vertice_mas_alcanzable[1]} caminos \n')

#2. Ordena e imprima las rutas de forma descendente
rutas_x_vertice = objgrafo.encontrar_caminos(grafo_creado, 0, vertice_mas_alcanzable[0])
caminos_ordenados = sorted(rutas_x_vertice, key=lambda x: x[-1], reverse=True)
print(f'''2. Todos los caminos desde 0 hasta {vertice_mas_alcanzable[0]} ordenados de forma descendente por peso son:\n''')
for camino in caminos_ordenados:
    print(f'''Ruta {camino[:-1]} con un peso de {camino[-1]}''')

#3. Introduzca un vértice adicional (V`) que cumpla las siguientes condiciones...
lista_aristas.extend([(1,9,1), (0,9,1), (2,9,1), (6,9,1), (8,9,1)])

nuevo_grafo = objgrafo.crear_grafo(lista_aristas)
vertices.append(9)

vertice_mas_alcanzable = objgrafo.encontrar_vertice_mayormente_alcanzable(nuevo_grafo, vertices)
print(f'\n3. Con el nuevo grafo ahora el vertice mas alcanzable desde el nodo 0 es: {vertice_mas_alcanzable[0]} con un total de {vertice_mas_alcanzable[1]} caminos \n')

print("Elementos del grafo.")
for element in lista_aristas:
    print('{' + ','.join(map(str, element)) + '}')
