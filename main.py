from cPilha import * 
from mao import *
from baralho import *
from ACE import * 
import random
#*****************************************************************************
#***                                                                       ***
#*****************************************************************************
def mico(num_jogadores):
    #cria o baralho
    baralho = ACE()
    jogadores = ListaEncadeada()
    #retira o Mico
    mico = baralho.tirarTopo()

    #cria jogadores
    for i in range(num_jogadores):
        nome_jogador = f'Jogador {i+1}'
        jogador = Jogador(nome_jogador)
        jogadores.insereNo(jogador)

    baralho.distribuirCartas(jogadores)


    for jogador in jogadores:
        jogador.mostrarCartas() 
    


    

mico(3)
