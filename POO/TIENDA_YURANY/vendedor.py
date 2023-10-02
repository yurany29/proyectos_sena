class Vendedor:

	def __init__(self, id_vendedor, nombre, telefono, domicilio, edad):
		self.id_vendedor = id_vendedor
		self.nombre = nombre
		self.telefono = telefono
		self.domicilio = domicilio
		self.edad = edad

	def mostrar_vendedores(self):
		print("Id del vendedor: ",self.id_vendedor)
		print("Nombre: ",self.nombre)
		print("Telefono: ",self.telefono)
		print("Domicilio: ",self.domicilio)
		print("Edad: ",self.edad)