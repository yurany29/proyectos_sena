class Pelicula:

	def __init__(self, codigo, titulo, genero, nombre_socio):

		self.codigo = codigo
		self.titulo = titulo
		self.genero = genero
		self.alquilada = False
		self.nombre_socio = nombre_socio

	def mostrar_pelicula(self):
		print("Codigo: ", self.codigo)
		print("Titulo: ", self.titulo)
		print("Genero: ", self.genero)
		print("Alquilada: ", self.alquilada)
		print("nombre_socio: ",self.nombre_socio)
		
	def peliculas_alquiladas(self):
		if self.alquilada == True:
			print("Codigo: ", self.codigo)
			print("Titulo: ", self.titulo)
			print("Genero: ", self.genero)
			print("Alquilada: ", self.alquilada)
			print("nombre_socio: ",self.nombre_socio)

	def peliculas_disponibles(self):
		if self.alquilada == False:
			print("Codigo: ", self.codigo)
			print("Titulo: ", self.titulo)
			print("Genero: ", self.genero)
			print("Alquilada: ", self.alquilada)
			print("nombre_socio: ",self.nombre_socio)