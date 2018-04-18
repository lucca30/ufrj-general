import math
class vetor:
    def __init__(self, dimensions):
        self.dim = len(dimensions)
        self.dimensions = dimensions

    def norma(self):
        return math.sqrt(self.escalar(self))

    def normalizar(self):
        norm = self.norma()
        for i in range(dim):
            self.dimensions[i] /= norm

    def escalar(self, B):
        soma = 0
        if(self.dim!=B.dim):
            print ("ERROR")
            return
        for i in range(self.dim):
            soma += B.dimensions[i] * self.dimensions[i]
        return soma

    def cos(self, B):
        return (self.escalar(B) / (self.norma() * B.norma()))
