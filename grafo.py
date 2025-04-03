from collections import defaultdict

class Grafo:

    def crear_grafo(self, aristas):
        grafo = defaultdict(list)
        for origen, destino, peso in aristas:
            grafo[origen].append((destino, peso))
        return grafo
        

    def encontrar_vertice_mayormente_alcanzable(self, grafo, vertices):
        vertice_mas_alcanzable = [0,0]
        for nodo in vertices:
            if nodo == 0:
                continue
            caminos_nodo= self.encontrar_caminos(grafo, 0, nodo)
            if len(caminos_nodo) > vertice_mas_alcanzable[1]:
                vertice_mas_alcanzable = [nodo, len(caminos_nodo)]
        return vertice_mas_alcanzable
            


    def encontrar_caminos(self, grafo, vertice_inicio, vertice_fin, ruta=[], peso_total=0):
        ruta = ruta+[vertice_inicio]
        if vertice_inicio == vertice_fin:
            return [ruta + [peso_total]]
        if vertice_inicio not in grafo:
            return []
        caminos=[]
        for vecino, peso in grafo[vertice_inicio]:
            if vecino not in caminos:
                nuevo_camino = self.encontrar_caminos(grafo, vecino, vertice_fin, ruta, peso_total + peso)
                for p in nuevo_camino:
                    caminos.append(p)
        return caminos