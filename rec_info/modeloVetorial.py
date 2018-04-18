import tf_idf
import vetor

def modelo_vetorial(ponderada_docs, ponderada_consulta):
    vetores_doc = []
    for i in ponderada_docs:
        vetores_doc.append(vetor.vetor(i))
    consulta = vetor.vetor(ponderada_consulta)
    rank = []
    for i in vetores_doc:
        rank.append(i.cos(consulta))
    return rank

M=['O peã e o caval são pec de xadrez. O caval é o melhor do jog.', 'A jog envolv a torr, o peã e o rei.','O peã lac o boi','Caval de rodei!','Polic o jog no xadrez.']
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são']
q='xadrez peã caval torr'
separadores=[' ',',','.','!','?']
(ponderada_docs, ponderada_consulta) = tf_idf.tf_idf(M, stopwords, q, separadores)
print(modelo_vetorial(ponderada_docs, ponderada_consulta))
