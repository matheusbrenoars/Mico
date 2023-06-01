Max_pilha = 200

class cPilha:

    def __init__(self, n):
        self.pilha = [0]*n
        self.maxElem = n 
        self.topo = 0 

#*****************************************************************************
    def push(self, dado):
        if self.full():
            return "pilha  cheia"
        self.pilha[self.topo] = dado 
        self.topo += 1

#*****************************************************************************
    def pop(self):
        if self.empty():
            return "Pilha já está vazia"
        
        self.topo -= 1
        return self.pilha[self.topo] 
    
#*****************************************************************************   
    def size(self):
        return self.topo 

#*****************************************************************************   
    def full(self):
        return self.topo == Max_pilha 

#*****************************************************************************
    
    def empty(self):
        return self.topo == 0
    
#*****************************************************************************  
if __name__ == '__main__':

    num_elementos = 20

    pilha = cPilha(num_elementos)

    for i in range(20):
        pilha.push(i)
        print(i) 

    print("**********************************")
    print(pilha.pop())
    print(pilha.pop()) 
