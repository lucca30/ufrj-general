


#PP[i] representa o conjunto de preditos como positivo pelo classificador i
#confidence: o nível de confiança que quero garantir de que a escolha está correta
#PT (Precision Threshold): condição mínimade precisão necessária
#PS (Precision Slack): uma certa folga para a precisão, criando assim a categoria de classificadores aceitáveis
#Slack : uma certa folga para o alcance que o algoritmo alcança
#T (Oracle Budget): quantas vezes o oráculo pode ser consultado
base_dados = []
def maxRecallSelector(PP, confidence, PT, PS, Slack, T, bd):
    infinity = 9999999999999
    global base_dados
    base_dados = []
    A = [i for i in range(len(PP))]
    PG = [i for i in range(len(PP))]
    RQ = []
    h = [0 for i in range(len(PP))]
    s = [0 for i in range(len(PP))]
    S = 0
    LCB = [0 for i in range(len(PP))]
    UCB = [1 for i in range(len(PP))]
    while(len(PG)!=0 and len(RQ)==0):
        S+=1
        PA = []
        PG = []
        KA = []
        KG = []
        UBGR = [0 for i in range(len(PP))]
        LBGR = 0
        if(S>T):
            return "alpha"
        #print("Chamou")
        SampleAndUpdateStatistics(A, h, s, UCB, LCB, confidence, PP, T)
        #print(UCB, LCB)
        for i in range(len(PP)):
            if(UCB[i]>PT-PS):
                PA.append(i)
            if(UCB[i]>PT):
                PG.append(i)
            if(LCB[i]>PT-PS):
                KA.append(i)
            if(LCB[i]>PT):
                KG.append(i)
        
        for i in range(len(PP)):
            if(len(PG)==0 or ( (i in PG) and len(PG)==1 )):
                UBGR[i] = -infinity
            else:
                maximo = -infinity
                for j in range(len(PP)):
                    if(j==i):
                        continue
                    maximo = max(maximo, UCB[j]*len(PP[j]))
                UBGR[i] = maximo
        RQ = []
        for idx in KA:
            i = KA[idx]
            if(LCB[i]*len(PP[i]) >= (1-Slack) * UBGR[i] ):
                RQ.append(i)
        if(len(KG)==0):
            LBGR = -infinity
        else:
            maximo = -infinity
            for j in KG:
                maximo = max(maximo, LCB[j]*len(PP[j]))
            LBGR = maximo
            
        RD = []
            
        for i in range(len(PP)):
            if(max((1-Slack) * UCB[i]*len(PP[i]), LCB[i]*len(PP[i]) ) < LBGR):
                RD.append(i)
        A = []
        for i in PG:
            if(i not in RD):
                A.append(i)
    if(len(RQ)>1):
        melhores = [(UBGR[i], i) for i in range(len(RQ))]
        return melhores[-1][1]
    elif(len(KA)>0):
        melhores = [(UBGR[i], i) for i in range(len(KA))]
        return melhores[-1][1]
    else:
        return "alpha_"

