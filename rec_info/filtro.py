def tokenizar(strings, separadores, stopwords):
    strings = [i.lower() for i in strings]
    temp = []
    for i in range(len(strings)):
        temp.append([])
        str_ = ''
        for char in strings[i]:
            if(char in separadores):
                if(len(str_)>0 and (str_ not in stopwords)):
                    temp[i].append(str_)
                str_= ''
            else:
                str_+=char
        if(len(str_)>0 and (str_ not in stopwords)):
            temp[i].append(str_)

    return temp

#retorna um array com todos os tokens do conjunto de documentos
#na matriz de incidencias, a posiçao do termo é relativa a posiçao neste array
def map_termos(M):
    temp = []
    for doc in M:
        for token in doc:
            if(token not in temp):
                temp.append(token)
    temp.sort()
    return len(temp), temp


def produzir_incidencias(M, ndocs, termos, ntermos):
    incidencias = [[0 for i in range(ntermos)] for j in range(ndocs)]

    for i in range(len(M)):
        for j in range(len(M[i])):
            incidencias[i][termos.index(M[i][j])]+=1
    return incidencias

def incidencias_termos(M, stopwords, q, separadores):
    M = tokenizar(M, separadores, stopwords)
    q = tokenizar([q], separadores, stopwords)
    q = q[0]
    ndocs = len(M)
    (ntermos, termos) = map_termos(M)
    incidencias = produzir_incidencias(M, ndocs, termos, ntermos)
    return incidencias, termos, M, q
