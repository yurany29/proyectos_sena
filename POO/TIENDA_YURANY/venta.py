from datetime import datetime
class Venta:

	def __init__(self, id_venta, dia, mes, anio, id_vendedor, id_producto, cantidad, valor_unitario):
		self.id_venta = id_venta
		self.dia = dia
		self.mes = mes
		self.anio = anio
		self.id_vendedor = id_vendedor  
		self.id_producto = id_producto
		self.cantidad = cantidad
		self.valor_unitario = valor_unitario
		self.total  = []
		#self.total_venta = total_venta
		#self.ventas_producto = []
		#productos = []

	def mostrar_ventas_producto(self):
		print("Id de la venta: ",self.id_venta)
		print("Id del vendedor: ",self.id_vendedor)
		print("Fecha: {}/{}/{}".format(self.dia, self.mes, self.anio))
		print("Id del producto: ",self.id_producto)
		print("Cantidad: ",self.cantidad)
		print("Total de la venta: ",self.total_venta())
		print("|---------------------------------|")


	def total_venta(self):
		total = self.cantidad * self.valor_unitario
		self.total.append(total)
		return total

	def mostrar_ventas_fecha(self):
		print("Id de la venta: ",self.id_venta)
		print("Fecha: {}/{}/{}".format(self.dia, self.mes, self.anio))
		print("Id del producto: ",self.id_producto)
		print("Cantidad: ",self.cantidad)
		print("Id del vendedor: ",self.id_vendedor)
		print("Total de la venta: ",self.total_venta())
		print("|---------------------------------|")

	def mostrar_ventas_vendedor(self):
		print("Id de la venta: ",self.id_venta)
		print("Fecha: {}/{}/{}".format(self.dia, self.mes, self.anio))
		print("Id del producto: ",self.id_producto)
		print("Cantidad: ",self.cantidad)
		print("Id del vendedor: ",self.id_vendedor)
		print("Total de la venta: ",self.total_venta())
		print("|---------------------------------|")



