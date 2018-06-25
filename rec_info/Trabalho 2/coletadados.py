f = open("./dados/relevantes.txt")
linhas = f.readlines()
f.close()
separados = [linha.split(" ") for linha in linhas]
print(separados[1])

relevantes = [{} for x in range(11)]

for i in separados:
    relevantes[int(i[0])][i[2]] = 1
    
vals = []
candidatos = []
consulta = '1'
for i in range(3):
    
    f = open("./dados/"+str(i+1)+".txt")
    linhas = f.readlines()
    f.close()
    separados = [linha.split(" ") for linha in linhas]
    candidato = []
    for j in separados:
        if(j[0]==consulta):
            candidato.append(j[2])
    candidatos.append(candidato)
    #[i[2] for i in separados[:100]]
    #relevantes[1]

