from os import system
from estudiante import Estudiante
from colegio import Colegio
from aula import Aula
from fecha import Fecha
from asistencia import Asistencia

class Menu:

	def __init__(self):
		self.colegio = Colegio()

	def listar_estudiantes(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     LISTAR ESTUDIANTE"    )
		print("+++++++++++++++++++++++++")
		for estudiante in self.colegio.get_estudiantes():
			print("+++++++++++++++++++++++++")
			print("codigo: %s" % (estudiante.get_codigo()))
			print("Nombre: %s" % (estudiante.get_nombre()))
			print("Apellido: %s" % (estudiante.get_apellido()))
			print("+++++++++++++++++++++++++")
		input()

	def listar_aulas(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     LISTAR LAS AULAS"    )
		print("+++++++++++++++++++++++++")
		for aula in self.colegio.get_aulas():
			print("+++++++++++++++++++++++++")
			print("codigo: %s" % (aula.codigo_aula))
			print("Nombre: %s" % (aula.nombre_aula))
			print("Capacidad del aula: %s" % (aula.capacidad_aula))
			print("+++++++++++++++++++++++++")
		input()

	def listar_asistencias(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     LISTAR ASISTENCIAS"    )
		print("+++++++++++++++++++++++++")
		for asistencia in self.colegio.get_asistencias():
			print("+++++++++++++++++++++++++")
			asistencia.visualizar_asistencia()
			print("+++++++++++++++++++++++++")
		input()

	def listar_asistencia_aula(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     LISTAR ASISTENCIA AULA    ")
		print("+++++++++++++++++++++++++")

		codigo_aula = input("Digite el codigo del aula: ")
		pos_aula = self.colegio.buscar_aula(codigo_aula)

		if pos_aula != -1:
			for asistencia in self.colegio.get_asistencia_aula(codigo_aula):
				print("+++++++++++++++++++++++++")
				asistencia.visualizar_asistencia()
				print("+++++++++++++++++++++++++")
			input()

		else:
			print("El aula no existe")
			input()

	def listar_asistencia_aula_estudiante(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     LISTAR ASISTENCIA AL AULA DEL ESTUDIANTE   ")
		print("+++++++++++++++++++++++++")

		codigo_estudiante = input("Digite el codigo del estudiante: ")
		pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

		if pos_estudiante != -1:
			for asistencia in self.colegio.get_asistencia_estudiante(codigo_estudiante):
				print("+++++++++++++++++++++++++")
				asistencia.visualizar_asistencia_estudiante()
				print("+++++++++++++++++++++++++")
			input()

		else:
			print("El estudiante no existe")
			input()



	def pedir_datos_crear_estudiante(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     CREAR ESTUDIANTE"    )
		print("+++++++++++++++++++++++++")
		nombre = input("Digite el nombre: ")
		apellido = input("Digite el apellido: ")
		codigo = input("Digite el codigo: ")

		estudiante = Estudiante(nombre, apellido, codigo)

		if self.colegio.adicionar_estudiante(estudiante):
			print("+++++++++++++++++++++++++")
			print("Info - El estudiante se agrego correctamente")
			print("+++++++++++++++++++++++++")
			input()

		else:
			print("+++++++++++++++++++++++++")
			print("Error - El estudiante no se pudo adicionar")
			print("+++++++++++++++++++++++++")
			input()


	def crear_aula(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     CREAR AULA"    )
		print("+++++++++++++++++++++++++")
		nombre_aula = input("Digite el nombre del aula: ")
		codigo_aula = input("Digite el codigo del aula: ")
		capacidad_aula = input("Digite la capacidad del aula: ")

		aula = Aula(nombre_aula, codigo_aula, capacidad_aula)

		if self.colegio.adicionar_aula(aula):
			print("+++++++++++++++++++++++++")
			print("Info - El aula fue adicionada correctamente")
			print("+++++++++++++++++++++++++")
			input()

		else:
			print("+++++++++++++++++++++++++")
			print("Error - El Aula no se pudo adicionar")
			print("+++++++++++++++++++++++++")
			input()


	def crear_asistencia_aula(self):
		system("cls")
		print("+++++++++++++++++++++++++")
		print("     CREAR ASISTENCIA AL AULA"    )
		print("+++++++++++++++++++++++++")
		codigo_aula = input("Digite el codigo del aula: ")
		pos_aula = self.colegio.buscar_aula(codigo_aula)

		if pos_aula != -1:
			dia = int(input("Digite el dia: "))
			mes = int(input("Digite el mes: "))
			anio = int(input("Digite el año: "))
			fecha = Fecha(anio, mes, dia)

			codigo_asistencia = int(input("Digite el codigo de la asistencia: "))

			asistencia_aula = Asistencia(fecha, self.colegio.get_aula(pos_aula), codigo_asistencia)

			while True:
				print("+++++++++++++++++++++++++")
				print("+++++++++++++++++++++++++")
				print("  ASISTENCIA ESTUDIANTE  ")
				print("+++++++++++++++++++++++++")
				print("1: Ingresar la asistencia del estudiante")
				print("2: Salir")
				print("+++++++++++++++++++++++++")
				op = int(input("Digite la opcion: "))
				print("+++++++++++++++++++++++++")

				if op == 1:
					codigo_estudiante = input("Digite el codigo del estudiante: ") #input = string
					pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)

					if pos_estudiante != -1:
						asistencia_aula.adicionar_estudiante(self.colegio.get_estudiante(pos_estudiante))

					else:
						print("+++++++++++++++++++++++++")
						print("ERROR - El estudiante no existe")
						print("+++++++++++++++++++++++++")
						input() #metodo de captura que espera algo

				elif op == 2:
					break

				else:
					print("+++++++++++++++++++++++++")
					print("ERROR - Opcion no valida")
					print("+++++++++++++++++++++++++")
					input()

			self.colegio.adicionar_asistencia(asistencia_aula)

		else:
			print("+++++++++++++++++++++++++")
			print("ERROR - Opcion no valida")
			print("+++++++++++++++++++++++++")
			input()


	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("+++++++++++++++++++++++++")
			print("+++++++++++++++++++++++++")
			print("         COLEGIO         ")
			print("+++++++++++++++++++++++++")
			print("+++         MENU      +++")
			print("+++++++++++++++++++++++++")
			print("1: Crear Estudiante")
			print("2: crear Aula")
			print("3: Crear Asistencia")
			print("4: Listar Estudiantes")
			print("5: Listar Aulas")
			print("6: Listar Asistencias")
			print("7: Listar Asistencia por Aula")
			print("8: Listar Asistencia al aula del Estudianre")
			print("0: Salir")
			print("+++++++++++++++++++++++++")
			print("+++++++++++++++++++++++++")

			try:

				op = int(input("Digite la opcion: "))
				
				if op == 1:
					self.pedir_datos_crear_estudiante()

				elif op == 2:
					self.crear_aula()

				elif op == 3:
					self.crear_asistencia_aula()

				elif op == 4:
					self.listar_estudiantes()

				elif op == 5:
					self.listar_aulas()

				elif op == 6:
					self.listar_asistencias()

				elif op == 7:
					self.listar_asistencia_aula()


				elif op == 8:
					self.listar_asistencia_aula_estudiante()

				elif op == 0:
					break

				else:
					print("+++++++++++++++++++++++++")
					print("Error - Opcion no valida")
					print("+++++++++++++++++++++++++")



			except ValueError:
				print("+++++++++++++++++++++++++")
				print("Error - El dato debe ser entero")
				print("+++++++++++++++++++++++++")
				input()

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()