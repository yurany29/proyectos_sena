class Sala_video:

	def __init__(self, codigo, pelicula, genero, duracion, valor, inicio, final):

		self.codigo = codigo
		self.pelicula = pelicula
		self.genero = genero
		self. duracion = duracion
		self.valor = valor
		self.inicio = inicio
		self.final = final

	def mostrar_sala(self):
		print("Codigo: ", self.codigo)
		print("Pelicula", self.pelicula)
		print("Genero: ", self.genero)
		print("Duracion de la pelicula: ", self.duracion)
		print("Valor de la entrada: ", self.valor)
		print("Hora de inicio: ", self.inicio)
		print("Hora de Finalizaciòn: ", self.final)
