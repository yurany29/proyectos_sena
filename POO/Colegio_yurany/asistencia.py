from fecha import Fecha
from estudiante import Estudiante
from aula import Aula

class Asistencia:

	def __init__(self, fecha, aula, codigo):
		self.__codigo = codigo
		self.__fecha = fecha
		self.__aula = aula
		self.__estudiantes = []

	def get_codigo(self):
		return self.__codigo

	def get_fecha(self):
		return self.__fecha

	def get_aula(self):
		return self.__aula

	def get_estudiantes(self):
		return self.__estudiantes

	def buscar_estudiante(self, estudiante):
		for item_estudiante in self.__estudiantes:
			if item_estudiante.get_codigo() == estudiante.get_codigo():
				return True
		return -1

	def buscar_estudiante_2(self, codigo_estudiante):
		for i in range(len(self.__estudiantes)):
			if self.__estudiantes[i].get_codigo() == codigo_estudiante:
				return codigo_estudiante
		return False

	def adicionar_estudiante(self, estudiante):
		if self.buscar_estudiante(estudiante) == -1:
			self.__estudiantes.append(estudiante)
			return True
		return False

	def visualizar_asistencia(self):
		print("Codigo: %s" % (self.__codigo))
		self.__fecha.visualizar_fecha()
		print("Aula: %s" % (self.__aula.nombre_aula))
		print("+++++++++++++++++++++++++")
		for estudiante in self.__estudiantes:
			estudiante.visualizar_estudiante()

	def visualizar_asistencia_estudiante(self):
		for estudiante in self.__estudiantes:
			estudiante.visualizar()
			print("+++++++++++++++++++++++++")
			print("Codigo: %s" % (self.__codigo))
			self.__fecha.visualizar_fecha()
			print("Aula: %s" % (self.__aula.nombre_aula))
			print("+++++++++++++++++++++++++")
		









			
