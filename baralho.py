import random 
from listaEncadeada import * 
#*****************************************************************************
#***                                                                       ***
#*****************************************************************************
class Carta:

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe 
#*****************************************************************************

    def __str__(self):
        return f'{self.valor} de {self.naipe}'

#*****************************************************************************
#***                                                                       ***
#*****************************************************************************
class Baralho:

    def __init__(self):
        self.cartas = ListaEncadeada() 
        self._tamanho = 0 
        naipes = ['Paus', 'Copas', 'Espadas', 'Ouros']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

        for i in range(4):
            for j in range(13):
                carta = Carta(valores[j], naipes[i])
                self.cartas.insereNo(carta) 
                self._tamanho += 1 

#*****************************************************************************
    def mostrarBaralho(self):
        atual = self.cartas.getInicio()
        while atual is not None:
            print(atual.getDado())
            atual = atual.getProx()
 
#*****************************************************************************
    def tamanho(self):
        return self._tamanho 

#*****************************************************************************
    def cartaAleatoria(self):
        if self._tamanho == 0:
            return None

        indice = random.randint(0, 51)
        atual = self.cartas.getInicio()
        for _ in range(indice):
            atual = atual.getProx()

        return atual.getDado()
#*****************************************************************************  
    def vazio(self):
        return self._tamanho == 0

#*****************************************************************************   
    def embaralhar(self):
    # Obter todos os elementos do baralho
        elementos = []
        atual = self.cartas.getInicio()
        while atual is not None:
            elementos.append(atual.getDado())
            atual = atual.getProx()

        # Embaralhar a lista de elementos
        shuffle(elementos)

        # Atualizar a lista encadeada com os elementos embaralhados
        self.cartas = ListaEncadeada()
        for elemento in elementos:
            self.cartas.insereNo(elemento)

        return self

#*****************************************************************************   
    def getCarta(self, posição):
        return self.cartas[posição]
    
#*****************************************************************************   
        
if __name__ == '__main__':
    baralho = Baralho() 
    baralho.mostrarBaralho()

    print('*****************************')
   
    
    baralho_embaralhado = baralho.embaralhar()
    baralho_embaralhado.mostrarBaralho()
    
    print("***************")
    
    a = baralho_embaralhado.getCarta(51)
    
    print(a)
