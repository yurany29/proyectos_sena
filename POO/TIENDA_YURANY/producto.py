class Producto:

	def __init__(self, id_producto, nombre, cantidad, valor_unitario):
		self.id_producto = id_producto
		self.nombre = nombre
		self.cantidad = cantidad
		self.valor_unitario = valor_unitario

	def mostrar_productos(self):
		print("Id del producto: ",self.id_producto)
		print("Nombre: ",self.nombre)
		print("Cantidad: ",self.cantidad)
		print("Valor unitario: ",self.valor_unitario)

	def descontar_cantidad(self, cantidad):
		if self.cantidad > 0:
			self.cantidad -= cantidad
			return True
		else:
			return False

	def get_valor_unitario(self):
		return self.valor_unitario
