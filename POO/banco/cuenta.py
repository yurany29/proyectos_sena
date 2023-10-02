class Cuenta:
	def __init__(self, id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo):
		self.__id_titular = id_titular
		self.__nombre_titular = nombre_titular
		self.__numero_cuenta = num_cuenta
		self.__saldo = saldo
		self.__fecha = fecha
		self.__tipo_cuenta = tipo_cuenta
		self.__cupo = cupo
		self.__cupo_original = cupo

	def get_num_cuenta(self): #Entrega informacion
		return self.__numero_cuenta

	def visualizar_cuenta(self):
		print("id del titular: ",self.__id_titular)
		print("Nombre del titular: ",self.__nombre_titular)
		print("Numero_cuenta: ",self.__numero_cuenta)
		print("Saldo de la cuenta: ",self.__saldo)
		print("Fecha actual: ",self.__fecha)
		print("Tipo de cuenta: ",self.__tipo_cuenta)
		print("Cupo disponible: ",self.__cupo)
		if self.__saldo < 0:
			print("Total disponible: ", self.__cupo)
		else:
			print("Total disponible: ",self.__saldo + self.__cupo)

	
	def retirar(self, monto):
		if self.__saldo - monto > 0:
			self.__saldo -= monto
			return True
		else:
			return False

	def retirar_corriente(self, monto):
		if self.__saldo > 0:
			if (self.__saldo + self.__cupo) - monto > 0:
				self.__saldo -= monto
				if self.__saldo < 0:
					self.__cupo += self.__saldo
					return True
			return False

		else:
			if (self.__cupo - monto) > 0:
				self.__cupo -= monto
				return True
			return False


	def depositar(self, monto):
		if monto > 0:
			self.__saldo += monto
			return True
		return False

	def depositar_corriente(self, monto):
		if monto > 0:
			if self.__saldo > 0 :
				self.__saldo += monto
			elif self.__saldo < 0:
				self.__saldo += monto
				if self.__cupo < self.__cupo_original:
					embalado = self.__cupo_original - self.__cupo

					if monto < embalado:
						self.__cupo += monto
						return True

					else:
						self.__cupo = self.__cupo_original
						return True
			else:		
				return False
		else:
			return False


	def get_saldo(self):
		return self.__saldo

	def get_nombre_titular(self):
		return self.__nombre_titular

	def get_id(self):
		return self.__id_titular

	def get_tipo_cuenta(self):
		return self.__tipo_cuenta

	def get_cupo(self):
		return self.__cupo