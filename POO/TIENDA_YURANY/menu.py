from os import system
from tienda import Tienda
from producto import Producto
from vendedor import Vendedor
from venta import Venta
from datetime import datetime


class Menu:

	def __init__(self):
		self.tienda = Tienda()

	def registrar_vendedor(self):
		system("cls")
		print("|---------------------------------|")
		print("|       REGISTRAR VENDEDOR        |")
		print("|---------------------------------|")
		id_vendedor = input("Ingrese el id del vendedor: ")
		nombre = input("Ingrese el nombre del vendedor: ")
		telefono = input("Ingrese el numero telefonico del vendedor: ")
		domicilio = input("Ingrese el domicilio del vendedor: ")
		edad = input("Ingrese la edad del vendedor: ")

		vendedor = Vendedor(id_vendedor, nombre, telefono, domicilio, edad)

		if self.tienda.buscar_vendedor(id_vendedor):

			if self.tienda.crear_vendedor(vendedor):
				print("|------------------------------------------|")
				print("| Info - El vendedor se creo correctamente |")
				print("|------------------------------------------|")
				input()

			else:
				print("|--------------------------------------|")
				print("| Error - El vendedor no se pudo crear |")
				print("|--------------------------------------|")
				input()
		else:
			print("|-------------------------------|")
			print("| Error - El vendedor ya existe |")
			print("|-------------------------------|")
			input()

	def listar_vendedores(self):
		system("cls")
		print("|---------------------------------|")
		print("|        LISTAR_VENDEDORES        |")
		print("|---------------------------------|")
		self.tienda.lista_vendedores()
		input()

	def modificar_vendedor(self):
		system("cls")
		print("|---------------------------------|")
		print("|       MODIFICAR VENDEDOR        |")
		print("|---------------------------------|")
		id_vendedor = input("Ingrese el codigo del vendedor a modificar: ")

		if self.tienda.modificar_vendedor(id_vendedor):
			print("|------------------------------------------------|")
			print("|Info - Los datos del vendedor fueron modificados|")
			print("|------------------------------------------------|")
			input()

		else:
			print("|------------------------------------------------|")
			print("|Error - Los datos del vendedor no se modificaron|")
			print("|------------------------------------------------|")
			input()

	def eliminar_vendedor(self):
		system("cls")
		print("|---------------------------------|")
		print("|        ELIMINAR VENDEDOR        |")
		print("|---------------------------------|")
		id_vendedor = input("Ingrese el codigo del vendedor a eliminar: ")

		if self.tienda.eliminar_vendedor(id_vendedor):
			print("|-----------------------------------|")
			print("|Info - El vendedor ha sido eiminado|")
			print("|-----------------------------------|")
			input()

		else:
			print("|----------------------------------------|")
			print("|Error - El vendedor no se pudo elimminar|")
			print("|----------------------------------------|")
			input()
		
	def registrar_producto(self):
		system("cls")
		print("|---------------------------------|")
		print("|       REGISTRAR PRODUCTO        |")
		print("|---------------------------------|")
		id_producto = input("Ingrese el id del producto: ")
		nombre = input("Ingrese el nombre del producto: ")
		cantidad = int(input("Ingrese la cantidad del producto: "))
		valor_unitario = int(input("Ingrese el valor unitario del producto: "))

		producto = Producto(id_producto, nombre, cantidad, valor_unitario)

		if self.tienda.buscar_producto(id_producto):


			if self.tienda.agregar_producto(producto):
				print("|----------------------------------------------|")
				print("| Info - El producto se registro correctamente |")
				print("|----------------------------------------------|")
				input()

			else:
				print("|------------------------------------------|")
				print("| Error - El producto no se pudo registrar |")
				print("|------------------------------------------|")
				input()
		else:
			print("|-------------------------------|")
			print("| Error - El producto ya existe |")
			print("|-------------------------------|")
			input()


	def listar_productos(self):
		system("cls")
		print("|---------------------------------|")
		print("|        LISTAR_PRODUCTOS         |")
		print("|---------------------------------|")
		self.tienda.listar_productos()
		input()

	def modificar_productos(self):
		system("cls")
		print("|---------------------------------|")
		print("|       MODIFICAR PRODUCTOS       |")
		print("|---------------------------------|")
		id_producto = input("Ingrese el codigo del producto a modificar: ")

		if self.tienda.modificar_productos(id_producto):
			print("|------------------------------------------------|")
			print("|Info - Los datos del producto fueron modificados|")
			print("|------------------------------------------------|")
			input()

		else:
			print("|------------------------------------------------|")
			print("|Error - Los datos del producto no se modificaron|")
			print("|------------------------------------------------|")
			input()

	def eliminar_productos(self):
		system("cls")
		print("|---------------------------------|")
		print("|        ELIMINAR PRODUCTO        |")
		print("|---------------------------------|")
		id_producto = input("Ingrese el codigo del producto a eliminar: ")

		if self.tienda.eliminar_productos(id_producto):
			print("|------------------------------------|")
			print("|Info - El producto ha sido eliminado|")
			print("|------------------------------------|")
			input()

		else:
			print("|---------------------------------------|")
			print("|Error - El producto no se pudo eliminar|")
			print("|---------------------------------------|")
			input()

	def registrar_venta(self):
		system("cls")
		print("|---------------------------------|")
		print("|         REGISTRAR VENTA         |")
		print("|---------------------------------|")
		id_venta = input("Ingrese el id de la venta: ")
		dia = int(input("Ingrese el dia: "))
		mes = int(input("Ingrese el mes: "))
		anio = int(input("Ingrese el año: "))
		id_vendedor = input("Ingrese el id del vendedor: ")
		id_producto = input("Ingrese el id del producto: ")
		cantidad = int(input("Ingrese la cantidad del producto: "))
		valor_unitario = self.tienda.buscar_valor(id_producto)
		
		

		venta = Venta(id_venta, dia, mes, anio, id_vendedor, id_producto, cantidad, valor_unitario)
		pos = self.tienda.buscar_producto(id_producto)

		

		if self.tienda.buscar_venta(id_venta):

			if self.tienda.fecha(dia, mes, anio):

				if self.tienda.buscar_vendedor(id_vendedor) != -1:

					if self.tienda.buscar_producto(id_producto) != -1:
					
						if self.tienda.productos[pos].cantidad >= cantidad:
						

							if self.tienda.registrar_venta(venta):
								print("|-------------------------------------|")
								print("|Info - La venta se creo correctamente|")
								print("|-------------------------------------|")
								input()

								self.tienda.descontar_cantidad(id_producto, cantidad)

							else:
								print("|--------------------------------------|")
								print("|     Info - La venta no fue creada    |")
								print("|--------------------------------------|")
								input()

						else:
							print("|------------------------------------------------|")
							print("|Error - No hay disponibilidad/stock del producto|")
							print("|------------------------------------------------|")
							input()

					else:
						print("|-------------------------------|")
						print("| Error - El producto no existe |")
						print("|-------------------------------|")
						input()


				else:
					print("|-------------------------------|")
					print("| Error - El vendedor no existe |")
					print("|-------------------------------|")
					input()

			else:
				print("|---------------------------------|")
				print("| Error - La fecha no es valida   |")
				print("|---------------------------------|")
				input()

		else:
			print("|-----------------------------------|")
			print("|Error - El id de la venta ya existe|")
			print("|-----------------------------------|")
			input()			

	def modificar_venta(self):
		system("cls")
		print("|---------------------------------|")
		print("|         MODIFICAR VENTA         |")
		print("|---------------------------------|")
		id_venta = input("Ingrese el codigo de la venta a modificar: ")

		if self.tienda.modificar_venta(id_venta):
			print("|-----------------------------------------------|")
			print("|Info - Los datos de la venta fueron modificados|")
			print("|-----------------------------------------------|")
			input()

		else:
			print("|-----------------------------------------------|")
			print("|Error - Los datos de la venta no se modificaron|")
			print("|-----------------------------------------------|")
			input()

	def mostrar_ventas_producto(self):
		system("cls")
		print("|---------------------------------|")
		print("|       VENTAS POR PRODUCTO       |")
		print("|---------------------------------|")
		id_producto = input("Ingrese el codigo del producto a buscar: ")
		#self.tienda.total_venta(id_producto)
		pos = self.tienda.buscar_producto(id_producto)

		if pos != -1:
			print("|---------------------------------|")
			self.tienda.ventas_producto(id_producto)
			input()

		else:
			print("|---------------------------------|")
			print("|  Error - El producto no existe  |")
			print("|---------------------------------|")
			input()

	def mostrar_ventas_fecha(self):
		system("cls")
		print("|---------------------------------|")
		print("|         VENTAS POR FECHA        |")
		print("|---------------------------------|")
		dia = int(input("Ingrese el dia: "))
		mes = int(input("Ingrese el mes: "))
		anio = int(input("Ingrese el año: "))

		if self.tienda.fecha(dia, mes, anio):
			print("|---------------------------------|")
			self.tienda.ventas_fecha(dia, mes, anio)
			input()

		else:
			print("|---------------------------------|")
			print("| Error - La fecha no es valida   |")
			print("|---------------------------------|")
			input()

	def mostrar_ventas_vendedor(self):
		system("cls")
		print("|---------------------------------|")
		print("|       VENTAS POR VENDEDOR       |")
		print("|---------------------------------|")
		id_vendedor = input("Ingrese el codigo del vendedor a buscar: ")
		pos = self.tienda.buscar_vendedor(id_vendedor)

		if pos != -1:
			print("|---------------------------------|")
			self.tienda.ventas_vendedor(id_vendedor)
			input()

		else:
			print("|---------------------------------|")
			print("|  Error - El vendedor no existe  |")
			print("|---------------------------------|")
			input()
	

	def mostrar_menu_principal(self):
		while True:
			system("cls")
			print("|---------------------------------|")
			print("|              TIENDA             |")
			print("|---------------------------------|")
			print("|          MENU PRINCIPAL         |")
			print("|---------------------------------|")
			print("|1: Registrar vendedor            |")
			print("|2: Listar vendedores             |")
			print("|3: Modificar vendedor            |")
			print("|4: Eliminar vendedor             |")
			print("|5: Registrar producto            |")
			print("|6: Listar productos              |")
			print("|7: Modificar productos           |")
			print("|8: Eliminar productos            |")
			print("|9: Registrar venta               |")
			print("|10: Modificar venta              |")
			print("|11: Mostrar ventas por producto  |")
			print("|12: Mostrar ventas por fecha     |")
			print("|13: Mostrar ventas por vendedor  |")
			print("|0: Salir                         |")
			print("|---------------------------------|")

			try:

				op = int(input("Digite la opcion: "))

				if op == 1:
					self.registrar_vendedor()

				elif op == 2:
					self.listar_vendedores()

				elif op == 3:
					self.modificar_vendedor()

				elif op == 4:
					self.eliminar_vendedor()

				elif op == 5:
					self.registrar_producto()

				elif op == 6:
					self.listar_productos()

				elif op == 7:
					self.modificar_productos()

				elif op == 8:
					self.eliminar_productos()

				elif op == 9:
					self.registrar_venta()

				elif op == 10:
					self.modificar_venta()

				elif op == 11:
					self.mostrar_ventas_producto()

				elif op == 12:
					self.mostrar_ventas_fecha()

				elif op == 13:
					self.mostrar_ventas_vendedor()

				elif op == 0:
					break

				else:
					print("|-------------------------------|")
					print("|    Error - opcion no valida   |")
					print("|-------------------------------|")


			except ValueError:
				print("|-----------------------------------|")
				print("|  Error - El dato debe ser entero  |")
				print("|-----------------------------------|")
				input()


if __name__ == '__main__':
	menu = Menu()
	menu.mostrar_menu_principal()