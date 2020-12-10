import json
grafo = False
with open('grafo.json') as file:
	grafo = json.load(file)
tablero_inicial = False
with open('tablero_inicial.json') as file:
	tablero_inicial = json.load(file)
tablero_final = False
with open('tablero_final.json') as file:
	tablero_final = json.load(file)
coordenadas=[]
lado = 0 #0 izquierda 1 derecha
while tablero_inicial!=tablero_final:
	coordenadas=[]
	for x in tablero_inicial:
		if tablero_inicial!=tablero_final:
			if tablero_inicial[x] == 1:
				if x not in coordenadas:
					nuevo = grafo[x][lado]
					coordenadas.append(nuevo)
					tablero_inicial[x]=0
					tablero_inicial[nuevo] = 1
			if tablero_inicial[x] == -1:
				if x not in coordenadas:
					nuevo = grafo[x][lado]
					coordenadas.append(nuevo)
					tablero_inicial[x]=0
					tablero_inicial[nuevo] = -1	
	print("tablero actual:",tablero_inicial)
	print("---")
	

