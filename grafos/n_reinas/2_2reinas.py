import numpy as np
tablero = np.zeros((4, 4))
posiciones = np.zeros((4, 4))
coordenadas = []
reinas = 4.0
def imprimirTablero():
	for linea in tablero:
		print(linea)

def rellenarVertical(x,y):
	i=0
	for fila in tablero[x]:
		if tablero[x][i]!=1:
			tablero[x][i]=2
		i+=1
	tablero[x][y]=1
def rellenarHorizontal(x,y):
	i=0
	for fila in tablero:
		if tablero[i][y]!=1:
			tablero[i][y]=2
		i+=1
	tablero[x][y]=1
		

def rellenarDiagonal(x,y):
	for i in range(1,4):
		try:
			if x>0 and y>0:
				if tablero[x-i][y-i]!=1:
					(tablero[x-i][y-i])=2
				if (tablero[x+i][y-i])!=1:
					(tablero[x-i][y-i])=2
				if (tablero[x-i][y+i])!=1:
					(tablero[x-i][y-i])=2
			else:
				if (tablero[x+i][y+i]) !=1:
					(tablero[x+i][y+i])=2
				if (tablero[x-i][y+i])!=1:
					(tablero[x+i][y+i])=2
		except Exception as e:
			 overflow=e

def isSafe(board, row, col): 
  
    # Check this row on left side 
    for i in range(col):
    	if board[row][i] == 1:
    		print("0",board[row][i])
    		return False

  
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
    	if i!=row and j!=col:
	    	if board[i][j] == 1: 
	    		print("1",board[i][j],i,j)
	    		return False
  
    # Check lower diagonal on left side 
    for i, j in zip(range(row, 4, 1), range(col, -1, -1)): 
    	if i!=row and j!=col:
    		if board[i][j] == 1:
    			return False
    return True
	
def colocarReina(x,y):
	rellenarHorizontal(x,y)
	rellenarVertical(x,y)
	rellenarDiagonal(x,y)

def recorrido():
	global reinas
	for i in range(0,4):
		for j in range(0,4):
			if tablero[i][j]==0:
				colocarReina(i,j)
				reinas=reinas-1
	
	if reinas>0:
		return False
	else: 
		R = True
		for i in range(0,4):
			for j in range(0,4):
				if(tablero[i][j]==1):
					r = isSafe(tablero,i,j)
					R = r and R
		if R:
			print("solucion encontrada")
			imprimirTablero()
			print("----")
		return R

def nuevaReina():
	global reinas
	for i in range(0,4):
		for j in range(0,4):
			if(posiciones[j][i]==0):
				colocarReina(j,i)
				reinas-=1
				posiciones[j][i]=1
				a = recorrido()
				if a==False:
					limpiarTablero()
					reinas=4
				else:
					coordenadas.append([j,i])
					limpiarTablero()
					reinas=4
					#imprimirTablero()

def limpiarTablero():
	for i in range(0,4):
		for j in range(0,4):
			tablero[j][i]=0



nuevaReina()
#limpiarTablero()
#imprimirTablero()



