from ArvoreTriangulos import ArvoreTriangulos
from terreno import * 
import pyglet 
from pyglet.window import key

# *************************************************
nivel = input("Insira um Nível de detalhe:")

window = pyglet.window.Window(width=500, height=500)


# Exemplo de uso
path = os.path.join(os.path.dirname(__file__), 'DEMs')
img = pyglet.image.load(f"{path}/Terreno0.5K.jpg")
arvore = ArvoreTriangulos()
arvore.gerar_arvore(img)



triangulos = arvore.obter_triangulos_nivel(nivel)
for triangulo in triangulos:
    print(triangulo)
batch = pyglet.graphics.Batch()  # Criação do objeto batch
criaTriangulacao(triangulos, batch, False )

@window.event
def on_draw():
    window.clear()
    batch.draw()

# Inicie o loop de eventos da janela
pyglet.app.run()


   
