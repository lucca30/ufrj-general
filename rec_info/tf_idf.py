import math
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

def count_termos(M):
    temp = []
    for doc in M:
        for token in doc:
            if(token not in temp):
                temp.append(token)
    return len(temp), temp

def tf_idf(M, stopwords, q, separadores):
    M = tokenizar(M, separadores, stopwords)
    q = tokenizar([q], separadores, stopwords)
    ndocs = len(M)
    (ntermos, termos) = count_termos(M)
    incidencias = [[0 for i in range(ntermos)] for j in range(ndocs)]
    for i in range(len(M)):
        for j in range(len(M[i])):
            incidencias[i][termos.index(M[i][j])]+=1

    N = ndocs
    n = [0 for x in range(ntermos)]
    for i in range(ndocs):
        for j in range(ntermos):
            if(incidencias[i][j]>=1):
                n[j]+=1
    tf_idf = [[0 for i in range(ntermos)] for j in range(ndocs)]
    for i in range(ndocs):
        for j in range(ntermos):
            if(incidencias[i][j]>=1):
                tf_idf[i][j] = float((1 + incidencias[i][j])) * math.log(N/n[j], 2)
    print("TF_IDF dos documentos:")
    print(tf_idf)


    ndocs = len(q)
    (ntermos, termos) = count_termos(q)
    incidencias = [[0 for i in range(ntermos)] for j in range(ndocs)]

    for i in range(len(q)):
        for j in range(len(q[i])):
            incidencias[i][termos.index(q[i][j])]+=1

    tf_idf = [[0 for i in range(ntermos)] for j in range(ndocs)]
    for i in range(ndocs):
        for j in range(ntermos):
            if(incidencias[i][j]>=1):
                tf_idf[i][j] = float((1 + incidencias[i][j])) * math.log(N/n[j], 2)
    print("TF_IDF da consulta:")
    print(tf_idf)
