import modeloVetorial
import modeloBM25
relevantes = [1, 2]

def convert_doc_order(result):
    temp = []
    for i in range(len(result)):
        if(result[i]>0):
            temp.append( (result[i], i+1) )
    temp.sort()
    return [x[1] for x in temp[::-1]]


def revocacao(relevantes, recuperados, N):
    recuperados = recuperados[:N]
    intersecao = [val for val in recuperados if val in relevantes]
    return float( len(intersecao)/len(relevantes) )

def precisao(relevantes, recuperados, N):
    recuperados = recuperados[:N]
    intersecao = [val for val in recuperados if val in relevantes]
    return float( len(intersecao)/len(recuperados) )


def F1(relevantes, recuperados, N):
    pj = precisao(relevantes, recuperados, N)
    rj = revocacao(relevantes, recuperados, N)
    return float(( 2 * pj * rj )/(pj+rj))

def getRecallsPrecisions(modelo, relevantes):
    idx_recs = [x for x in range(len(modelo)) if(modelo[x] in relevantes) ]
    rec_prec = []
    for i in range(len(idx_recs)):
        revoc = revocacao(relevantes, modelo, idx_recs[i]+1)
        prec =  precisao(relevantes, modelo, idx_recs[i]+1)
        rec_prec.append((revoc, prec))
    return rec_prec
BM25 = convert_doc_order(modeloBM25.getConsultapadrao())
Vetorial = convert_doc_order(modeloVetorial.getConsultapadrao())

print("-------------------Revocação e Precisão-------------------")

print("Modelo BM25:")
print(" - Revocação: ", revocacao(relevantes, BM25, len(BM25)))
print(" - Precisão: ", precisao(relevantes, BM25, len(BM25)))

print("Modelo Vetorial:")
print(" - Revocação: ", revocacao(relevantes, Vetorial, len(Vetorial)))
print(" - Precisão: ", precisao(relevantes, Vetorial, len(Vetorial)))
print("\n")


print("-------------------------Medida F1----------------------")
print("Modelo BM25:")
print(" - F1: ", F1(relevantes, BM25, len(BM25)))

print("Modelo Vetorial:")
print(" - F1: ", F1(relevantes, Vetorial, len(Vetorial)))
print("\n")


print("---Revocação e Precisão para cada documento relevante----")
print("Modelo BM25:")
idx_recs = [x for x in range(len(BM25)) if(BM25[x] in relevantes) ]
for i in range(len(idx_recs)):
    print(" - ", str(i+1), "º doc Recuperado:")
    print("     Revocação:", revocacao(relevantes, BM25, idx_recs[i]+1) )
    print("     Precisão:", precisao(relevantes, BM25, idx_recs[i]+1))
print("Modelo Vetorial:")
idx_recs = [x for x in range(len(Vetorial)) if(Vetorial[x] in relevantes) ]
for i in range(len(idx_recs)):
    print(" - ", str(i+1), "º doc Recuperado:")
    print("     Revocação:", revocacao(relevantes, Vetorial, idx_recs[i]+1) )
    print("     Precisão:", precisao(relevantes, Vetorial, idx_recs[i]+1))
print("\n")

print("------------Precisão Interpolada 11 niveis--------------")
rec_prec = getRecallsPrecisions(BM25, relevantes)
rang = [x/10 for x in range(11)]
print("BM25: ")
print("Revocação  |  Precisão")
for i in rang:
    max_prec = 0
    for j in rec_prec:
        if(j[0]>=i):
            max_prec = max(max_prec, j[1])
    print("  ",str(i),"   ", "|   ",str(max_prec)[:3] )

rec_prec = getRecallsPrecisions(Vetorial, relevantes)
rang = [x/10 for x in range(11)]
print("Vetorial: ")
print("Revocação  |  Precisão")
for i in rang:
    max_prec = 0
    for j in rec_prec:
        if(j[0]>=i):
            max_prec = max(max_prec, j[1])
    print("  ",str(i),"   ", "|   ",str(max_prec)[:3] )
