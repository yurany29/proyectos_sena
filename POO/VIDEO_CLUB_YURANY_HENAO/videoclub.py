from socio import Socio
from pelicula import Pelicula
from sala_video import Sala_video

#definimos la clase
class Videoclub:

	#constructos de clase
	def __init__(self):
		#atributo tipo lista
		self.socios = []
		self.peliculas = []
		self.salas = []

	def buscar_socio(self, codigo):
		for i in range(len(self.socios)):
			if self.socios[i].codigo == codigo: #compara cada codigo de los objetos de la lista con el nuevo codigo ingresado
				return i #posicion cero
		return -1 #si la condicion no se cumple

	def adicionar_socio(self, socio):
		if self.buscar_socio(socio.codigo) == -1:
			self.socios.append(socio)
			return True
		return False

	def listar_socios(self):
		for i in self.socios:
			print("*****************************")
			i.mostrar_socio()

	def modificar_socio(self, codigo):
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != -1:
			if self.socios[pos_socio].codigo == codigo:
				print("*****************************")
				print("*** OPCIONES PARA MODIFICAR ***")
				print("*****************************")

				try:
					print("*****************************")
					print("1 = Modificar nombre")
					print("2 = Modificar telefono")
					print("3 = Modificar la direccion")
					print("*****************************")

					op = int(input("Seleccione la opcion a modificar: "))

					if op == 1:
						nombre = input("Digite el nuevo nombre del socio: ")
						self.socios[pos_socio].nombre = nombre
						return True

					elif op == 2:
						telefono = input("Digite el nuevo telefono del socio: ")
						self.socios[pos_socio].telefono = telefono
						return True

					elif op == 3:
						direccion = input("Digite la nueva direccion del socio: ")
						self.socios[pos_socio].direccion = direccion
						return True

					else:
						return False


				except ValueError:
					print("*****************************")
					print("Error - El dato debe ser entero")
					print("*****************************")
					input()

			else:
				return False

		else:
			return False


	def eliminar_socio(self, codigo):
		pos_socio = self.buscar_socio(codigo)
		if pos_socio != -1:
			del (self.socios[pos_socio])
			return True

		else:
			return False

	def adicionar_pelicula(self, pelicula):
		if self.buscar_pelicula(pelicula.codigo) == -1:
			self.peliculas.append(pelicula)
			return True
		return False

	def buscar_pelicula(self, codigo):
		for i in range(len(self.peliculas)):
			if self.peliculas[i].codigo == codigo: 
				return i 
		return -1 

	def listar_pelicula(self):
		for pelicula in self.peliculas:
			print("*****************************")
			pelicula.mostrar_pelicula()

	def modificar_pelicula(self, codigo):
		pos_pelicula = self.buscar_pelicula(codigo)
		if pos_pelicula != -1:
			if self.peliculas[pos_pelicula].codigo == codigo:
				print("*****************************")
				print("*** OPCIONES PARA MODIFICAR ***")
				print("*****************************")

				try:
					print("*****************************")
					print("1 = Modificar titulo")
					print("2 = Modificar genero")
					print("*****************************")

					op = int(input("Seleccione la opción a modificar: "))

					if op  == 1:
						titulo = input("Digite el nuevo nombre de la pelicula: ")
						self.peliculas[pos_pelicula].titulo = titulo
						return True

					elif op == 2:
						genero = input("Digite el nuevo genero de la pelicula: ")
						self.peliculas[pos_pelicula].genero = genero
						return True

					else:
						return False

				except ValueError:
					print("*****************************")
					print("Error - El dato debe ser entero")
					print("*****************************")
					input()
			else:
				return False

		else:
			return False


	def eliminar_pelicula(self, codigo):
		pos_pelicula = self.buscar_pelicula(codigo)
		if pos_pelicula != -1:
			del (self.peliculas[pos_pelicula])
			return True
		return False


	def alquilar_pelicula(self, codigo_socio, codigo_pelicula):
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		pos_socio = self.buscar_socio(codigo_socio)
		if pos_pelicula != -1 and pos_socio != -1:
			if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.peliculas[pos_pelicula].alquilada = True
					self.peliculas[pos_pelicula].nombre_socio = self.socios[pos_socio].nombre
					return True
				else:
					return False

			else:
				return False
		else:
			return False


	def devolver_pelicula(self, codigo_socio, codigo_pelicula):
		pos_pelicula = self.buscar_pelicula(codigo_pelicula)
		pos_socio = self.buscar_socio(codigo_socio)
		if pos_pelicula != -1 and pos_socio != -1:
			if self.peliculas[pos_pelicula].codigo == codigo_pelicula:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.peliculas[pos_pelicula].alquilada = False
					return True
				else:
					return False
			else:
				return False
		else:
			return False


	def listar_peliculas_alquiladas(self):
		for pelicula in self.peliculas:
			print("*****************************")
			pelicula.peliculas_alquiladas()
			
	def listar_peliculas_disponibles(self):
		for i in self.peliculas:
			print("*****************************")
			i.peliculas_disponibles()


	def buscar_sala(self, codigo):
		for i in range(len(self.salas)):
			if self.salas[i].codigo == codigo:
				return i
		return -1

	def adicionar_sala_video(self, sala_video):
		if self.buscar_sala(sala_video.codigo) == -1:
			self.salas.append(sala_video)
			return True
		return False


	def llenar_sala(self, codigo_sala, codigo_socio):
		pos_sala = self.buscar_sala(codigo_sala)
		pos_socio = self.buscar_socio(codigo_socio)

		if pos_sala != -1 and pos_socio != -1:
			if self.salas[pos_sala].codigo == codigo_sala:
				if self.socios[pos_socio].codigo == codigo_socio:
					self.salas[pos_sala].disponible = True
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	

	def listar_salas(self):
		for i in self.salas:
			print("*****************************")
			i.mostrar_sala()