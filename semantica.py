import json
cadena_json = json.load(open('conocimientos.json'))
print(cadena_json['Conocimientos']);
###########################################################################
#Funciona solo si el proceso es igual para cada comparacion 
###########################################################################
def toBe(A,B,C, F):
    if not F:
        return False
    D = len(F)
    i = 0
    while i < D:
        if F[i][0] == A:
            if F[i][1] == B:
                if F[i][2] == C:
                    return True
                else:
                    i = i + 1
            else:
                #A = C[i][1]
                i = i + 1
        else:
            i = i + 1
            if  i == D:
                return False


def toBeEs(A,B,C, F):
    if not F:
        return False
    D = len(F)
    i = 0
    while i < D:
        if F[i][0] == A:
            if F[i][1] == B:
                if F[i][2] == C:
                    return True
                else:
                    A = F[i][2]
                    i = i + 1
            else:
                #A = C[i][1]
                i = i + 1
        else:
            i = i + 1
            if  i == D:
                return False


def recorrer(A,B,C, F):
    if B == "es"  :
         return toBeEs(A,B,C, F)
    else:
        return toBe(A,B,C,F)

print(recorrer("gato","vive","agua",cadena_json['Conocimientos']))
