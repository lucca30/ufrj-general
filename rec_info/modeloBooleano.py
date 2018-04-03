"""
Priorize executar em python 3

No bash:
    python3 -i modeloBooleano.py

No shell do python:

M=['O peã e o caval são pec de xadrez. O caval é o melhor do jog.', 'A jog envolv a torr, o peã e o rei.','O peã lac o boi','Caval de rodei!','Polic o jog no xadrez.']
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são']
q='xadrez peã caval torr'
separadores=[' ',',','.','!','?']
modeloBooleano(M, stopwords, q, separadores)

"""

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

def convert_to_bitmask(idx, incidencias, ndocs):
    bitmask = 0
    for i in range(ndocs):
        if(incidencias[i][idx]!=0):
            bitmask += 2**(ndocs-1-i)
    return bitmask

def modeloBooleano(M, stopwords, q, separadores):

    M = tokenizar(M, separadores, stopwords)
    q = tokenizar([q], separadores, stopwords)
    q = q[0]
    ndocs = len(M)
    (ntermos, termos) = count_termos(M)
    incidencias = [[0 for i in range(ntermos)] for j in range(ndocs)]
    for i in range(len(M)):
        for j in range(len(M[i])):
            incidencias[i][termos.index(M[i][j])]+=1


    for i in range(len(q)):
        if(i==0):
            bitmask = convert_to_bitmask(termos.index(q[i]), incidencias, ndocs)
        else:
            bitmask = bitmask & convert_to_bitmask(termos.index(q[i]), incidencias, ndocs)
    print("&: " + bin(bitmask))

    for i in range(len(q)):
        if(i==0):
            bitmask = convert_to_bitmask(termos.index(q[i]), incidencias, ndocs)
        else:
            bitmask = bitmask | convert_to_bitmask(termos.index(q[i]), incidencias, ndocs)
    print("|: " +bin(bitmask))
