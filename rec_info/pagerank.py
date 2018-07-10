rede = [ [0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 0, 0],
         [0, 0, 1, 0],
       ]
T = len(rede)
PR = [float(1.0/T) for x in range(T)]

TH = 0.0001
beta = 0.8
L = []
for i in rede:
    soma = 0
    for j in i:
        soma +=j
    L.append(soma)

while(True):
    stop = 0
    antigoPR = [x for x in PR]
    for i in range(T):
        somatorio = 0
        for j in range(T):
            if(rede[j][i]==1):
                somatorio+= float(antigoPR[j])/float(L[j])
        PR[i] = float((1-beta))/float(T) + beta * somatorio
        if(abs(PR[i] - antigoPR[i]) < TH ):
            stop+=1
    if(stop==T):
        break

print(PR)
