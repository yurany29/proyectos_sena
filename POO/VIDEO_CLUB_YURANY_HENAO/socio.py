class Socio:

	def __init__(self, codigo, nombre, telefono, direccion):
		#atributos de la clase
		#self.nombre_atributo = parametros
		self.codigo = codigo
		self.nombre = nombre
		self.telefono = telefono
		self.direccion = direccion 

	def mostrar_socio(self):
		print("Codig: ", self.codigo)
		print("Nombre completo: ", self.nombre)
		print("Telefono: ", self.telefono)
		print("Direccion: ", self.direccion)