from Node import Node
from terreno import *
from triangulo import *
import pyglet 
from pyglet.window import *
import os

# *******************************************************
# ***                                                 ***
# *******************************************************

class ArvoreTriangulos:
    def __init__(self):
        self.raiz = None

# *************************************************************************************************************************
    def gerar_arvore(self, imagem):
        largura = imagem.width
        altura = imagem.height

        v0 = (0, 0)
        v1 = (largura, 0)
        v2 = (largura, altura)
        v3 = (0, altura)

        quadrado_inicial = Quadrado(v0, v1, v2, v3)
        self.raiz = Node(quadrado_inicial)

        self.subdividir_triangulos(self.raiz, imagem)

# *************************************************************************************************************************
    def subdividir_triangulos(self, no, imagem):
        quadrado = no.getDado()

        filho_esq = Node(Triangulo(quadrado.v1, quadrado.v2, quadrado.v0))
        filho_dir = Node(Triangulo(quadrado.v0, quadrado.v1, quadrado.v3))

        no.setFilhoEsq(filho_esq)
        no.setFilhoDir(filho_dir)

        ponto_medio_hipotenusa = self.calcular_ponto_medio(quadrado.v0, quadrado.v2)

        while self.calcular_area(filho_esq.getDado().v1, filho_esq.getDado().v2, filho_esq.getDado().v0) > 0.5:
            filho_esq_v2_v3 = self.calcular_ponto_medio(quadrado.v2, quadrado.v1)
            self.subdividir_triangulos_recursivo(filho_esq, ponto_medio_hipotenusa, quadrado.v1, filho_esq_v2_v3, imagem)
            quadrado = filho_esq.getDado()
            ponto_medio_hipotenusa = self.calcular_ponto_medio(quadrado.v0, quadrado.v2)

        while self.calcular_area(filho_dir.getDado().v0, filho_dir.getDado().v1, filho_dir.getDado().v2) > 0.5:
            filho_dir_v1_v3 = self.calcular_ponto_medio(quadrado.v1, quadrado.v3)
            self.subdividir_triangulos_recursivo(filho_dir, ponto_medio_hipotenusa, filho_dir_v1_v3, quadrado.v0, imagem)
            quadrado = filho_dir.getDado()
            ponto_medio_hipotenusa = self.calcular_ponto_medio(quadrado.v0, quadrado.v2)

# *************************************************************************************************************************
    def subdividir_triangulos_recursivo(self, no, ponto_medio_hipotenusa, v1, v2, imagem):
        triangulo = no.getDado()

        filho_esq_v1_pm = self.calcular_ponto_medio(triangulo.v1, ponto_medio_hipotenusa)
        filho_esq_pm_v2 = self.calcular_ponto_medio(ponto_medio_hipotenusa, v2)

        filho_esq = Node(Triangulo(triangulo.v1, filho_esq_v1_pm, filho_esq_pm_v2))
        no.setFilhoEsq(filho_esq)

        if self.calcular_area(filho_esq.getDado().v0, filho_esq.getDado().v1, filho_esq.getDado().v2) > 0.5:
            self.subdividir_triangulos_recursivo(filho_esq, ponto_medio_hipotenusa, filho_esq_v1_pm, ponto_medio_hipotenusa, imagem)

        filho_dir_pm_v2 = self.calcular_ponto_medio(ponto_medio_hipotenusa, triangulo.v2)
        filho_dir_pm_v1 = self.calcular_ponto_medio(ponto_medio_hipotenusa, v1)

        filho_dir = Node(Triangulo(ponto_medio_hipotenusa, filho_dir_pm_v1, v1))
        no.setFilhoDir(filho_dir)

        if self.calcular_area(filho_dir.getDado().v0, filho_dir.getDado().v1, filho_dir.getDado().v2) > 0.5:
            self.subdividir_triangulos_recursivo(filho_dir, ponto_medio_hipotenusa, filho_dir_pm_v1, filho_dir_pm_v2, imagem)

# *************************************************************************************************************************
    @staticmethod
    def calcular_ponto_medio(ponto1, ponto2):
        return ((ponto1[0] + ponto2[0]) / 2, (ponto1[1] + ponto2[1]) / 2)

# *************************************************************************************************************************
    @staticmethod
    def calcular_area(ponto1, ponto2, ponto3):
        return abs((ponto1[0] * (ponto2[1] - ponto3[1]) + ponto2[0] * (ponto3[1] - ponto1[1]) + ponto3[0] * (ponto1[1] - ponto2[1])) / 2)

# *************************************************************************************************************************
    def obter_triangulos_nivel(self, nivel):
        triangulos = []
        self._obter_triangulos_nivel_recursivo(self.raiz, nivel, 0, triangulos)  # Modificação aqui
        return triangulos


# *************************************************************************************************************************
    def _obter_triangulos_nivel_recursivo(self, no, nivel_desejado, nivel_atual, triangulos):
        if nivel_atual == nivel_desejado:
            triangulo = no.getDado()
            triangulos.append(triangulo)
        else:
            nivel_atual += 1
            if nivel_atual <= nivel_desejado:
                if no.getFilhoEsq() is not None:
                    self._obter_triangulos_nivel_recursivo(no.getFilhoEsq(), nivel_desejado, nivel_atual, triangulos)
                if no.getFilhoDir() is not None:
                    self._obter_triangulos_nivel_recursivo(no.getFilhoDir(), nivel_desejado, nivel_atual, triangulos)

# *************************************************************************************************************************
if __name__ == "__main__":
   
    path = os.path.join(os.path.dirname(__file__), 'DEMs')
    img = pyglet.image.load(f"{path}/Terreno0.5K.jpg")

    arvore_triangulos = ArvoreTriangulos()
    arvore_triangulos.gerar_arvore(img)
    triangulos_nivel = arvore_triangulos.obter_triangulos_nivel(1)
    for triangulo in triangulos_nivel:
        print(triangulo) 


    
    

  
