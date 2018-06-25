import math
classificados = {}
contador_classificados = []
proximo_classificar = -1

def SampleAndUpdateStatistics(A, h, s, UCB, LCB, confidence, PP, T):
    global classificados, contador_classificados, proximo_classificar
    if(len(contador_classificados) == 0):
        contador_classificados = [0 for i in range(len(PP))]
    
    if( proximo_classificar == -1 ):
        proximo_classificar = 0
    
    #------BUG---------
    item_p_classificar = 0    
    #------------------
    for i in PP[proximo_classificar]:
        if(i not in classificados):
            item_p_classificar = i
            break
    
    classificados[item_p_classificar] = oraculo(item_p_classificar)
    for i in range(len(PP)):
        if(item_p_classificar in PP[i]):
            contador_classificados[i] += 1

    menos_classificado = -1
    for i in A:
        menos_classificado = min(menos_classificado, contador_classificados[i])
        if(item_p_classificar not in PP[i]):
            continue
        
        s[i] += 1
        if(classificados[item_p_classificar]):
            h[i] += 1
        P_i = float(h[i])/float(s[i])
        U_i = math.sqrt( float(math.log( (2.0*len(PP)*T)/confidence ))/ (2.0*s[i]) )
        #print(P_i, U_i, UCB[i], LCB[i])
        LCB[i] = max(LCB[i],P_i-U_i)
        UCB[i] = min(UCB[i], P_i+U_i)
        #print(P_i, U_i, UCB[i], LCB[i], "__")
    
    
    for i in A:
        if(contador_classificados[i] == menos_classificado):
            proximo_classificar = i
            break

