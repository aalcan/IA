print('#-----Busqueda subida de la colina-------#')
print()
#importamos 
import json
import random
#para abrir nuestro documento json
with open('conocimiento.json') as file:
	Conocimiento = json.load(file)


ruta=[]
way=[]
objetivo = 'E'
ruta.append('A')
def hill():
	while ruta:
	    #paso 3: DESAPILAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
	    actual = ruta.pop()
	    way.append(actual)
	    print("Vertice actual -> ", actual)
	    if actual == objetivo:
	    	return #Si lo encuentra aquí acaba todo
	    else:
	    	if actual != objetivo:#Sino mostramos los posibles caminos
	    		print("Posibles opciones",Conocimiento[actual])
	    		pesoIndice = [] #Creamos una lista vacia para el peso de cada camino
	    		for key,lista in Conocimiento[actual]:
	    			pesoIndice.append(lista)
	    		pesosRepetidos = repetidos(pesoIndice)#Verificamos si hay un peso que se repite
	    		if(len(pesosRepetidos)>0):#Hay mas de un peso que se repite?
	    			if pesosRepetidos[0]==min(pesoIndice):#El peso que se repite es igual al peso minimo de todas la opciones del camino?
	    				print("random way")#Entonces tomamos una desición aleatoria
	    				index = []#Creamos una lista para guardar los indices
	    				i = 0
		    			for key,lista in Conocimiento[actual]:
		    				if lista==pesosRepetidos[0]: #Si el indice coincide con el peso minimo
		    					index.append(i)#Guardamos el indice
		    					i+=1
		    			r = -1 #Variable que usaremos para el número random
		    			while r not in index: #Nos aseguramos que el valor random sea uno de los indices
		    				r = random.randrange(0,max(index)+1,1)
		    			print("indice ramdom",r)
		    			actual = (Conocimiento[actual][r][0])#Ahora nuestro nuevo camino será la desición random
		    			if actual != objetivo: #LLegamos a nuestro objetivo?
		    				ruta.append(actual)#Continuamos el ciclo
		    			else:
	    					way.append(actual)#Fin
		    		else: #Si el peso que se repite no es el minimo entonces continuamos normal
		    			for key,lista in Conocimiento[actual]:
		    				actual = key
		    				if key != objetivo:#LLegamos a nuestro objetivo?
		    					ruta.append(key)#Continuamos el ciclo
		    				else:
	    						way.append(key)#Fin
	    		else:#Si no hay pesos que se repiten entonces continuamos normal
	    			for key,lista in Conocimiento[actual]:
	    				if lista==min(pesoIndice): #Elejimos siempre el camino más corto
	    					actual = key #Nuestro actual ahora es el nodo con el camino más corto
	    					#Nuestro nodo actual es el objetivo?
	    					if key != objetivo:
	    						ruta.append(key)#Sino continuamos el ciclo
	    					else:
	    						way.append(key)#Fin

def repetidos(data):
	no_dup = []
	dup = []
	for item in data:
		if item not in no_dup:
			no_dup.append(item)
		else:
			dup.append(item)
	return dup

hill()
print("Nodos visitados",way)
