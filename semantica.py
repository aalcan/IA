import json
Conocimiento = False
with open('conocimientos.json','r') as read_file:
	data = json.load(read_file)
	Conocimiento = data['Conocimientos']
#print(Conocimiento)
###########################################################################
#Funciona solo si el proceso es igual para cada comparacion 
###########################################################################
def toBe(A,B,C,F):
	if not F:
		return False
	Elemento = [e for e in F if e[0] == A]
	if not Elemento:
		return False
	for x in Elemento:
		if B == x[1]:
			if C == x[2]:
				return True
			else:
				return toBe(x[2],B,C,F)
	

def esta(A,B,C):
	return toBe(A,B,C,Conocimiento)


def main():
	print("Bienvenido")
	print('Puedes consultar escribiendo esta("<animal>","<es, vive o tiene>","<Conocimiento>"")')
	print('Puedes salir presionando "q" o escribiendo quit()')
	Terminar = False
	while not Terminar:
		Leer = input("> ")
		if Leer == 'q':
			return
		Imprimir = eval(Leer)
		print(Imprimir)

if __name__ == '__main__':
	main()
