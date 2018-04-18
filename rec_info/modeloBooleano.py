import filtro
"""
Priorize executar em python 3

No bash:
    python3 modeloBooleano.py

"""

def convert_to_bitmask(idx, incidencias, ndocs):
    bitmask = 0
    for i in range(ndocs):
        if(incidencias[i][idx]!=0):
            bitmask += 2**(ndocs-1-i)
    return bitmask

def modeloBooleano(M, stopwords, q, separadores):
    (incidencias, termos, M, q) = filtro.incidencias_termos(M, stopwords, q, separadores)

    for i in range(len(q)):
        if(i==0):
            bitmask = convert_to_bitmask(termos.index(q[i]), incidencias, len(M))
        else:
            bitmask = bitmask & convert_to_bitmask(termos.index(q[i]), incidencias, len(M))
    print("&: " + bin(bitmask))

    for i in range(len(q)):
        if(i==0):
            bitmask = convert_to_bitmask(termos.index(q[i]), incidencias, len(M))
        else:
            bitmask = bitmask | convert_to_bitmask(termos.index(q[i]), incidencias, len(M))
    print("|: " +bin(bitmask))

M=['O peã e o caval são pec de xadrez. O caval é o melhor do jog.',
'A jog envolv a torr, o peã e o rei.',
'O peã lac o boi',
'Caval de rodei!',
'Polic o jog no xadrez.']
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são']
q='rei peã'
separadores=[' ',',','.','!','?']
modeloBooleano(M, stopwords, q, separadores)
