import tf_idf
import math
def modelo_BM25(ponderada_docs, ponderada_consulta, incidencias, n, k1, b):
    ndocs = len(incidencias)
    ntermos = len(n)
    # l = len do doc
    avg_doc_len = 0
    l = [0 for x in range(ndocs)]
    for i in range(ndocs):
        for j in incidencias[i]:
            l[i] += j
        avg_doc_len += l[i]
    avg_doc_len /= len(l)
    beta = [[0 for x in range(ntermos)] for y in range(ndocs)]
    for i in range(ndocs):
        for j in range(ntermos):
            beta[i][j] = ((k1+1)*ponderada_docs[i][j])/( k1*( (1-b) + b*(l[i]/avg_doc_len) ) + ponderada_docs[i][j] )

    rank = []
    for i in range(ndocs):
        resultado = 0
        for j in range(ntermos):
            if(ponderada_consulta[j]!=0):
                resultado += beta[i][j] * math.log( (ndocs-n[j]+0.5)/(n[j]+0.5) , 2)
        rank.append(resultado)
    return rank
M=['O peã e o caval são pec de xadrez. O caval é o melhor do jog.', 'A jog envolv a torr, o peã e o rei.','O peã lac o boi','Caval de rodei!','Polic o jog no xadrez.']
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são']
q='xadrez peã caval torr'
separadores=[' ',',','.','!','?']
(ponderada_docs, ponderada_consulta, incidencias, n) = tf_idf.tf(M, stopwords, q, separadores, True)
print(modelo_BM25(ponderada_docs, ponderada_consulta, incidencias, n, 1, 0.75))
