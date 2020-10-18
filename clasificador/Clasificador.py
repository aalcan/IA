"""
	Para este ejercicio voy a tomar 10 tweets 
	del influencer SoyFedelobo
	
	La idea es detectar cuando un tweet avisa que SoyFedelobo esta en
	stream
	Cada tweet debe tener al menos 3 palabras para ser evaluado
	
	El primero paso es crear la matriz de probabilidad, para eso vamos
	a analizar los 10 tweets.
	
	
	Tweet 0
	https://twitter.com/SoyFedelobo/status/1316442745507057665
	Texto:
		Que pedo wey
		
	Tweet 1
	https://twitter.com/SoyFedelobo/status/1316204032814440448
	Texto:
		Vamos a darle un ratito a terror en este Martes claro que sí
	
	Tweet 2
	https://twitter.com/SoyFedelobo/status/1315745560096370688
	Texto:
		Assassin's Creed Syndicate: La Historia en 1 Video 
		
	Tweet 3
	https://twitter.com/SoyFedelobo/status/1315468480901246976
	Texto:
		Vamos a seguirle al Bloodborne =)
		
	Tweet 4
	https://twitter.com/SoyFedelobo/status/1315435524870426624
	Texto:
		Chale seño ya le puse a mis tacos
		
	Tweet 5
	https://twitter.com/SoyFedelobo/status/1315121959269793793
	Texto:
		Lo mismo me va a pasar cuando haga un Top de los juegos que más me gustaron en 2020. Ni pedo.
	
	Tweet 6
	https://twitter.com/SoyFedelobo/status/1315006487559798784
	Texto:
		¡Nuevo Video! ROBOCOP: La Saga en 1 Video, vayan a ver esta historia de Cyborgs, empresas millonarias y gente idiota
	
	Tweet 7
	https://twitter.com/SoyFedelobo/status/1314776481831190528
	Texto:
		Vamos a darle a la nueva temporada de FALL GUYS
	
	Tweet 8
	https://twitter.com/SoyFedelobo/status/1314731760622727169
	Texto:
		Vamos a continuarle al Bloodborne, acompañenme a sufrir
		
	Tweet 9
	https://twitter.com/SoyFedelobo/status/1314379279468298242
	Texto:
		Vamos a seguirle al Sheep Raider
	
	Nuestro espacio muestral son esos 10 tweets de los cuales
	solo nos vamos a concentrar en sujetos, verbos y adjetivos, 
	adverbios, preposiciones, numeros, signos puntuacion y articulos 
	quedaran descartados.
	
	########################################################
	T0 => pedo,wey
	T1 => Vamos,darle,ratito,terror,Martes,claro
	T2 => Assassin's,Creed,Syndicate,Historia, Video 
	T3 => Vamos,seguirle,Bloodborne
	T4 => Chale,seño,puse,tacos
	T5 => mismo,va,pasar,haga,Top, juegos, gustaron,pedo.
	T6 => Nuevo,Video,ROBOCOP,Saga,Video, vayan, ver, historia,Cyborgs, empresas, millonarias,gente,idiota
	T7 => Vamos,darle,nueva,temporada,FALL,GUYS
	T8 => Vamos,continuarle,Bloodborne,acompañenme,sufrir
	T9 => Vamos,seguirle,Sheep,Raider
	########################################################
	
	De los tweets anteriores solo T1, T3, T7, T8, T9
	Son Streams,(lo que reduce nuestro espacio muestral aun mas)
	de estos, nos vamos a concentrar en las palabras 
	que manejan y obtenemos su probabilidad.
	
	
	Palabra		noAparece 	Aparece		total	P(Palabra)	P(¬Palabra)
	Vamos			0			5		5		1			0
	Bloodborne		3			2		5		0.4			0.6
	darle			3			2		5		0.4			0.6
	seguirle		3			2		5		0.4			0.6
	acompañenme		4			1		5		0.2			0.8
	claro			4			1		5		0.2			0.8
	continuarle		4			1		5		0.2			0.8
	FALL			4			1		5		0.2			0.8
	GUYS			4			1		5		0.2			0.8
	Martes			4			1		5		0.2			0.8
	nueva			4			1		5		0.2			0.8
	Raider			4			1		5		0.2			0.8
	ratito			4			1		5		0.2			0.8
	Sheep			4			1		5		0.2			0.8
	sufrir			4			1		5		0.2			0.8
	temporada		4			1		5		0.2			0.8
	terror			4			1		5		0.2			0.8
	
	Lo que nos importa es la P(Palabra) con la cual realizaremos el json
	{
		Probabilidades: [
			["Vamos","1"],
			["Bloodborne","0.4"],
			["darle","0.4"],
			["seguirle","0.4"],
			["acompañenme","0.2"],
			["claro","0.2"],
			["continuarle","0.2"],
			["FALL","0.2"],
			["GUYS","0.2"],
			["Martes","0.2"],
			["nueva","0.2"],
			["Raider","0.2"],
			["ratito","0.2"],
			["Sheep","0.2"],
			["sufrir","0.2"],
			["temporada","0.2"],
			["terror","0.2"]
		]
	}
	
	//////////////////////////////////////////////////////////////
	Ahora que ya tenemos el json es hora de plantear el funcionamiento 
	básico del clasificador
	
	1) El analizador debe abrir un archivo de texto llamado 
		tweet.txt donde estara un tweet a analizar
	2) Con su base de conocimientos en formato json (base.json)
		buscara cada palabra (token) del json en el texto de tweet.txt
	3) llevara un registro en una pila, (o algo que se comporte como una) 
		de cada palabra y probabilidad según aparezcan en el texto
	4) Obtendra el promedio de las probabilidades y si dicho promedio
		supera el 55 % debera de imprimir "Stream" en caso contrario
		"No es Stream"
		
	Ejemplo:
	
	###	tweet.txt ###
	Vamos a darle al among us
	
	#######################################
	Al comparar los tokens del json con el texto
	encontrara dos ocurrencias: [[Vamos,1], [darle,0.4]]
	
	Sacamos el promedio de las probabilidades
	1.0 + 0.4 = 1.4
	1.4 / 2 = 0.7
	
	Como 0.7 es superior a 0.55
	Entonces el clasificador debera imprimir
	
	"Stream"
	
	

"""
import json
Probabilidades = False
with open('base.json','r') as read_file:
	data = json.load(read_file)
	Probabilidades = data['Probabilidades']

#print(Probabilidades)
archivo = open('tweet.txt', 'r')
contenido = archivo.read()
#print(contenido)

def getData(data):
	concidencias = []
	for word in data:
		for prob in Probabilidades:
			if prob[0] == word:concidencias.append(prob)
	return concidencias

def averageOfProb(concidencias):
	av_prob = 0.0
	for prob in concidencias: av_prob = av_prob + float(prob[1])
	return av_prob

def isStrem(P):
	if P > 0.55:
		return "Stream"
	else:
		return "No es Stream"

data  = getData(contenido.split())
P = averageOfProb(data)
print(isStrem(P))
#print(isStrem(av_prob))
archivo.close()




