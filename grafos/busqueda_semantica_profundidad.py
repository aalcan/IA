#PARA MEJOR COMPRENSION EL VALOR 'a': [('p',4), ('j',15), ('b',1)],
#INDICA QUE EL VERTICE 'a' ES ADYACENTE CON 'P', CON 'J' Y CON 'b'

grafo = False
import json
with open('arbol.json') as file:
    grafo =json.load(file)
#MUESTRA EL GRAFO ANTES DEL RECORRIDO
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
    print(key, lista)

def profundidad():      
    visitados = []
    pila = []
    origen = '10'
    destino = '14'
    print("\nLista de recorrido en profundidad\n")
    #Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA PILA
    pila.append(origen)
    #Paso 2: MIENTRAS LA PILA NO ESTE VACÍA
    while pila:
        #paso 3: DESAPILAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
        actual = pila.pop()
        print("Vertice actual -> ", actual)
        #FORMA ALTERNATIVA PARA DESAPILAR:
        #actual = pila[-1]
        #pila.remove(pila[-1])
        if actual==destino:
            visitados.append(actual)
            print(visitados)
            return

        #paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
        if actual not in visitados:
            #paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
            
            #paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
            visitados.append(actual)
        #paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
        #        Y QUE NO HA SIDO VISITADO:
        #        APILAR EL VERTICE
        for key in grafo[actual]:
            if key not in visitados:
                pila.append(key)

    print(visitados)

profundidad()