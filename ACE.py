from cPilha import *
from baralho import *
from listaEncadeada import *
# *******************************************************
# ***                                                 ***
# *******************************************************
class ACE:
    def __init__(self):
        
        self.pilha_embaralhada = cPilha(52)

        baralho = Baralho()
        baralho.embaralhar()

        # Adiciona as cartas embaralhadas à pilha
        for c in range(52):
            carta = baralho.getCarta(c)
            self.pilha_embaralhada.push(carta)
       
#*******************************************************
    
    def tirarTopo(self):
        if self.pilha_embaralhada.empty():
            return 
        else:
            return self.pilha_embaralhada.pop()

#*******************************************************
    def distribuirCartas(self, jogadores):
        num_cartas = self.pilha_embaralhada.size()
        num_jogadores = len(jogadores)

        # Distribuir as cartas entre os jogadores
        for i in range(num_cartas):
            jogador = jogadores[i % num_jogadores]  # Seleciona o jogador atual
            carta = self.tirarTopo()  # Tira a carta do topo do baralho
            jogador.receberCarta(carta)  # Entrega a carta ao jogador

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = ListaEncadeada()

    def receberCarta(self, carta):
        self.cartas.insereNo(carta)
    
    def __str__(self):
        cartas_str = ', '.join([str(carta.valor()) for carta in self.cartas])
        return f"{self.nome}: {cartas_str} cartas"

    def mostrarCartas(self):
        print(f"{self.nome}: {str(self.cartas)}") 

if __name__ == '__main__':
    ace = ACE()
    jogador1 = Jogador("Jogador 1")
    jogador2 = Jogador("Jogador 2")
    jogador3 = Jogador("jogador 3")
    jogadores = [jogador1, jogador2, jogador3]

    ace.distribuirCartas(jogadores)

    # Verificar as cartas de cada jogador
    for jogador in jogadores:
        jogador.mostrarCartas()
