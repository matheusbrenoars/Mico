class Node:
    def __init__(self, triangulo):
        self.triangulo = triangulo
        self._esq = None
        self._dir = None
        self._pai = None
        self._direcao = None 
        
    def getDado(self):
       return self.triangulo
    

    def getFilhoEsq(self):
        return self._esq

    def setFilhoEsq(self, triangulo):
        self._esq = triangulo

    def getFilhoDir(self):
        return self._dir

    def setFilhoDir(self, triangulo):
        self._dir = triangulo

    def __str__(self):
        outStr = ""
        outStr += "+=================+======+=================+\n"
        outStr += f"|   {self.triangulo}   |      |                 |\n"
        outStr += "+=================+======+=================+\n"
        return outStr

    def setPai(self, pai):
        self._pai = pai

    def getPai(self):
        return self._pai


    # Verificar as cartas de cada jogador
    for jogador in jogadores:
        jogador.mostrarCartas()
