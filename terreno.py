# ###############################################
# Desenhando Terrenos (MDTs e Imagens)
# ###############################################

import 	sys
import os
import 	pyglet
from 	pyglet.window  	import key

WIN_X 	= 500
WIN_Y 	= 500

drawMDT	= True


# *******************************************************
# ***                                                 ***
# *******************************************************
def leImagem(arq):

	# Chama a função de leitura de uma imagem do Pyglet, 
	# passando como parametro a localização do arquivo

	img = pyglet.image.load(arq)

	# Uma vez lida a imagem o obj criado possui atributos como largura e altura da imagem
	# que pode ser consultados

	print(f'{img.width} x {img.height} => {img.width*img.height}')

	# O objeto image criado pelo Pyglet é retornado

	return img

# *******************************************************
# ***                                                 ***
# *******************************************************
def calculaElevacoes(MDT):

	# Para ter acesso aos pixels/amostras do objeto imagem do Pyglet
	# é necessário recuperar os dados, em formato de um vetor de intensidade.
	# No caso de terrenos existe apenas um canal de "cor" na imagem, referente a intensidade do pixel
	# O valor de "pitch" é definido para que possamos utilizar um endereçamento matricial (linhaxcoluna) para
	# acessar os elementos do vetor. 

	format = 'I'
	pitch = MDT.width * len(format)
	amostras = MDT.get_image_data().get_data(format, pitch)

	# Aqui contaremos quantos pixels possuem cada valor de elevação
	# Lembrando que imagens em tons de cinza (um canal de cor) representam suas intensidades em 1 Byte,
	# ou seja, permite 256 intensidades com valores no intervalo [0..255]

	contElev = [0] * 256

	eMax = 0
	eMin = 256
	eMedia = 0

	for i in range(MDT.width):		
		for j in range(MDT.height):

			# cada linha salta "pitch" elementos (colunas) para passar para a proxima linha 
			elevacao = amostras[i * pitch + j]

			# verifica os valores de intensidade máxima e mínima

			if elevacao > eMax: eMax = elevacao
			elif elevacao < eMin: eMin = elevacao

			# incrementa o contador de elevações do valor encontrado no pixel/amostra

			contElev[elevacao] += 1 	

	# Calcula o somatório das intensidades e divide pelo total de amostras/pixels para gerar a
	# intensidade/elevação média

	eMedia = 0
	for k in range(256):
		eMedia += contElev[k] * k

	eMedia /= MDT.width * MDT.height

	# retorno os valores calculados

	return eMin, eMax, eMedia

# *******************************************************
# ***                                                 ***
# *******************************************************
def criaTriangulacao(triangles, bat, fill=True):

	# Sabendo que a tela mede WIN_X pixels de largura por WIN_Y pixel de altura, temos
	#  V3    V2
	#  +-----+
	#  |   / |
	#  | /   |
	#  +-----+
	#  V0    V1

	x0 = 1
	y0 = 1
	x1 = WIN_X
	y1 = 1
	x2 = WIN_X
	y2 = WIN_Y
	x3 = 1
	y3 = WIN_Y

	xm = WIN_X // 2
	ym = WIN_Y // 2

	triangles.clear()

	# Formas geométricas no Pyglet são definidas por shapes pré definidos
	# No caso desse exemplo se a opção fill estiver verdadeira 
	# serão criados triangulos que são sempre desenhados preenchidos

	if fill:
		tri = pyglet.shapes.Triangle(x0, y0, xm, ym, xm, y0, color=(255, 0, 0, 255), batch=bat)
		triangles.append(tri)

		tri = pyglet.shapes.Triangle(x2, y2, xm, ym, x2, ym, color=(0, 0, 255, 255), batch=bat)
		triangles.append(tri)

	# No caso o parametro fill sinalizar falso 
	# serão criados triangulos definidos apenas por linhas
	else:
		tri = pyglet.shapes.Line(x0, y0, x1, y1, color=(255, 0, 0, 255), batch=bat)
		triangles.append(tri)
		tri = pyglet.shapes.Line(x1, y1, x2, y2, color=(0, 255, 0, 255), batch=bat)
		triangles.append(tri)
		tri = pyglet.shapes.Line(x2, y2, x0, y0, color=(0, 0, 255, 255), batch=bat)
		triangles.append(tri)

		tri = pyglet.shapes.Line(x0, y0, x2, y2, color=(0, 0, 255, 255), batch=bat)
		triangles.append(tri)
		tri = pyglet.shapes.Line(x2, y2, x3, y3, color=(0, 255, 255, 255), batch=bat)
		triangles.append(tri)
		tri = pyglet.shapes.Line(x3, y3, x0, y0, color=(255, 0, 255, 255), batch=bat)
		triangles.append(tri)
	 	


# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

	# Essas variáveis precisam ser globais pois serão acessadas dentro das funções de tratamento
	# de eventos da janela

	global window, MDT_Image, MDT_Triang

	# A representação do terreno como uma imagem, armazenada no arquivo passado como parametro
	# é lida pela função a seguir
	path = os.path.join(os.path.dirname(__file__), 'DEMs')
	MDT_Image 	= leImagem(pyglet.image.load(f"{path}/Terreno0.5K.jpg"))

	WIN_X = MDT_Image.width
	WIN_Y = MDT_Image.height

	# O acesso ao valor de cada pixel da image, ou seja, a elevação de cada amostra do MDT
	# é feita pela função a seguir. Essa função não permite modificar os valores de elevação

	eMin, eMax, eMedia = calculaElevacoes(MDT_Image)

	print(f'Elevações: Max = {eMax}  -  Min = {eMin}  -  Media = {eMedia}')

	# As funções a seguir criam uma janela gráfica para desenho

	window 		= pyglet.window.Window(WIN_X, WIN_Y)
	window.set_caption('Visualizando um Modelo Digital de Terreno')

	# Um "lote" de objetos gráficos é criado no Pyglet para que possamos
	# preencher com o que deve ser desenhado a cada "frame"

	MDT_Triang 	= pyglet.graphics.Batch()

	# A lista dos "shapes" do Pyglet a serem desenhados começa vazia

	tri 		= []

	# Essa função cria os "shapes" do Pyglet armazendo a lista tri e adicionando no "lote" MDT_Triang

	criaTriangulacao(tri, MDT_Triang, True)

	# Usando o "decorator" do Python é possível associar funções a eventos do ambiente de janelas
	# Abaixo dois tipos de eventos são associados a funções:
	# on_draw() => função chamada sempre que a tela precisa ser redesenhada. 
	# on_key_press() => função chamada sempre que uma tecla for pressionada no teclado

	@window.event
	def on_draw():
		global drawMDT

		# Limpa a janela de desenho
		window.clear()

		# com base no valor armazenado em "drawMDT" decide se será mostrada a imagem do terreno ou
		# sua representação como uma triangulação
		if drawMDT:
			MDT_Image.blit(0, 0, 0)
		else:
			MDT_Triang.draw()

	# key press event	
	@window.event
	def on_key_press(symbol, modifier):
		global drawMDT

		# Mapeia as teclas que deverão gerar alguma ação dentro da aplicação
		# No caso a tecla 'I' chaveia entre a imagem e a triangulação
		# enquanto que a tecla 'T' recria os elementos de desenho alternando 
		# entre triangulos preenchidos ou só com o contorno. 
		# O parametro "modifier" indica se a tecla "SHIFT" estava acionada
		# permitindo diferenciar entre 'I' e 'i'
		if symbol == key.I:
			drawMDT = True
		elif symbol == key.T:
			drawMDT = False
			criaTriangulacao(tri, MDT_Triang, modifier & key.MOD_SHIFT)				

	# Aqui a aplicação entra no loop de eventos e só retorna quando a tecla 'ESC' for pressionada
	pyglet.app.run()

	# Atenção que todos os comandos colocados a partir desse ponto só serão executados ao 
	# final da aplicação.

	print("Só passo aqui no final da aplicação!")


    

mico(3)
