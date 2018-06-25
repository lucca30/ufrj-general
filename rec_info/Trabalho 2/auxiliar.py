def precisao(relevantes, recuperados):
    intersecao = [val for val in recuperados if val in relevantes]
    return float( len(intersecao)/len(recuperados) )

def revocacao(relevantes, recuperados):
    intersecao = [val for val in recuperados if val in relevantes]
    return float( len(intersecao)/len(relevantes) )
