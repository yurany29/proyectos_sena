from os import system # se utiliza para que la consola se pueda limpiar
from datetime import datetime
from banco import Banco
from cuenta import Cuenta


class Menu:
	def __init__(self):
		self.banco = Banco()


	def pedir_datos_cuenta(self):
		try:
			system("cls")
			print("**************************")
			print("*****  CREAR CUENTA  *****")
			print("**************************")
			id_titular = input("Digite el numero de documento del titular: ")
			nombre_titular = input("Digite el nombre del titular: ")
			num_cuenta = self.banco.generar_numeros_cuentas()
			saldo = int(input("Digite el saldo inicial de la cuenta: "))
			fecha = datetime.now()

			while True:
				print("**************************")
				print("***   TIPO DE CUENTA   ***")
				print("**************************")
				print("1: Ahorros")
				print("2: Corriente")
				print("**************************")

				try:
					op_tipo_cuenta = int(input("Seleccione el tipo de cuenta: "))

					if op_tipo_cuenta == 1:
						tipo_cuenta = "Ahorro"
						cupo = 0
						break

					elif op_tipo_cuenta == 2:
						tipo_cuenta = "Corriente"
						

						try:
							cupo = float(input("Digite el cupo asignado a la cuenta: "))
							break

						except ValueError:
							print("**************************")
							print("Error - El cupo debe ser numerico")
							print("**************************")
							input()

					else:
						print("**************************")
						print("Error - Opcion no valida debe ser 1 o 2.")
						print("**************************")
						input()

				except ValueError:
					print("**************************")
					print("Error - El dato debe ser entero")
					print("**************************")
					input()

			cuenta = Cuenta(id_titular, nombre_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo)

			pos = self.banco.buscar_id(id_titular)

			if pos != -1:
				print("**************************")
				print("Error - El id del titular ya existe en el sistema")
				print("**************************")
				input()


			elif self.banco.adicionar_cuenta(cuenta):
				print("**************************")
				print("Info - La cuenta se creo correctamente")
				print("El numero de cuenta es: ", num_cuenta)
				print("**************************")
				input()

			else:
				print("**************************")
				print("Error - La cuenta no se puede crear")
				print("**************************")
				input()
			
		except ValueError:
			print("**************************")
			print("Error - El numero no esta definido")
			print("**************************")
			input()
				

	def pedir_datos_visualizar_cuenta(self):
		system("cls")
		print("**************************")
		print("*** VISUALIZAR CUENTA ***")
		print("**************************")
		num_cuenta = int(input("Digite el numero de cuenta: "))
		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1:
			self.banco.visualizar_cuenta(num_cuenta)
			input()

			                           
		else:
			print("**************************")
			print("Error - El numero de cuenta no existe")
			print("**************************")
			input()


	def pedir_datos_retiro_cuenta(self):
		system("cls")
		print("**************************")
		print("***      RETIROS       ***")
		print("**************************")
		num_cuenta = int(input("Digite el numero de la cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)
		if pos != -1 and self.banco.buscar_tipo_cuenta(num_cuenta) == 'Ahorros':
			monto = float(input("Digite el monto a retirar: "))

			if self.banco.retirar_monto_cuenta(num_cuenta, monto):
				print("**************************")
				print("Info - El retiro de la cuenta de ahorros se realizo con exito")
				print("**************************")
				input()

			else:
				print("**************************")
				print("Error -  El retiro no se pudo realizar")
				print("**************************")
				input()

		elif pos != -1 and self.banco.buscar_tipo_cuenta(num_cuenta) == 'Corriente':
			monto = float(input("Digite el monto a retirar: "))

			if self.banco.retirar_monto_corriente(num_cuenta, monto):
				print("**************************")
				print("Info - El retiro de la cuenta corriente se realizo con exito")
				print("**************************")
				input()

			else:
				print("**************************")
				print("Error -  El retiro no se pudo realizar")
				print("**************************")
				input()
		else:
			print("**************************")
			print("Error -  La cuenta no existe")
			print("**************************")
			input()


	def pedir_datos_deposito_cuenta(self):
		system("cls")
		print("**************************")
		print("***      DEPÓSITO       ***")
		print("**************************")
		num_cuenta = int(input("Digite el numero de la cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)

		if pos != -1 and self.banco.buscar_tipo_cuenta(num_cuenta) == 'Ahorros':
			monto = float(input("Digite el monto del depósito: "))

			if self.banco.depositar_monto_cuenta(monto, num_cuenta):
				print("**************************")
				print("Info -  El depósito se realizo correctamente")
				print("**************************")
				input()

			else:
				print("**************************")
				print("Error -  El depósito no se pudo realizar")
				print("**************************")
				input()

		elif pos != -1 and self.banco.buscar_tipo_cuenta(num_cuenta) == 'Corriente':
			monto = float(input("Digite el monto del depósito: "))

			if self.banco.depositar_cuenta_corriente(monto, num_cuenta):
				print("**************************")
				print("Info -  El depósito se realizo correctamente")
				print("**************************")
				input()

			else:
				print("**************************")
				print("Error -  El depósito no se pudo realizar")
				print("**************************")
				input()
		else:
			print("**************************")
			print("Error - La cuenta no existe")
			print("**************************")
			input()


	def mostrar_saldo_cuenta(self):
		system("cls")
		print("**************************")
		print("***      MOSTRAR SALDO       ***")
		print("**************************")
		num_cuenta = int(input("Digire el numero de la cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)
		if pos != -1:
			print("**************************")
			print("saldo: ", (self.banco.consultar_saldo_cuenta(num_cuenta)))
			print("cupo: ", (self.banco.consultar_cupo(num_cuenta)))
			print("Total disponible: ",(self.banco.total_disponible(num_cuenta)))
			print("**************************")
			input()

		else:
			print("**************************")
			print("Error - El numero de cuenta no existe")
			print("**************************")
			input()


	def pedir_datos_visualizar_cliente(self):
		system("cls")
		print("**************************")
		print("***      VISUALIZAR CLIENTE       ***")
		print("**************************")
		num_cuenta = int(input("Digite el numero de la cuenta: "))

		pos = self.banco.buscar_cuenta(num_cuenta)
		if pos != -1:
			print("**************************")
			print("Info -  El nombre del titular de la cuenta es: ", (self.banco.visualizar_cliente(num_cuenta)))
			print("**************************")
			input()

		else:
			print("**************************")
			print("Error - La cuenta no existe")
			print("**************************")
			input()



	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("**************************")
			print("**************************")
			print("*****      BANCO     *****")
			print("**************************")
			print("1: Crear Cuenta")
			print("2: Visualizar Cuenta")
			print("3: Retiro")
			print("4: Depósito")
			print("5: Consultar saldo")
			print("6: Consultar cliente")
			print("0: Salir")
			print("**************************")

			try:
				opcion = int(input("Digite la opcion: "))
				print("**************************")

				if opcion == 1:
					self.pedir_datos_cuenta()

				elif opcion == 2:
					self.pedir_datos_visualizar_cuenta()

				elif opcion == 3:
					self.pedir_datos_retiro_cuenta()

				elif opcion == 4:
					self.pedir_datos_deposito_cuenta()

				elif opcion == 5:
					self.mostrar_saldo_cuenta()

				elif opcion == 6:
					self.pedir_datos_visualizar_cliente()

				elif opcion == 0:
					break

				else:
					print("**************************")
					print("Error - Opcion no valida")
					print("**************************")
					input()

			except ValueError:
				print("**************************")
				print("Error - El dato debe ser entero")
				print("**************************")
				input()

if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()









