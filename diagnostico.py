Ls=[1,2,3,1,2,3]
def piedraTijera (L):
	if len(L)==1:
		print(L[0])
		return []
	if len(L)>1:
		print(L)
		print(nToText(L[0]),"vs",nToText(L[1]))
		R = quienGana(L[0],L[1])
		if(R!=4):
			L[1] = R
			print("Ganador:",nToText(L[1]))
			return piedraTijera(L[1:])
		else:
			return []
	else:
		return piedraTijera(L[1:])

"""
Pierdra = 1
Papel = 2
Tijeras = 3"""
def quienGana(op1,op2):
	if(op1<=3 and op1 >=0 and op2<=3 and op2 >=0):
		if (op1 == op2):
			return 0
		if(op1==1):
			if (op2==2):
				return op2
			if (op2==3):
				return op1
		if(op1==2):
			if (op2==1):
				return op1
			if (op2==3):
				return op2
		if(op1==3):
			if (op2==1):
				return op2
			if (op2==2):
				return op1
		if(op1==0):
			return op2
	else:
		print("Op no valida")
		return 4


def nToText(N):
	if(N==1):
		return "Piedra"
	if(N==2):
		return "Papel"
	if(N==3):
		return "Tijera"
	if(N==0):
		return "Empate"

print(piedraTijera(Ls))