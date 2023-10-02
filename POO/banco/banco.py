import random
from cuenta import Cuenta

class Banco:

	def __init__(self):
		self.__cuentas = []
		self.__numeros_cuentas = []

	def generar_numeros_cuentas(self):
		while True:
			numero = random.randint(1, 9)
			if numero not in self.__numeros_cuentas:
				self.__numeros_cuentas.append(numero)
				break
		return numero
	
	def buscar_cuenta(self, num_cuenta):
		for i in range(len(self.__cuentas)):
			if self.__cuentas[i].get_num_cuenta() == num_cuenta:
				return i 
		return -1

	def buscar_id(self, id_titular):
		for i in range(len(self.__cuentas)):
			if self.__cuentas[i].get_id() == id_titular:
				return i
		return -1

	def buscar_tipo_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			tipo_cuenta = self.__cuentas[pos].get_tipo_cuenta()
			return tipo_cuenta

	def adicionar_cuenta(self, cuenta):
		pos = self.buscar_cuenta(cuenta.get_num_cuenta())
		if pos == -1:
			self.__cuentas.append(cuenta)
			return True
		return False

	def visualizar_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].visualizar_cuenta():
				return True
		return False
	

	def retirar_monto_cuenta(self, num_cuenta, monto):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			if self.__cuentas[pos].retirar(monto):
				return True
		return False


	def retirar_monto_corriente(self, num_cuenta, monto):
		pos = self.buscar_cuenta(num_cuenta)
		if pos !=  -1:
			if self.__cuentas[pos].retirar_corriente(monto):
				return True
		return False

	def depositar_monto_cuenta(self, monto, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			self.__cuentas[pos].depositar(monto)
			return True
		return False

	def depositar_cuenta_corriente(self, monto, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			self.__cuentas[pos].depositar_corriente(monto)
			return True
		return False

	def consultar_saldo_cuenta(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			valor = self.__cuentas[pos].get_saldo()
			return valor

	def consultar_cupo(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			cupo = self.__cuentas[pos].get_cupo()
			return cupo

	def total_disponible(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			saldo = self.__cuentas[pos].get_saldo() 
			cupo = self.__cuentas[pos].get_cupo()
			if saldo < 0:
				total = cupo
				return total
			else:
				total = saldo + cupo
				return total

	def visualizar_cliente(self, num_cuenta):
		pos = self.buscar_cuenta(num_cuenta)
		if pos != -1:
			nombre = self.__cuentas[pos].get_nombre_titular()
			return nombre

	

