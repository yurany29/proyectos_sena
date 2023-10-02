class Estudiante:

	def __init__(self, nombre, apellido, codigo):

		self.__nombre = nombre
		self.__apellido = apellido
		self.__codigo = codigo

	def get_codigo(self):
		return self.__codigo

	def get_nombre(self):
		return self.__nombre

	def get_apellido(self):
		return self.__apellido

	def visualizar_estudiante(self):
		print("Nombre: %s" % (self.__nombre))
		print("Apellido: %s" % (self.__apellido))
		print("Codigo: %s" % (self.__codigo))
		print("+++++++++++++++++++++++++")

	def visualizar(self):
		print("Nombre del estudiante: %s" % (self.__nombre))
		print("+++++++++++++++++++++++++")
