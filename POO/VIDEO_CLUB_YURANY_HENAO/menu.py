from os import system
from socio import Socio
from videoclub import Videoclub
from pelicula import Pelicula
from sala_video import Sala_video

#creamos clase
class Menu: #Nombre de la clase es el mismo nombre del archivo

	def __init__(self): #Es el constructor y contiene los atributos o objetos, permite que la clase tenga un punto de inicio 
		#self es el que permite el trabajo de los objetos.
		self.videoclub = Videoclub()

	def adicionar_socio(self):
		system("cls") #limpieza de consola
		print("*****************************")
		print("ADICIONAR SOCIO")
		print("*****************************")
		codigo = input("Digite su numero de documento: ")
		nombre = input("Digite su nombre completo con apellidos: ")
		telefono = input("Digite su numero de telefono celular: ")
		direccion = input("Digite su dirección de residencia: ")

		#Instancia de la clase
		#socio -> objeto
		#Socio -> clase
		socio = Socio(codigo, nombre, telefono, direccion)

		if self.videoclub.adicionar_socio(socio):
			print("*****************************")
			print("Info - El socio fue adicionado correctamente")
			print("*****************************")
			input()#Se utiliza para que los mensajes se dejen ver 

		else:
			print("*****************************")
			print("Error - El socio ya existe")
			print("*****************************")
			input()

	def listar_socios(self):
		system("cls")
		print("*****************************")
		print("      LISTAR SOCIOS          ")
		print("*****************************")
		self.videoclub.listar_socios()
		input()

	def modificar_socio(self):
		system("cls")
		print("*****************************")
		print("      MODIFICAR SOCIO        ")
		print("*****************************")
		codigo = input("Digite el codigo del socio que desea buscar: ")

		if self.videoclub.modificar_socio(codigo):
			print("*****************************")
			print("Info - los datos del socio fueron modificados")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - Los datos del socio no se pueden modificar")
			print("*****************************")
			input()
		
	def eliminar_socio(self):
		system("cls")
		print("*****************************")
		print("       ELIMINAR SOCIO        ")
		print("*****************************")
		codigo = input("Digite el codigo del socio que desea buscar: ")

		if self.videoclub.eliminar_socio(codigo):
			print("*****************************")
			print("Info - El socio fue eliminado")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - El socio no se puede eliminar")
			print("*****************************")
			input()


	def adicionar_pelicula(self):
		system("cls")
		print("*****************************")
		print("       ADICIONAR PELICULA      ")
		print("*****************************")
		codigo = input("Digite el codigo de la pelicula: ")
		titulo = input("Digite el nombre de la pelicula: ")
		genero = input("Digite el genero de la pelicula: ")
		nombre_socio = ("No asignado o la pelicula se encuentra disponible")
		pelicula = Pelicula(codigo, titulo, genero, nombre_socio)

		if self.videoclub.adicionar_pelicula(pelicula):
			print("*****************************")
			print("Info - La pelicula fue adicionada correctamente")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - La pelicula no se pudo adicionar")
			print("*****************************")
			input()

	def listar_pelicula(self):
		system("cls")
		print("*****************************")
		print("      LISTAR PELICULAS      ")
		print("*****************************")
		self.videoclub.listar_pelicula()
		input()

	def modificar_pelicula(self):
		system("cls")
		print("*****************************")
		print("      MODIFICAR PELICULA      ")
		print("*****************************")
		codigo = input("Digite el codigo de la pelicula que desea buscar: ")

		if self.videoclub.modificar_pelicula(codigo):
			print("*****************************")
			print("Info - los datos de la pelicula fueron modificados")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - Los datos de la pelicula no se pueden modificar")
			print("*****************************")
			input()


	def eliminar_pelicula(self):
		system("cls")
		print("*****************************")
		print("       ELIMINAR PELICULA       ")
		print("*****************************")
		codigo = input("Digite el codigo de la pelicula que desea buscar: ")

		if self.videoclub.eliminar_pelicula(codigo):
			print("*****************************")
			print("Info - La pelicula fue eliminada")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - La pelicula no se puede eliminar")
			print("*****************************")
			input()


	def alquilar_pelicula(self):
		system("cls")
		print("*****************************")
		print("       ALQUILAR PELICULA       ")
		print("*****************************")
		codigo_socio = input("Digite el codigo del socio que desea buscar: ")
		codigo_pelicula = input("Digite el codigo de la pelicula que desea buscar: ")

		if self.videoclub.alquilar_pelicula(codigo_socio, codigo_pelicula):
			print("*****************************")
			print("Info - La pelicula fue alquilada")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - La pelicula no fue alquilada")
			print("*****************************")
			input()

	def devolver_pelicula(self):
		system("cls")
		print("*****************************")
		print("       DEVOLVER PELICULA       ")
		print("*****************************")
		codigo_socio = input("Digite el codigo del socio que desea buscar: ")
		codigo_pelicula = input("Digite el codigo de la pelicula que desea buscar: ")

		if self.videoclub.devolver_pelicula(codigo_socio, codigo_pelicula):
			print("*****************************")
			print("Info - La pelicula fue devuelta")
			print("*****************************")
			input()


		else:
			print("*****************************")
			print("Error - La pelicula no fue devuelta")
			print("*****************************")
			input()


	def listar_peliculas_alquiladas(self):
		system("cls")
		print("*****************************")
		print("      LISTAR PELICULAS ALQUILADAS      ")
		print("*****************************")
		self.videoclub.listar_peliculas_alquiladas()
		input()


	def listar_peliculas_disponibles(self):
		system("cls")
		print("*****************************")
		print("      LISTAR PELICULAS DISPONIBLES      ")
		print("*****************************")
		self.videoclub.listar_peliculas_disponibles()
		input()

	def adicionar_sala_video(self):
		system("cls")
		print("*****************************")
		print("      ADICIONAR SALA DE VIDEO      ")
		print("*****************************")
		codigo = input("Digite el codigo de la sala: ")
		titulo = input("Digite el nombre de la pelicula: ")
		genero = input("Digite el genero de la pelicula: ")
		duracion = input("Digite la duracion de la pelicula: ")
		valor = input("Digite el valor de la entrada: ")
		inicio = input("Digite la hora de inicio: ")
		final = input("Digite la hora de finnalización: ")

		sala_video = Sala_video(codigo, titulo, genero, duracion, valor, inicio, final)

		if self.videoclub.adicionar_sala_video(sala_video):
			print("*****************************")
			print("Info - La sala de video fue adicionada correctamente")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - La sala de video no se pudo adicionar")
			print("*****************************")
			input()

	def llenar_sala(self):
		system("cls")
		print("*****************************")
		print("      INGRESAR A LA SALA DE VIDEO      ")
		print("*****************************")
		codigo_sala = input("Digite el codigo de la sala: ")
		codigo_socio = input("Digite el codogo del socio: ")

		if self.videoclub.llenar_sala(codigo_sala, codigo_socio):
			print("*****************************")
			print("Info - Ingreso a la sala correctamente")
			print("*****************************")
			input()

		else:
			print("*****************************")
			print("Error - No es posible ingresar a la sala")
			print("*****************************")
			input()

	def listar_salas(self):
		system("cls")
		print("*****************************")
		print("      LISTAR SALAS DE VIDEO      ")
		print("*****************************")

		self.videoclub.listar_salas()
		input()

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("*****************************")
			print("*****************************")
			print("VIDEOCLUB")
			print("*****************************")
			print("*****************************")
			print("Menu principal")
			print("*****************************")
			print("*****************************")
			print("1 = Crear Socio.")
			print("2 = listar Socios.")
			print("3 = Modificar socio.")
			print("4 = Eliminar socio.")
			print("5 = Crear pelicula")
			print("6 = Listar peliculas")
			print("7 = Modificar pelicula")
			print("8 = Eliminar pelicula")
			print("9 = Alquilar pelicula")
			print("10 = Devolver pelicula")
			print("11 = Listar peliculas alquiladas")
			print("12 = Listar peliculas disponibles")
			print("13 = Crear sala de video")
			print("14 = ingresar a la sala de video")
			print("15 = Listar las salas de video existentes")
			print("16 = Salir")
			print("*****************************")
			print("*****************************")

			try:
				op = int(input("Digite su opción: "))

				if op == 1:
					#invoco el metodo
					self.adicionar_socio()

				elif op == 2:
					#invoco el metodo
					self.listar_socios()

				elif op == 3:
					#invoco el metodo
					self.modificar_socio()

				elif op == 4:
					#invoco el metodo
					self.eliminar_socio()

				elif op == 5:
					self.adicionar_pelicula()

				elif op == 6:
					self.listar_pelicula()

				elif op == 7:
					self.modificar_pelicula()

				elif op == 8:
					self.eliminar_pelicula()

				elif op == 9:
					self.alquilar_pelicula()

				elif op == 10:
					self.devolver_pelicula()

				elif op == 11:
					self.listar_peliculas_alquiladas()

				elif op == 12:
					self.listar_peliculas_disponibles()

				elif op == 13:
					self.adicionar_sala_video()

				elif op == 14:
					self.llenar_sala()

				elif op == 15:
					self.listar_salas()

				elif op == 16:
					break

				else:
					print("*****************************")
					print("Error - opcion no valida")
					print("*****************************")
					input()

			except ValueError:
				print("*****************************")
				print("Error - el dato ingresado no es entero")
				print("*****************************")
				input()

if __name__ == '__main__':
	#instancia de clase Menu
	menu = Menu()
	menu.mostrar_menu_principal()