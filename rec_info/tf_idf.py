import math
import filtro

def print_tf_idf(Mtf_idf, termos):
    return
    temp = "      "
    for i in termos:
        temp +=  str(i + "      ")[:9]
    print(temp)

    for i in range(len(Mtf_idf)):
        temp = "doc" +str(i)[:3] +  ": "
        for j in range(len(Mtf_idf[i])):
            temp += str(str(Mtf_idf[i][j])[:5] + "               "  )[:9]
        print(temp)

def tf_idf(M, stopwords, q, separadores, valores_extras=False):
    (incidencias, termos, M, q) = filtro.incidencias_termos(M, stopwords, q, separadores)

    N = len(M)
    n = [0 for i in range(len(termos))]


    for i in range(len(M)):
        for j in range(len(termos)):
            if(incidencias[i][j]>=1):
                n[j]+=1

    Mtf_idf = [[0 for i in range(len(termos))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(termos)):
            if(incidencias[i][j]>=1):
                Mtf_idf[i][j] = float((1 + math.log(incidencias[i][j],2))) * math.log(N/n[j], 2)
    #print("TF_IDF dos documentos:")

    print_tf_idf(Mtf_idf, termos)
    ret1 = Mtf_idf

    incidencias_consulta = [0 for i in range(len(termos))]
    for i in range(len(q)):
        incidencias_consulta[termos.index(q[i])]+=1

    Mtf_idf = [0 for i in range(len(termos))]
    for i in range(len(termos)):
        if(incidencias_consulta[i]>=1):
            Mtf_idf[i] = float((1 + math.log(incidencias_consulta[i],2))) * math.log(N/n[i], 2)
    #print("TF_IDF da consulta:")
    print_tf_idf([Mtf_idf], termos)
    ret2 = Mtf_idf
    if(valores_extras):
        return (ret1, ret2, incidencias, n)
    return (ret1, ret2)

def tf(M, stopwords, q, separadores, valores_extras=False):
    (incidencias, termos, M, q) = filtro.incidencias_termos(M, stopwords, q, separadores)

    N = len(M)
    n = [0 for i in range(len(termos))]


    for i in range(len(M)):
        for j in range(len(termos)):
            if(incidencias[i][j]>=1):
                n[j]+=1

    Mtf_idf = [[0 for i in range(len(termos))] for j in range(len(M))]
    for i in range(len(M)):
        for j in range(len(termos)):
            if(incidencias[i][j]>=1):
                Mtf_idf[i][j] = float((1 + math.log(incidencias[i][j],2)))
    #print("TF dos documentos:")

    print_tf_idf(Mtf_idf, termos)
    ret1 = Mtf_idf

    incidencias_consulta = [0 for i in range(len(termos))]
    for i in range(len(q)):
        incidencias_consulta[termos.index(q[i])]+=1

    Mtf_idf = [0 for i in range(len(termos))]
    for i in range(len(termos)):
        if(incidencias_consulta[i]>=1):
            Mtf_idf[i] = float((1 + math.log(incidencias_consulta[i],2)))
    #print("TF da consulta:")
    print_tf_idf([Mtf_idf], termos)
    ret2 = Mtf_idf
    if(valores_extras):
        return (ret1, ret2, incidencias, n)
    return (ret1, ret2)
M=['O peã e o caval são pec de xadrez. O caval é o melhor do jog.',
'A jog envolv a torr, o peã e o rei.',
'O peã lac o boi',
'Caval de rodei!',
'Polic o jog no xadrez.']
stopwords=['a', 'o', 'e', 'é', 'de', 'do', 'no', 'são']
q='xadrez peã caval torr'
separadores=[' ',',','.','!','?']
tf_idf(M, stopwords, q, separadores)
