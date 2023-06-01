class cNo:

    def __init__(self, dado = None):
        self._dado = dado
        self._prox = None 

#*****************************************************************************
    def __str__(self):
        outStr = ""
        outStr += "+======+=================+\n"
        if self._dado is None:
            outStr += "|      None      |"
        else:
            outStr += f"| {self._dado:4} |"
        if self._prox is None:
            outStr += '       None       |\n'
        else:
            outStr += f" {id(self._prox):^17} |\n"
        outStr += "+======+=================+\n"
        outStr += "                 |   \n"
        outStr += "                 |   \n"
        outStr += "           +-----+   \n"
        outStr += "           |            \n"
        if self._prox:
            outStr += "           V            \n"
        else:
            outStr += "           =            \n"
        return outStr
    
#*****************************************************************************
    
    def setDado(self, dado):
        if type(dado) == int:
            self._dado = dado

#*****************************************************************************
    def setProx(self, prox):
        if type(prox) == cNo:
            self._prox = prox 

#*****************************************************************************
    def getDado(self):
        return self._dado
    
#*****************************************************************************    
    def getProx(self):
        return self._prox 
    
#*****************************************************************************   

if __name__ == "__main__": 
    
    no      = cNo()   
    outroNo = cNo(20)

    print(str(no))
    print(str(outroNo))

    no.setDado(100)
    no._dado = 200
    no.setProx(outroNo)
        
    print(str(no))
    print(str(outroNo))
