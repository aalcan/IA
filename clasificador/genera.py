"""
En el comentario del archivo anterior, hice varias cosas, 
para poder sacar la matriz de probabilidades, 
ahora hay que hacer un programa que a partir de 10 tweets genere la misma 
matriz de probabilidades
sabiendo de ante mano cuales son los de stream

Sugiero esta estructura, para lo tweets

{
	"Tweets" : [
		{"Stream":true, "texto":"Vamos a darle a Among Us con famosos"},
		{"Stream":false, "texto":"El Fugitivo: La Historia en 1 Video"},
	]
}

y debe generar el  json compatible con el programa de clasificacion

"""
import re
import json

advervios = ["lejos", "cerca", "aquí", "allí", "allá", "acá", "así", "bien", "mal", "ayer", "mañana", "nunca", "hoy", "jamás", "siempre", "a veces", "quizás", "tal vez", "acaso",
"mucho", "poco", "bastante", "demasiado","sí", "también","no", "tampoco"]

articulos = ["el", "la", "los", "las", "un", "uno", "una", "unos", "unas"]

preposiciones =["a", "antes de", "dentro de", "desde", "desde hace", "después de", "durante", "en", "hasta", "por", "sobre", "tras", "a la derecha de", "a la izquierda de",
"al lado de", "alrededor de", "a través de", "cerca de", "contra", "debajo de", "delante de", "detrás de" ]


tweets = False
with open('tweets_json.json','r') as read_file:
	data = json.load(read_file)
	tweets = data['Tweets']

def fun(variable): 
	p = re.compile(r'\d+')
	x = p.findall(variable)
	if ((variable in advervios) or (variable in articulos) or (variable in preposiciones) or x): 
		return False
	else: 
		return True
# using filter function 

def listaPalabrasDicFrec(listaPalabras):
    frecuenciaPalab = [listaPalabras.count(p) for p in listaPalabras]
    return dict(list(zip(listaPalabras,frecuenciaPalab))) 

def ordenaDicFrec(dicfrec):
    aux = [(dicfrec[key], key) for key in dicfrec]
    aux.sort()
    aux.reverse()
    return aux


words_stream = []
words_not_stream = []
for tweet in tweets:
	#print(tweet['texto'])
	lista_palabras = tweet['texto'].split()
	filtered = filter(fun, lista_palabras)
	for x in filtered:
		if (tweet['Stream']):
			words_stream.append(x)
		else:
			words_not_stream.append(x)
frecuenciaPalab = listaPalabrasDicFrec(words_stream)	
frecuenciaPalabOrdenadas = ordenaDicFrec(frecuenciaPalab)
valor_maximo = frecuenciaPalabOrdenadas[0][0]
probabilidades=[]
valor=[]
data = {} 
data['Probabilidades'] = []
for x in frecuenciaPalabOrdenadas:
	prob = x[0]/valor_maximo
	data['Probabilidades'].append((x[1],prob))
	probabilidades.append(prob)
	valor.append(x[1])
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Frecuencias\n" + str(list(zip(probabilidades, valor))) + "\n")