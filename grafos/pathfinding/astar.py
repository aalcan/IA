import numpy as np
import json

class Nodo:
    """
        Creamos un objeto tipo Nodo para el algoritmo A* Pathfinding
        Padre es el dada la redundancia el padre del nodo
        Posicion es la posicion actual del nodo
        g es el costoo G(n) del nodo actual
        h es la 'distancia' del nodo actual al final
        f Represeta el costo total:  f = g + h
    """

    def __init__(self, padre=None, posicion=None):
        self.padre = padre
        self.posicion = posicion

        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.posicion == other.posicion

#Regresa el camino de la busqueda
def reconstruir_camino(nodo_actual,maze):
    camino = []
    no_filas, no_columnas = np.shape(maze)
    # inicializamos valores con -1 de todos los nodos, no importa ya que tenemos las cordenadas del camino que se siguo
    resultado = [[-1 for i in range(no_columnas)] for j in range(no_filas)]
    actual = nodo_actual
    while actual is not None:
        camino.append(actual.posicion)
        actual = actual.padre
    # Como necesitamos mostrar de principio a fin camino regresamos el camino inverso
    camino = camino[::-1]
    valor_inicial = 0
    # Actualizamos el camino que se siguio dando numero a cada paso y vamos incrementando en 1
    for i in range(len(camino)):
        resultado[camino[i][0]][camino[i][1]] = valor_inicial
        valor_inicial += 1
    return resultado


def busqueda(matriz, costo, inicio, final):
    """
        Devuelve una lista de tuplas con un camino desde el comienzo dado 
        hasta el final dado en el laberinto dado
    """

    # Creamos el nodo inicial y final con valores iniciados para g, h y f
    nodo_inicial = Nodo(None, tuple(inicio))
    nodo_inicial.g = nodo_inicial.h = nodo_inicial.f = 0
    nodo_final = Nodo(None, tuple(final))
    nodo_final.g = nodo_final.h = nodo_final.f = 0

    # Inicializar tanto la lista de nodos_por_visitar 
    # en esta lista pondremos todos los nodos que aún están por visitar para su exploración.
    # Desde aquí encontraremos el nodo de costo más bajo para expandir a continuación
    nodos_por_visitar = []  
    # en esta lista pondremos todos los nodos ya explorados para que no lo volvamos a explorar
    nodos_visitados = [] 
    
    # Añadimos el nodo iniial
    nodos_por_visitar.append(nodo_inicial)
    
    # Añadiendo una condición de parada. Esto es para evitar cualquier bucle infinito y detener
    # la ejecución después de un número razonable de pasos
    # Gg, la verdad es que se me ciclaba :)
    pasos = 0
    pasos_maximos = (len(matriz) // 2) ** 10

    # En que casillas buscamos. El movimiento del es izquierda-derecha-arriba-abajo
    #(4 movimientos) para cada posicion

    movimientos  =  [[-1, 0 ], # Arriba
              [ 0, -1], # Izquierda
              [ 1, 0 ], # Abajo
              [ 0, 1 ]] # Derecha


    """
        1) Primero obtenemos el nodo actual comparando todos los costos y seleccionando el nodo de costo más bajo
        2) Comprobamos si la iteración máximaya fue alcanzada o no para detener la ejecución
        3) Elimine el nodo seleccionado de la lista nodos_por_visitar y agregue este nodo a la lista visitada
        4) Comprobmos si ya llegamos a nuestro objetivo y devolvemios el camino recorrido, de lo contrario:
        5) Para el nodo seleccionado, averiguar todos los hijos (nos movemos para ver esos hijos)
            a) obtener la posición actual para el nodo seleccionado (esto se convierte en nodo padre para los nodos hijos)
            b) comprobar si existe una posición válida (el límite invalidará algunos nodos)
            c) si algún nodo es una pared, ignora ese nodo
            d) agregar a la lista de nodos hijos válidos para el padre seleccionado
            
    """
    #Encontrar cuantas filas y cuantas columas tiene una matriz
    no_filas, no_columnas = np.shape(matriz)
    
    # Nos metemos al ciclo hasta que encuentre un fin
    
    while len(nodos_por_visitar) > 0:
        
        # Contador de pasos gg
        pasos += 1    

        
        # Obtner nodo actual
        nodo_actual = nodos_por_visitar[0]
        indice_actual = 0
        for indice, item in enumerate(nodos_por_visitar):
            if item.f < nodo_actual.f:
                nodo_actual = item
                indice_actual = indice
                
        # Si ya llegamos a los pasos maximos, nos deteneos
        if pasos > pasos_maximos:
            print ("Se cancela, esto fue a lo que se llego")
            return reconstruir_camino(nodo_actual,matriz)

        # Sacamos el nodo actual de la lista de nodos por visitar y lo agregamos a los visitador
        nodos_por_visitar.pop(indice_actual)
        nodos_visitados.append(nodo_actual)

        # Es el nodo actual nuestro destino? Si sí aquí acaba todo
        if nodo_actual == nodo_final:
            return reconstruir_camino(nodo_actual,matriz)

        # Hijos de todos los adyacentes
        hijos = []

        for nueva_posicion in movimientos: 

            # Obtenemos la posicion del nodo
            nodo_posicion = (nodo_actual.posicion[0] + nueva_posicion[0], nodo_actual.posicion[1] + nueva_posicion[1])

            # Nos aseguramos que esta en rango
            if (nodo_posicion[0] > (no_filas - 1) or 
                nodo_posicion[0] < 0 or 
                nodo_posicion[1] > (no_columnas -1) or 
                nodo_posicion[1] < 0):
                continue

            # Vemos si hay obstaculos 0 es libre 1 es obstaculo
            if matriz[nodo_posicion[0]][nodo_posicion[1]] != 0:
                continue

            # Creamos el nuevo nodo
            nuevo_nodo = Nodo(nodo_actual, nodo_posicion)

            # Append
            hijos.append(nuevo_nodo)

        # Loop through hijos
        for hijo in hijos:
            
            #El hijo esta en la lista de visitados
            if len([visited_child for visited_child in nodos_visitados if visited_child == hijo]) > 0:
                continue

            # Cramos los valores f, g, y h 
            hijo.g = nodo_actual.g + costo
            ## Calculamos el costo de h (x1-x2)+(y1-y2)
            hijo.h = (((hijo.posicion[0] - nodo_final.posicion[0]) ) + 
                       ((hijo.posicion[1] - nodo_final.posicion[1]) )) 

            hijo.f = hijo.g + hijo.h

            # El hijo ya esta en a lista de nodos por vistar y el costo de g es menor
            if len([i for i in nodos_por_visitar if hijo == i and hijo.g > i.g]) > 0:
                continue

            # Añador a nodos por visitar
            nodos_por_visitar.append(hijo)


if __name__ == '__main__':
    camino = []
    matriz = False
    with open('matriz.json') as file:
        matriz =json.load(file)
    print("Tablero inicial")
    for x in matriz:
        print(matriz[x])
        camino.append(matriz[x])
    inicio = [0, 0] # Cordenadas de inicio
    final = [(len(camino)-1),(len(camino[0])-1)] # Coordenadas de final
    costo = 1 # costo per movement
    camino_final = busqueda(camino,costo, inicio, final)
    print("-----------------")
    print("Tablero final")
    print('\n'.join([''.join(["{:" ">3d}".format(item) for item in row]) 
      for row in camino_final]))