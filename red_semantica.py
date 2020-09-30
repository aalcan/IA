
tiene = [
        ("tortuga","garras"),
        ("tortuga","Proteccion queratina"),
        ("gallo","garras"),
        ("gallo","Proteccion queratina"),
        ("cocodrilo","garras"),
        ("cocodrilo","Proteccion queratina"),
        ("iguana","garras"),
        ("iguana","Proteccion queratina"),
        ("gato","g. mamarias"),
        ("gato","pelo"),
        ("gato","garras"),
        ("ballena","g. mamarias"),
        ("ballena","pelo"),
        ("oso","g. mamarias"),
        ("oso","pelo"),
        ("oso","garras"),
        ("delfin","g. mamarias")
        ]
vive = [
        ("tortuga","agua"),
        ("gallo","tierra"),
        ("cocodrilo","agua"),
        ("iguana","tierra"),
        ("gato","tierra"),
        ("ballena","agua"),
        ("oso","tierra"),
        ("delfin","agua")
       ]

es = [
        ("tortuga","sauropsida"),
        ("gallo","sauropsida"),
        ("cocodrilo","sauropsida"),
        ("iguana","sauropsida"),
        ("gato","mammalia"),
        ("ballena","mammalia"),
        ("oso","mammalia"),
        ("delfin","mammalia"),
        ("mammalia","viviparo"),
        ("viviparo","tetrapodo"),
        ("sauropsida","oviparo"),
        ("oviparo","tetrapodo"),
        ("tetrapodo","vertebrado")
       ]




###########################################################################
#Funciona solo si el proceso es igual para cada comparacion 
###########################################################################
def toBe(A,B,C, F):
    if not C:
        return False
    D = len(C)
    i = 0
    while i < D:
        if F == 1:
            if C[i][0] == A:
                if C[i][1] == B:
                    return True
                else:
                    A = C[i][1]
        if C[i][0] == A:
            if C[i][1] == B:
                return True
        i = i + 1
    else:
        return False

def dato1(A):
    def dato2(B):
        def array_list(C):
            def doble_recorrido(F = 0):
                return toBe(A,B,C,F)
            return doble_recorrido
        return array_list
    return dato2

print(dato1("gato")("pelo")(tiene)())
print(dato1("tortuga")("vertebrado")(es)(1))
print(dato1("tortuga")("oviparo")(es)(1))
print(dato1("gato")("garras")(tiene)())
print(dato1("ballena")("agua")(vive)())
print(dato1("gato")("tetrapodo")(es)(1))
print(dato1("oso")("pelo")(tiene)())
