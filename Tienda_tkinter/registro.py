from tkinter import * 
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from subprocess import call
import sys 

class Registro:

	db_name = 'db_proyecto_tienda.db'

	def __init__(self, ventana_registro):

		'''---------------Window attributes----------------'''

		# The window is created.
		self.window = ventana_registro 
		# The title is added.
		self.window.title("FORMULARIO DE REGISTRO") 
		# The size is determined.
		self.window.geometry("390x630") 
		# Insert icon image.
		self.window.iconbitmap("C:/Users/YURANY HENAO/Desktop/Tienda2/img/foto_tienda.ico") 
		self.window.resizable(1,1) #Manipular eltamaño de la ventana.

		'''----------------Titulo de la ventana---------------------'''

		titulo = Label(ventana_registro, text="REGISTRO DE USUARIO", fg="black", font=("Comic Sans", 14, "bold"),pady=10).pack()# pack: empaquetar


		'''----------------Logo del Login---------------------------'''

		imagen_registro = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/login_icon_176905.png") #
		nueva_imagen = imagen_registro.resize((40,40))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(ventana_registro, image=render)
		label_imagen.image = render
		label_imagen.pack(pady=5)

		'''---------------Ventana de registro-----------------------'''
		marco = LabelFrame(ventana_registro, text="Datos Personales", font=("Comic Sans", 10, "bold"))
		marco.pack()

		'''----------------Formulario del registro------------------'''
		label_usuario = Label(marco, text="Usuario: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky="s", padx=5, pady=8)
		self.usuario = Entry(marco, width=25)
		self.usuario.focus()
		self.usuario.grid(row=0, column=1, padx=5, pady=8)

		'''----------------Nombre---------------------------------'''
		label_nombre = Label(marco, text="Nombre: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky="s", padx=5, pady=8)
		self.nombres = Entry(marco, width=25)
		self.nombres.grid(row=1, column=1, padx=5, pady=8)

		'''-----------------Apellido-----------'''

		label_apellido = Label(marco, text="Apellido: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky="s", padx=5, pady=8)
		self.apellidos = Entry(marco, width=25)
		self.apellidos.grid(row=2, column=1, padx=5, pady=8)

		'''----------------Genero------------'''

		label_genero = Label(marco, text="Genero: ", font=("Comic Sans", 10, "bold")).grid(row=3, column=0, sticky="s", padx=5, pady=8)
		self.combo_genero = ttk.Combobox(marco, values=["Masculino", "Femenino"], width=22, state="readonly") # state="Readonly" sirve solo para lectura
		self.combo_genero.current(0) # Para posicionarse en el primer valor de la lista.
		self.combo_genero.grid(row=3, column=1, padx=10, pady=8)

		'''-----------------Edad---------------------------------'''

		label_edad = Label(marco, text="Edad: ", font=("Comic Sans", 10, "bold")).grid(row=4, column=0, sticky="s", padx=5, pady=8)
		self.edad = Entry(marco, width=25)
		self.edad.grid(row=4, column=1, padx=5, pady=8)

		'''----------------Correo-----------'''

		label_correo = Label(marco, text="Correo: ", font=("Comic Sans", 10, "bold")).grid(row=5, column=0, sticky="s", padx=5, pady=8)
		self.correo = Entry(marco, width=25)
		self.correo.grid(row=5, column=1, padx=5, pady=8)

		'''----------------Password------------------'''

		label_password = Label(marco, text="Password: ", font=("Comic Sans", 10, "bold")).grid(row=6, column=0, sticky="s", padx=5, pady=8)
		self.password = Entry(marco, width=25)
		self.password.grid(row=6, column=1, padx=5, pady=8)

		'''---------------Repetir password-----------'''

		label_repetir_password = Label(marco, text="Confirmar Password: ", font=("Comic Sans", 10, "bold")).grid(row=7, column=0, sticky="s", padx=5, pady=8)
		self.repetir_password = Entry(marco, width=25)
		self.repetir_password.grid(row=7, column=1, padx=5, pady=8)



		'''-----------------Marco Pregunta del Registro--------------'''

		marco_pregunta = LabelFrame(ventana_registro, text="¿Olvido su password?", font=("Comic Sans", 10, "bold"),pady=8)
		marco_pregunta.pack()

		label_pregunta = Label(marco_pregunta, text="preguntas",font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky="s", padx=5, pady=8)
		self.combo_pregunta = ttk.Combobox(marco_pregunta, values=["Nombre primera mascota", "Nombre colegio", "Ciudad de nacimiento", "Nombre deporte favorito"], width=30, state="readonly")
		self.combo_pregunta.current(0)
		self.combo_pregunta.grid(row=0, column=1, padx=10, pady=8)

		label_respuesta = Label(marco_pregunta, text="Respuesta: ",font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky="s", padx=10, pady=8)
		self.respuesta_pregunta = Entry(marco_pregunta, width=33)
		self.respuesta_pregunta.grid(row=1, column=1, padx=10, pady=8)

		'''--------------Frame de los botones del registro---------------'''
		frame_botones = Frame(ventana_registro)
		frame_botones.pack()


		boton_registrar = Button(frame_botones, text="REGISTRAR", command=self.registrar_usuario, height=2, width=12, bg="green", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=1, padx=10, pady=15)
		boton_limpiar = Button(frame_botones, text="LIMPIAR", height=2, command= self.limpiar_formulario, width=9, bg="orange", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=2, padx=10, pady=15)
		boton_login = Button(frame_botones, text="LOGIN", height=2, command= self.llamar_login, width=9, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=3, padx=10, pady=15)
		boton_cancelar = Button(frame_botones, text="CANCELAR", height=2, command= ventana_registro.quit, width=9, bg="red", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=4, padx=10, pady=15)

	def registrar_usuario(self):
		if self.validar_formulario() and self.validar_password() and self.validar_usuario():
			query = 'INSERT INTO usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
			parameters = (self.usuario.get(), self.nombres.get(), self.apellidos.get(), self.combo_genero.get(), self.edad.get(), self.correo.get(), self.password.get(), self.respuesta_pregunta.get(), )
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("Registro Exitoso",f"Bienvenid@ {self.nombres.get()}{self.apellidos.get()}")
			self.limpiar_formulario()

	def validar_formulario(self):
		if len(self.usuario.get()) != 0 and len(self.nombres.get()) != 0 and len(self.apellidos.get()) != 0 and  len(self.combo_genero.get()) != 0 and len(self.edad.get()) != 0 and len(self.correo.get()) != 0 and len(self.password.get()) != 0 and len(self.repetir_password.get()) != 0 and len(self.respuesta_pregunta.get()) != 0:
			return True 

		else:
			messagebox.showerror("Error en el registro", "Diligencie todos los campos del formulario")

	def validar_password(self):
		if (str(self.password.get())) == (str(self.repetir_password.get())):
			return True 
		else:
			messagebox.showerror("Error la contraseña no es valida.")

	def validar_usuario(self):
		usuario = self.usuario.get()
		dato = self.buscar_usuario(usuario)
		#Si dato se encuentra vacio, el usuario no existe.
		if dato == []:
			return True 

		else:
			messagebox.showerror("Error en registro", "Usuario ya se encuentra registrado")

	def limpiar_formulario(self):
		self.usuario.delete(0, END)
		self.nombres.delete(0, END)
		self.apellidos.delete(0, END)
		self.combo_genero.delete(0, END)
		self.edad.delete(0, END)
		self.correo.delete(0, END)
		self.password.delete(0, END)
		self.repetir_password.delete(0, END)
		self.combo_pregunta.delete(0, END)
		self.respuesta_pregunta.delete(0, END)

	def ejecutar_consulta(self, query, parameters=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			conexion.commit() #Commit actualiza cambios

		return result

	def buscar_usuario(self, usuario):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			sql = "SELECT * FROM  usuarios WHERE usuario = {}".format(usuario)
			cursor.execute(sql)
			usuario_consulta = cursor.fetchall()# va obtener la informacion que esta en usuarios como una lista. si vuelve vacio el usuario se puede registrar
			cursor.close()
		return usuario_consulta
	
	def llamar_login(self):
		#Se destruye la ventana de registro.
		ventana_registro.destroy()
		#Se invoca el archivo login.py
		call([sys.executable, 'login.py'])



		



		

if __name__ == '__main__':
	ventana_registro = Tk()
	application = Registro(ventana_registro)
	ventana_registro.mainloop()