from cNo import *
from random import shuffle 
#*****************************************************************************
#***                                                                       ***
#*****************************************************************************
class ListaEncadeada:

    def __init__(self):
        self._inicio = None
        self.tamanho = 0 
#*****************************************************************************
    def insereNo(self, n):
        if self._inicio:
            pointer = self._inicio
            while (pointer.getProx()):
                pointer = pointer.getProx()
            pointer.setProx(cNo(n))
        
        else:
            self._inicio= cNo(n)
        
        self.tamanho += 1
#*****************************************************************************
    def buscaDado(self, n):
        pointer = self._inicio
        i = 0
        while (pointer):
            if pointer.getDado() == n:
                return n, i 
            pointer = pointer.getProx()
            i += 1 
#*****************************************************************************   
    def insertInicio(self, n):
      
      if self._inicio: 
        pointer = self._inicio
      
      
        for i in range(self.tamanho - 1):
            pointer = pointer.getProx()

        novoNo = cNo(n)
        novoNo.setProx(self._inicio)
        self._inicio = novoNo


        self.tamanho += 1
       
      else:
        self._inicio= cNo(n)
        
        self.tamanho += 1
#*****************************************************************************
    def __len__(self):
        return self.tamanho

#*****************************************************************************   
    def removeNo(self, n):
        if self._inicio is None:
            return False
        
        elif self._inicio.getDado() == n:
            self._inicio = self._inicio.getProx()
            self.tamanho -= 1 
            return True 
        else:
            ant = self._inicio
            pointer = self._inicio.getProx()
            while (pointer):
                if pointer.getDado() == n:
                    ant.setProx(pointer.getProx())
                    pointer.setProx(None)
                    self.tamanho -= 1
                    return True
                ant = pointer
                pointer = pointer.getProx() 

#*****************************************************************************
    def __str__(self):
        if self._inicio is None:
            return "Lista vazia."
        
        pointer = self._inicio
        lista_str = ""

        while pointer:
            lista_str += str(pointer.getDado()) + " "
            pointer = pointer.getProx()

        return lista_str
    
#*****************************************************************************
    def getInicio(self):
        return self._inicio
    
#*****************************************************************************
    def _getnode(self, index):
        pointer = self._inicio
        for i in range(index):
            if pointer:
                pointer = pointer.getProx()
            else:
                return False 
        return pointer
    
#*****************************************************************************
    def __getitem__(self, index):
        
        pointer = self._getnode(index)
        if pointer:
            return pointer.getDado()
        else:
            raise IndexError("list index out of range")
        
#*****************************************************************************
    def __setitem__(self, index, elem):
        
        pointer = self._getnode(index)
        if pointer:
            pointer.setDado = elem
        else:
            raise IndexError("list index out of range")
    
#*****************************************************************************   

if __name__ == '__main__':

    lista = ListaEncadeada()

    for i in range(10):
        lista.insereNo(i)

    print(str(lista))

    lista.removeNo(3)
    lista.removeNo(9)

    print(str(lista))

    lista.insertInicio(19)

    print(str(lista))

    print(lista[0] )

    print(lista[1])
