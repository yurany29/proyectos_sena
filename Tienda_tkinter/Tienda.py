from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import sys 
from tkinter import messagebox
import sqlite3

class Productos:

	db_name = 'db_proyecto_tienda.db'

	def __init__(self, ventana_productos):

		'''-----------------Atributos de la ventana -----------------'''
		menubar = Menu(ventana_productos)
		ventana_productos.title("Tienda")
		ventana_productos.geometry("800x670")
		ventana_productos.iconbitmap("C:/Users/YURANY HENAO/Desktop/Tienda2/img/foto_tienda.ico")
		ventana_productos.resizable(0,0)
		ventana_productos.config(menu=menubar) #Agregar un menu a la ventana desplegable

		'''---------------- Menu de la ventana------------------------------'''

		Productos = Menu(menubar, tearoff=0) #
		Clientes = Menu(menubar, tearoff=0)
		Ventas = Menu(menubar, tearoff=0)
		Informacion = Menu(menubar, tearoff=0)


		#Agregamos los elementos del menu (opciones) en cascada
		menubar.add_cascade(label="Productos", menu=Productos)
		menubar.add_cascade(label="Clientes", menu=Clientes)
		menubar.add_cascade(label="Ventas", menu=Ventas)
		menubar.add_cascade(label="Ayuda", menu=Informacion)

		#Iconos del menu 
		self.img_registrar = PhotoImage(file="C:/Users/YURANY HENAO/Desktop/Tienda2/img/registro.png")
		self.img_buscar = PhotoImage(file="C:/Users/YURANY HENAO/Desktop/Tienda2/img/buscar.png")
		self.img_informacion = PhotoImage(file="C:/Users/YURANY HENAO/Desktop/Tienda2/img/informacion.png")
		self.img_venta = PhotoImage(file="C:/Users/YURANY HENAO/Desktop/Tienda2/img/venta.png")
		self.img_cliente = PhotoImage(file="C:/Users/YURANY HENAO/Desktop/Tienda2/img/clientes.png")

		#Acciones del menu
		self.boton_registrar = Productos.add_command(label="Registrar", command=self.widgets_crud, image=self.img_registrar, compound=LEFT)
		self.boton_buscar_cliente = Clientes.add_command(label="Buscar", command=self.widgets_buscador_cliente, image=self.img_buscar, compound=LEFT)
		self.boton_buscar = Productos.add_command(label="Buscar", command=self.widgets_buscador, image=self.img_buscar, compound=LEFT)
		self.boton_informacion = Informacion.add_command(label="Informacion del sistema", command=self.widgets_informacion, image=self.img_informacion, compound=LEFT)
		self.boton_clientes = Clientes.add_command(label="Clientes", command=self.widgets_crud_cliente, image=self.img_cliente, compound=LEFT)
		self.boton_registrar_venta = Ventas.add_command(label="Registrar", command=self.widgets_crud_venta, image=self.img_venta, compound=LEFT)
		self.boton_buscar_venta = Ventas.add_command(label="Buscar", command=self.widgets_buscador_venta, image=self.img_buscar, compound=LEFT)
		'''-----------------Widgets del Menu -------------------------------'''

		#Widgets crud
		self.label_titulo_crud = LabelFrame(ventana_productos)
		self.frame_logos_productos = LabelFrame(ventana_productos)
		self.frame_registro = LabelFrame(ventana_productos, text="Informacion del producto",font=("Comic Sans", 10, "bold"),pady=5)
		self.frame_botones_registro = LabelFrame(ventana_productos)
		self.frame_tabla_crud = LabelFrame(ventana_productos)

		#Widgets buscador
		self.label_titulo_buscador = LabelFrame(ventana_productos)
		self.frame_buscar_producto = LabelFrame(ventana_productos, text="Buscar producto", font=("Comic Sans", 10, "bold"),pady=10)
		self.frame_boton_buscar = LabelFrame(ventana_productos)

		#Widgets buscador cliente
		self.label_titulo_buscador_cliente = LabelFrame(ventana_productos)
		self.frame_buscar_cliente = LabelFrame(ventana_productos, text="Buscar cliente", font=("Comic Sans", 10, "bold"),pady=10)
		self.frame_boton_buscar_cliente = LabelFrame(ventana_productos)

		#Widgets buscador ventas

		self.label_titulo_buscador_ventas = LabelFrame(ventana_productos)
		self.frame_buscar_venta = LabelFrame(ventana_productos, text="Buscar ventas", font=("Comic Sans", 10, "bold"),pady=10)
		self.frame_boton_buscar_venta = LabelFrame(ventana_productos)

		#Widgets informacion
		self.label_informacion = LabelFrame(ventana_productos)

		#Widgets crud venta
		self.label_titulo_venta = LabelFrame(ventana_productos)
		self.frame_logo_venta = LabelFrame(ventana_productos)
		self.frame_registro_venta = LabelFrame(ventana_productos, text="Informacion de la venta", font=("Comic Sans", 10, "bold"),pady=5)
		self.frame_botones_venta = LabelFrame(ventana_productos)
		self.frame_tabla_venta = LabelFrame(ventana_productos)
		
		
		#Widgets crud cliente
		self.label_titulo_cliente = LabelFrame(ventana_productos)
		self.frame_logo_cliente = LabelFrame(ventana_productos)
		self.frame_registro_cliente = LabelFrame(ventana_productos, text="Informacion de clientes", font=("Comic Sans", 10, "bold"),pady=5)
		self.frame_botones_cliente = LabelFrame(ventana_productos)
		self.frame_tabla_clientes = LabelFrame(ventana_productos)




		#Pantalla inicial
		self.widgets_crud()





	def widgets_crud(self):
		# que se inicie el sistema se carga el crud
		self.label_titulo_crud.config(bd=0)
		self.label_titulo_crud.grid(row=0, column=0)

		'''----------------Titulo de la ventana--------------'''
		self.titulo_crud = Label(self.label_titulo_crud, text="LISTA DE PRODUCTOS", fg="black", font=("Comic Sans MS", 13, "bold"),pady=10)
		self.titulo_crud.grid(row=0, column=0)

		'''----------------Frame de los productos-------------'''
		self.frame_logos_productos.grid(row=1, column=0, padx=5, pady=5)

		'''---------------Logo de la ventana------------------'''
		imagen_pc = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/pc.png")
		nueva_imagen = imagen_pc.resize((60, 60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=0, padx=15, pady=5)

		imagen_mouse = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/mouse.png")
		nueva_imagen = imagen_mouse.resize((60, 60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=1, padx=15, pady=5)

		imagen_portatil = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/portatil-removebg-preview.png")
		nueva_imagen = imagen_portatil.resize((60, 60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=2, padx=15, pady=5)

		imagen_teclado = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/teclado.png")
		nueva_imagen = imagen_teclado.resize((60, 60))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.frame_logos_productos, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=3, padx=15, pady=5)

		'''----------------Marco de la ventana -----------------'''
		self.frame_registro.grid(row=2, column=0, padx=50, pady=5)

		'''----------------Formulario de la ventana ------------'''
		label_codigo = Label(self.frame_registro, text="Codigo del producto", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		self.codigo = Entry(self.frame_registro, width=25)
		self.codigo.focus()
		self.codigo.grid(row=0, column=1, padx=5,  pady=10)

		label_categoria = Label(self.frame_registro, text="Categorias del producto", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		self.combo_categoria = ttk.Combobox(self.frame_registro, values=["Computadores", "Perifericos"], width=22, state="readonly")
		self.combo_categoria.current(0)
		self.combo_categoria.grid(row=0, column=3, padx=5, pady=8)



		label_nombre_producto = Label(self.frame_registro, text="Nombre del producto", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		self.nombre_producto = Entry(self.frame_registro, width=25)
		self.nombre_producto.grid(row=1, column=1, padx=5,  pady=10)

		label_descripcion = Label(self.frame_registro, text="Descripcion del producto", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		self.descripcion = Entry(self.frame_registro, width=25)
		self.descripcion.grid(row=1, column=3, padx=5,  pady=10)

		label_cantidad = Label(self.frame_registro, text="Cantidad del producto", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		self.cantidad_producto = Entry(self.frame_registro, width=25)
		self.cantidad_producto.grid(row=2, column=1, padx=5,  pady=10)

		label_precio = Label(self.frame_registro, text="Precio del producto", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		self.precio = Entry(self.frame_registro, width=25)
		self.precio.grid(row=2, column=3, padx=5,  pady=10)

		'''----------------------Frame de los botones--------------------'''
		self.frame_botones_registro.grid(row=3, column=0, padx=5, pady=5)

		boton_registrar = Button(self.frame_botones_registro, text="REGISTRAR", height=2, command= self.agregar_producto, width=10, bg="green", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=0, padx=10, pady=15)
		boton_editar = Button(self.frame_botones_registro, text="EDITAR", height=2, command= self.editar_producto, width=10, bg="orange", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=1, padx=10, pady=15)
		boton_eliminar = Button(self.frame_botones_registro, text="ELIMINAR", height=2, command= self.eliminar_productos, width=10, bg="red", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=3, padx=10, pady=15)
		boton_salir = Button(self.frame_botones_registro, text="SALIR", height=2, command=ventana_productos.quit, width=10, bg="lightseagreen", fg="white", font=("Comic Sans MS", 9, "bold")).grid(row=0, column=2, padx=10, pady=15)
		


		'''---------------------Tabla con la lista de productos ----------------'''

		self.frame_tabla_crud.grid(row=4, column=0, padx=5, pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_crud, height=13, columns=("columna1", "columna2", "columna3", "columna4", "columna5"))

		self.tree.heading("#0", text="Codigo", anchor=CENTER) # Encabezado anchor Centrar infrmacion
		self.tree.column("#0", width=90, minwidth=75, stretch=False) # stretch= Manipular la columna

		self.tree.heading("columna1", text='Nombre', anchor=CENTER)
		self.tree.column("columna1", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna2", text='Categoria', anchor=CENTER)
		self.tree.column("columna2", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna3", text='Cantidad', anchor=CENTER)
		self.tree.column("columna3", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna4", text='Precio', anchor=CENTER)
		self.tree.column("columna4", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna5", text='Descripcion', anchor=CENTER)
		self.tree.column("columna5", width=150, minwidth=75, stretch=False)

		#Se crearon las columnas y los titulos de la columna.
		self.tree.grid(row=0, column=0, sticky=E)
		self.listar_productos()
		self.widgets_buscador_remove()
		self.widgets_crud_cliente_remove()
		self.frame_tabla_clientes.grid_remove()
		self.frame_tabla_venta.grid_remove()
		self.widgets_crud_ventas_remove()
		self.widgets_buscador_cliente_remove()
		self.widgets_buscador_venta_remove()
		self.label_informacion.grid_remove()
		




 	

	def widgets_buscador(self):
 		#Se carga el buscador
		self.label_titulo_buscador.config(bd=0)
		self.label_titulo_buscador.grid(row=0, column=0, padx=5, pady=5)

		'''--------------------------Titulo-------------------------'''
		self.titulo_buscador = Label(self.label_titulo_buscador, text="BUSCADOR DE PRODUCTOS", fg="black", font=("Comic Sans", 17, "bold"))
		self.titulo_buscador.grid(row=0, column=0)

		'''-------------------------- Frame buscar -----------------'''
		self.frame_buscar_producto.config(bd=2)
		self.frame_buscar_producto.grid(row=2, column=0, padx=5, pady=5)

		'''-------------------------- Formulario buscar --------------'''
		self.label_buscar = Label(self.frame_buscar_producto, text="Buscar por: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=5)
		self.combo_buscar = ttk.Combobox(self.frame_buscar_producto, values=["codigo", "nombre"], width=22, state="readonly")
		self.combo_buscar.current(0)
		self.combo_buscar.grid(row=0, column=1, padx=5, pady=5)

		label_codigo_codigo = Label(self.frame_buscar_producto, text="Codigo / Nombre del producto: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=5)
		self.codigo_nombre = Entry(self.frame_buscar_producto, width=25)
		self.codigo_nombre.focus()
		self.codigo_nombre.grid(row=0, column=3, padx=10, pady=5)

		'''---------------------- Frame marco --------------------------'''
		self.frame_boton_buscar.config(bd=0)
		self.frame_boton_buscar.grid(row=3, column=0, padx=5, pady=5)

		'''----------------------- Boton ------------------------------'''
		self.boton_buscar = Button(self.frame_boton_buscar, text="BUSCAR", command=self.buscar_productos, height=2, width=20, bg="black", fg="white", font=("Comic Sans", 10, "bold"))
		self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

		#Se carga la tabla pero sin datos
		self.tree.delete(*self.tree.get_children())

	
		#REMOVER OTROS WIDGETS de otros formularios
		self.widgets_crud_cliente_remove()
		self.widgets_crud_ventas_remove()
		self.widgets_crud_remove()
		self.frame_tabla_clientes.grid_remove()
		self.frame_tabla_venta.grid_remove()
		self.widgets_buscador_cliente_remove()
		self.widgets_buscador_venta_remove()
		self.label_informacion.grid_remove()
		
		

	def widgets_crud_remove(self):
		#remove permite que al cambiar de una ventana a otra se limpie(cargue la nueva ventana solicitada, pasara de registro a buscar o viceversa)
		#Se limpia label y se carga los nuevo
		self.label_titulo_crud.grid_remove()
		self.frame_registro.grid_remove()
		self.frame_botones_registro.grid_remove()
		self.frame_logos_productos.grid_remove()
		#self.frame_tabla_crud.grid_remove()

	def widgets_buscador_remove(self):
		self.label_titulo_buscador.grid_remove()
		self.frame_buscar_producto.grid_remove()
		self.frame_boton_buscar.grid_remove()


	def widgets_informacion(self):
		#Se ocultan los frame de los logos y de la tabla para que no carguen en ayuda
		self.frame_logos_productos.grid_forget()
		self.frame_tabla_crud.grid_forget()
		self.label_informacion.config(bd=0)
		self.label_informacion.grid(row=0, column=0)

		'''----------------------------Titulo -------------------------'''
		self.label_titulo = Label(self.label_informacion, text="APLICACION DE ESCRITORIO", fg="white", bg="black", font=("Comic Sans", 25, "bold"), padx=137, pady=20)
		self.label_titulo.grid(row=0, column=0)

		'''--------------------------- Logo imagenes ------------------'''
		#Logo
		imagen_soporte = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/soporte.png")
		nueva_imagen = imagen_soporte.resize((170,170))
		render = ImageTk.PhotoImage(nueva_imagen)
		label_imagen = Label(self.label_informacion, image = render)
		label_imagen.image = render
		label_imagen.grid(row=1, column=0, padx=10, pady=15)

		'''--------------------------- Opciones -------------------------'''
		self.label_titulo = Label(self.label_informacion, text="> Codigo de Tienda de Tecnologia", fg="black", font=("Comic Sans", 18, "bold"))
		self.label_titulo.grid(row=2, column=0, sticky=W, padx=30, pady=10)

		self.label_titulo = Label(self.label_informacion, text="> En esta tienda encontraras productos de tecnologia", fg="black", font=("Comic Sans", 18, "bold"))
		self.label_titulo.grid(row=3, column=0, sticky=W, padx=30, pady=10)

		self.label_titulo = Label(self.label_informacion, text="> Aprendices Jhon Faver Alvarez - Yurany Henao", fg="black", font=("Comic Sans", 18, "bold"))
		self.label_titulo.grid(row=4, column=0, sticky=W, padx=30, pady=10)

		self.label_titulo = Label(self.label_informacion, text="Creado por Jhon Faver - Yurany Henao - Ficha 2560119 Tgo ADSO - 2023", fg="black", font=("Comic Sans", 10, "bold"))
		self.label_titulo.grid(row=6, column=0, pady=60)

		#Remove de las otras ventanas para cargar la nueva 
		self.widgets_crud_cliente_remove()
		self.widgets_crud_ventas_remove()
		self.widgets_buscador_remove()
		self.widgets_crud_remove()
		self.widgets_buscador_venta_remove()
		self.widgets_buscador_cliente_remove()
		self.frame_tabla_venta.grid_remove()
		self.frame_tabla_clientes.grid_remove()

	def agregar_producto(self):
		if self.validar_formulario_completo():
			query = 'INSERT INTO productos VALUES(NULL, ?, ?, ?, ?, ?, ?)'
			parameters = (self.codigo.get(), self.nombre_producto.get(), self.combo_categoria.get(), self.cantidad_producto.get(), self.precio.get(), self.descripcion.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("REGISTRO EXITOSO", f'Producto registrado: {self.nombre_producto.get()}')
		self.limpiar_formulario()
		self.listar_productos()

	def validar_formulario_completo(self):
		if len(self.codigo.get()) != 0 and len(self.nombre_producto.get()) != 0 and len(self.combo_categoria.get()) != 0 and len(self.cantidad_producto.get()) != 0 and len(self.precio.get()) != 0 and len(self.descripcion.get()) != 0:
			return True 
		else:
			messagebox.showerror("ERROR", "Complete todos los campos del formulario") 

	def ejecutar_consulta(self, query, parameters=()):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			result = cursor.execute(query, parameters)
			conexion.commit()
		return result
	
	def limpiar_formulario(self):
		self.codigo.delete(0, END)
		self.nombre_producto.delete(0, END)
		self.cantidad_producto.delete(0, END)
		self.precio.delete(0, END)
		self.descripcion.delete(0, END)

	def listar_productos(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)

		query = 'SELECT * FROM productos ORDER BY nombre DESC'
		db_rows = self.ejecutar_consulta(query)
		for row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))

	def eliminar_productos(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]

		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un producto de la tabla.")
		dato = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM productos WHERE codigo = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Esta seguro que desea eliminar el producto: {nombre}?")
		if respuesta == 'yes':
			self.ejecutar_consulta(query, (dato,))
			self.listar_productos()
			messagebox.showinfo('EXITO', f'Producto eliminado:  {nombre}')
		else:
			messagebox.showerror('ERROR', f'Error al eliminar el producto: {nombre}')

	def editar_producto(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un producto de la tabla.")

		codigo = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		categoria = self.tree.item(self.tree.selection())['values'][1]
		cantidad = self.tree.item(self.tree.selection())['values'][2]
		precio = self.tree.item(self.tree.selection())['values'][3]
		descripcion = self.tree.item(self.tree.selection())['values'][4]

		self.ventana_editar = Toplevel()
		self.ventana_editar.title("EDITAR PRODUCTO")
		#Incluir icono a la ventana
		self.ventana_editar.iconbitmap("C:/Users/YURANY HENAO/Desktop/Tienda2/img/foto_tienda.ico")
		#Modificar o no las dimenciones de la ventana
		self.ventana_editar.resizable(0,0)

		label_codigo = Label(self.ventana_editar, text="Codigo del producto: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo), width=25)
		nuevo_codigo.grid(row=0, column=1, padx=5, pady=8)

		label_categoria = Label(self.ventana_editar, text="Categoria", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_combo_categoria = ttk.Combobox(self.ventana_editar, values=["Computadores", "Perifericos"], width=22, state="readonly")
		nuevo_combo_categoria.set(categoria)
		nuevo_combo_categoria.grid(row=0, column=3, padx=5, pady=0)

		label_nombre = Label(self.ventana_editar, text="Nombre del producto: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		nuevo_nombre = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=nombre), width=25)
		nuevo_nombre.grid(row=1, column=1, padx=5, pady=0)

		label_descripcion = Label(self.ventana_editar, text="Descripcion: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nueva_descripcion = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=descripcion), width=25)
		nueva_descripcion.grid(row=1, column=3, padx=5, pady=0)

		label_cantidad = Label(self.ventana_editar, text="Cantidad:", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nueva_cantidad = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=cantidad), width=25)
		nueva_cantidad.grid(row=2, column=1, padx=5, pady=0)

		label_precio = Label(self.ventana_editar, text="Precio: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		nuevo_precio = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=precio), width=25)
		nuevo_precio.grid(row=2, column=3, padx=5, pady=0)

		boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR", command=lambda:self.actualizar(nuevo_codigo.get(), nuevo_nombre.get(), nuevo_combo_categoria.get(), nueva_cantidad.get(), nuevo_precio.get(), nueva_descripcion.get(), codigo), height=2, width=20, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar.mainloop()


	def actualizar(self, nuevo_codigo, nuevo_nombre, nuevo_combo_categoria, nueva_cantidad, nuevo_precio, nueva_descripcion, codigo):
		query = 'UPDATE productos SET codigo = ?, nombre = ?, categoria = ?, cantidad = ?, precio = ?, descripcion = ? WHERE codigo = ? '
		parameters = (nuevo_codigo, nuevo_nombre, nuevo_combo_categoria, nueva_cantidad, nuevo_precio, nueva_descripcion, codigo)
		self.ejecutar_consulta(query, parameters)
		messagebox.showinfo('EXITO',f'Producto Actualizado: {nuevo_nombre}')
		self.ventana_editar.destroy()
		self.listar_productos()

	def buscar_productos(self):
		if(self.validar_busqueda()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			if (self.combo_buscar.get() == 'codigo'):
				#sentencia SQL LIKE-> inicie por una letra o varias o completas
				query = ("SELECT * FROM Productos WHERE codigo LIKE ? ")
				#% permite realizar la busqueda sin tener completa del codigo a buscar (busqueda parcial de la palabra y luego clic en buscar)
				parameters = (self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parameters,))

				for row in db_rows:
					self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))

				if(list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR","Producto no encontrado")
			else:
				#sentencia SQL LIKE-> inicie por
				query = ("SELECT * FROM Productos WHERE nombre LIKE ? ")
				#% permite realizar la busqueda sin tener completa del nombre a buscar (busqueda parcial de la palabra y luego clic en buscar)
				parameters = ("%"+self.codigo_nombre.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parameters,))

				for row in db_rows:
					self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))

				if(list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR","Producto no encontrado")

	def validar_busqueda(self):
		if len(self.codigo_nombre.get()) !=0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR", "Complete todos los campos para la busqueda")
   
	'''-----------------------------------clientes----------------------------------------------'''
	def widgets_crud_cliente(self):

		self.frame_logos_productos.grid_forget()
		self.frame_tabla_crud.grid_forget()
		self.label_informacion.config(bd=0)
		self.label_informacion.grid(row=0, column=0)
		
		
		self.label_titulo_cliente.config(bd=0)
		self.label_titulo_cliente.grid(row=0, column=0, padx=5, pady=5)

		'''--------------------------Titulo de la ventana-------------------------------'''
		self.titulo_cliente = Label(self.label_titulo_cliente, text="REGISTRO DE CLIENTES", fg="black", font=("Comic Sans", 13, "bold"),pady=10)
		self.titulo_cliente.grid(row=0, column=0)

		'''--------------------------Frame del cliente----------------------------'''
		self.frame_logo_cliente.grid(row=1, column=0, padx=5, pady=5)
		
		'''--------------------------Logo de la venta cliente---------------------'''
		img_cliente = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/logo cliente.png")
		nueva_img_cliente = img_cliente.resize((60,60))
		render = ImageTk.PhotoImage(nueva_img_cliente)
		label_imagen_cliente = Label(self.frame_logo_cliente, image=render)
		label_imagen_cliente.image = render
		label_imagen_cliente.grid(row=2, column=0, padx=15, pady=5)
		
		'''------------------------Marco de la ventana cliente------------------------------'''
		self.frame_registro_cliente.grid(row=2, column=0, padx=50, pady=5)

		'''-----------------------Fromulario del cliente--------------------------------------------'''
		label_codigo_cliente = Label(self.frame_registro_cliente, text="ID del cliente", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		self.codigo_cliente = Entry(self.frame_registro_cliente, width=25)
		self.codigo_cliente.focus()
		self.codigo_cliente.grid(row=0, column=1, padx=5, pady=10)

		label_nombre_cliente = Label(self.frame_registro_cliente, text="Nombre del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		self.nombre_cliente = Entry(self.frame_registro_cliente, width=25)
		self.nombre_cliente.grid(row=1, column=1, padx=5, pady=10)

		label_telefono_cliente = Label(self.frame_registro_cliente, text="Telefono: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		self.telefono_cliente = Entry(self.frame_registro_cliente, width=25)
		self.telefono_cliente.grid(row=0, column=3, padx=5, pady=10)

		label_direccion_cliente = Label(self.frame_registro_cliente, text="Direccion: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		self.direccion_cliente = Entry(self.frame_registro_cliente, width=25)
		self.direccion_cliente.grid(row=2, column=1, padx=5, pady=10)

		label_correo_cliente = Label(self.frame_registro_cliente, text="Correo: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		self.correo_cliente = Entry(self.frame_registro_cliente, width=25)
		self.correo_cliente.grid(row=1, column=3, padx=5, pady=10)

		'''-------------------------Frame botones----------------------------------'''
		self.frame_botones_cliente.grid(row=3, column=0, padx=5, pady=5)

		'''-------------------------Botones del cliente----------------------------'''
		boton_registrar_cliente = Button(self.frame_botones_cliente, text="REGISTRAR", height=2, command=self.agregar_cliente, width=10, bg="green", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=0, padx=10, pady=15)
		boton_editar_cliente = Button(self.frame_botones_cliente, text="EDITAR", height=2, command=self.editar_cliente, width=10, bg="blue", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=1, padx=10, pady=15)
		boton_salir_cliente = Button(self.frame_botones_cliente, text="SALIR", height=2, command=ventana_productos.quit,  width=10, bg="purple", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=2, padx=10, pady=15)
		boton_eliminar_cliente = Button(self.frame_botones_cliente, text="ELIMINAR", height=2, command=self.eliminar_clientes, width=10, bg="red", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=3, padx=10, pady=15)

		'''----------------------Tabla con la lista de clientes-----------------------'''
		self.frame_tabla_clientes.grid(row=4, column=0, padx=5, pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_clientes, height=13, columns=("columna1", "columna2", "columna3", "columna4"))

		self.tree.heading("#0", text="ID Cliente", anchor=CENTER)
		self.tree.column("#0", width=90, minwidth=75, stretch=False)

		self.tree.heading("columna1", text="Nombre Cliente", anchor=CENTER)
		self.tree.column("columna1", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna2", text="Telefono", anchor=CENTER)
		self.tree.column("columna2", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna3", text="Direccion", anchor=CENTER)
		self.tree.column("columna3", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna4", text="Correo", anchor=CENTER)
		self.tree.column("columna4", width=70, minwidth=75, stretch=False)

		self.tree.grid(row=0, column=0, sticky=E)


		'''Acaaaa tambienpuseee removessss'''
		#Limpia las ventanas 
		self.widgets_crud_ventas_remove()
		self.widgets_buscador_remove()
		self.widgets_crud_remove()
		self.label_informacion.grid_remove()
		self.listar_clientes()
		self.widgets_buscador_cliente_remove()
		self.widgets_buscador_venta_remove()
		self.frame_tabla_venta.grid_remove()
		self.frame_tabla_crud.grid_remove()



	def agregar_cliente(self):
		if self.validar_formulario_completo_cliente():
			query = 'INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?, ?)'
			parameters = (self.codigo_cliente.get(), self.nombre_cliente.get(), self.telefono_cliente.get(), self.direccion_cliente.get(), self.correo_cliente.get())
			self.ejecutar_consulta(query, parameters)
			messagebox.showinfo("REGISTRO EXITOSO", f'Cliente registrado: {self.nombre_cliente.get()}')
		self.limpiar_formulario_cliente()
		self.listar_clientes()

	def validar_formulario_completo_cliente(self):
		if len(self.codigo_cliente.get()) != 0 and len(self.nombre_cliente.get()) != 0 and len(self.telefono_cliente.get()) != 0 and len(self.direccion_cliente.get()) != 0 and len(self.correo_cliente.get()) != 0:
			return True
		else:
			messagebox.showerror("ERROR", "Complete todos los campos del formulario")

	def limpiar_formulario_cliente(self):
		self.codigo_cliente.delete(0, END)
		self.nombre_cliente.delete(0, END)
		self.telefono_cliente.delete(0, END)
		self.direccion_cliente.delete(0, END)
		self.correo_cliente.delete(0, END)
		
	def listar_clientes(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		query = 'SELECT * FROM clientes ORDER BY nombre_cliente DESC'
		db_rows = self.ejecutar_consulta(query)
		for row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2], row[3], row[4], row[5]))

	def eliminar_clientes(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar un cliente de la tabla.")
		dato = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM clientes WHERE codigo_cliente = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA", f"¿Esta seguro que desea eliminar el cliente: {nombre}?")
		if respuesta == 'yes':
			self.ejecutar_consulta(query, (dato,))
			self.listar_clientes()
			messagebox.showinfo('EXITO', f'Cliente eliminado: {nombre}')
		else:
			messagebox.showerror('ERROR', f'Error al eliminar el producto: {nombre}')

	def editar_cliente(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe solucionar un cliente de la tabla.")

		codigo = self.tree.item(self.tree.selection())['text']
		nombre = self.tree.item(self.tree.selection())['values'][0]
		telefono = self.tree.item(self.tree.selection())['values'][1]
		direccion = self.tree.item(self.tree.selection())['values'][2]
		correo = self.tree.item(self.tree.selection())['values'][3]

		self.ventana_editar_cliente = Toplevel()
		self.ventana_editar_cliente.title("EDITAR CLIENTE")
		self.ventana_editar_cliente.iconbitmap("C:/Users/YURANY HENAO/Desktop/Tienda2/img/foto_tienda.ico" )
		self.ventana_editar_cliente.resizable(0,0)

		label_codigo_cliente = Label(self.ventana_editar_cliente, text="ID del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo_cliente = Entry(self.ventana_editar_cliente, textvariable=StringVar(self.ventana_editar_cliente, value=codigo), width=25)
		nuevo_codigo_cliente.grid(row=0, column=1, padx=5, pady=8)

		label_nombre_cliente = Label(self.ventana_editar_cliente, text="Nombre del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_nombre_cliente = Entry(self.ventana_editar_cliente, textvariable=StringVar(self.ventana_editar_cliente, value=nombre), width=25)
		nuevo_nombre_cliente.grid(row=0, column=3, padx=5, pady=8)

		label_telefono_cliente = Label(self.ventana_editar_cliente, text="Telefono del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		nuevo_telefono_cliente = Entry(self.ventana_editar_cliente, textvariable=StringVar(self.ventana_editar_cliente, value=telefono), width=25)
		nuevo_telefono_cliente.grid(row=1, column=1, padx=5, pady=8)

		label_direccion_cliente = Label(self.ventana_editar_cliente, text="Direccion del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nuevo_direccion_cliente = Entry(self.ventana_editar_cliente, textvariable=StringVar(self.ventana_editar_cliente, value=direccion), width=25)
		nuevo_direccion_cliente.grid(row=1, column=3, padx=5, pady=8)

		label_correo_cliente = Label(self.ventana_editar_cliente, text="Correo del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nuevo_correo_cliente = Entry(self.ventana_editar_cliente, textvariable=StringVar(self.ventana_editar_cliente, value=correo), width=25)
		nuevo_correo_cliente.grid(row=2, column=1, padx=5, pady=8)

		boton_actualizar_cliente = Button(self.ventana_editar_cliente, text="ACTUALIZAR", command=lambda:self.actualizar_cliente(nuevo_codigo_cliente.get(), nuevo_nombre_cliente.get(), nuevo_telefono_cliente.get(), nuevo_direccion_cliente.get(), nuevo_correo_cliente.get(), codigo), height=2, width=20, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar_cliente.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar_cliente.mainloop()

	def actualizar_cliente(self, nuevo_codigo_cliente, nuevo_nombre_cliente, nuevo_telefono_cliente, nuevo_direccion_cliente, nuevo_correo_cliente, codigo):
		query = 'UPDATE clientes SET codigo_cliente = ?, nombre_cliente = ?, telefono_cliente = ?, direccion_cliente = ?, correo_cliente = ? WHERE codigo_cliente = ?'
		parameters = (nuevo_codigo_cliente, nuevo_nombre_cliente, nuevo_telefono_cliente, nuevo_direccion_cliente, nuevo_correo_cliente, codigo)
		self.ejecutar_consulta(query, parameters)
		messagebox.showinfo('EXITO', f'Cliente Actualizado: {nuevo_nombre_cliente}')
		self.ventana_editar_cliente.destroy()
		self.listar_clientes()

	def widgets_buscador_cliente(self):


 		#Se carga el buscador
		self.label_titulo_buscador_cliente.config(bd=0)
		self.label_titulo_buscador_cliente.grid(row=0, column=0, padx=5, pady=5)

		'''--------------------------Titulo-------------------------'''
		self.titulo_buscador_cliente = Label(self.label_titulo_buscador_cliente, text="BUSCADOR DE CLIENTES", fg="black", font=("Comic Sans", 17, "bold"))
		self.titulo_buscador_cliente.grid(row=0, column=0)

		'''-------------------------- Frame buscar -----------------'''
		self.frame_buscar_cliente.config(bd=2)
		self.frame_buscar_cliente.grid(row=2, column=0, padx=5, pady=5)

		'''-------------------------- Formulario buscar --------------'''
		self.label_buscar_cliente = Label(self.frame_buscar_cliente, text="Buscar por: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=5)
		self.combo_buscar_cliente = ttk.Combobox(self.frame_buscar_cliente, values=["ID", "nombre"], width=22, state="readonly")
		self.combo_buscar_cliente.current(0)
		self.combo_buscar_cliente.grid(row=0, column=1, padx=5, pady=5)

		label_codigo_cliente = Label(self.frame_buscar_cliente, text="ID / Nombre del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=5)
		self.codigo_nombre_cliente = Entry(self.frame_buscar_cliente, width=25)
		self.codigo_nombre_cliente.focus()
		self.codigo_nombre_cliente.grid(row=0, column=3, padx=10, pady=5)

		'''---------------------- Frame marco --------------------------'''
		self.frame_boton_buscar_cliente.config(bd=0)
		self.frame_boton_buscar_cliente.grid(row=3, column=0, padx=5, pady=5)

		'''----------------------- Boton ------------------------------'''
		self.boton_buscar_cliente = Button(self.frame_boton_buscar_cliente, text="BUSCAR",height=2, command=self.buscar_clientes, width=20, bg="black", fg="white", font=("Comic Sans", 10, "bold"))
		self.boton_buscar_cliente.grid(row=0, column=0, padx=5, pady=5)

		#Se carga la tabla pero sin datos
		self.tree.delete(*self.tree.get_children())

		'''ESTOS REMOVE SON LOS QUE PUSE'''
		#REMOVER OTROS WIDGETS de otros formularios
		self.widgets_crud_cliente_remove()
		self.widgets_crud_ventas_remove()
		self.widgets_crud_remove()
		self.label_informacion.grid_remove()
		self.widgets_buscador_remove()
		self.widgets_buscador_venta_remove()
		

	def widgets_buscador_cliente_remove(self):
		self.label_titulo_buscador_cliente.grid_remove()
		self.frame_buscar_cliente.grid_remove()
		self.frame_boton_buscar_cliente.grid_remove()

	def buscar_clientes(self):
		if(self.validar_busqueda_cliente()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			if (self.combo_buscar_cliente.get() == 'ID'):
				#sentencia SQL LIKE-> inicie por una letra o varias o completas
				query = ("SELECT * FROM clientes WHERE codigo_cliente LIKE ? ")
				#% permite realizar la busqueda sin tener completa del codigo a buscar (busqueda parcial de la palabra y luego clic en buscar)
				parameters = (self.codigo_nombre_cliente.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parameters,))

				for row in db_rows:
					self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5]))

				if(list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR","Cliente no encontrado")
			else:
				#sentencia SQL LIKE-> inicie por
				query = ("SELECT * FROM clientes WHERE nombre_cliente LIKE ? ")
				#% permite realizar la busqueda sin tener completa del nombre a buscar (busqueda parcial de la palabra y luego clic en buscar)
				parameters = ("%"+self.codigo_nombre_cliente.get()+"%")
				db_rows = self.ejecutar_consulta(query,(parameters,))

				for row in db_rows:
					self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5]))

				if(list(self.tree.get_children()) == []):
					messagebox.showerror("ERROR","Cliente no encontrado")

	def validar_busqueda_cliente(self):
		if len(self.codigo_nombre_cliente.get()) !=0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR", "Complete todos los campos para la busqueda")

		
	def validar_codigo_cliente(self):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			query = f"SELECT * FROM clientes WHERE codigo_cliente = {self.codigo_cliente.get()}"
			cursor.execute(query)
			validacion = cursor.fetchall()
			cursor.close()
			if validacion:
				return True 
			else:
				messagebox.showerror("ERROR", "El cliente no existe")
	
		




	'''-----------------------------------ventas------------------------------------------------'''
	def widgets_crud_venta(self):
  
		#Cargar el crud
		self.label_titulo_venta.config(bd=0)
		self.label_titulo_venta.grid(row=0, column=0, padx=5, pady=5)

		#Titulo
		self.titulo_venta = Label(self.label_titulo_venta, text="REGISTRAR VENTAS", fg="black", font=("Comic Sans MS", 13, "bold"),pady=10)
		self.titulo_venta.grid(row=0, column=0)

		#Fame venta
		self.frame_logo_venta.grid(row=1, column=0, padx=5, pady=5)

		#Logo_venta
		imagen_venta = Image.open("C:/Users/YURANY HENAO/Desktop/Tienda2/img/carrito.png")
		new_image = imagen_venta.resize((60,60))
		render = ImageTk.PhotoImage(imagen_venta)
		label_imagen = Label(self.frame_logo_venta, image=render)
		label_imagen.image = render
		label_imagen.grid(row=0, column=0, padx=15, pady=5)

		#Marco de la ventana
		self.frame_registro_venta.grid(row=2, column=0, padx=50, pady=5)

		#formulario de la venta
		label_codigo_venta = Label(self.frame_registro_venta, text="Codigo de la venta", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		self.codigo_venta = Entry(self.frame_registro_venta, width=25)
		self.codigo_venta.focus()
		self.codigo_venta.grid(row=0, column=1, padx=5, pady=10)

		label_codigo_producto = Label(self.frame_registro_venta, text="Codigo del producto", font=("Comic Sans MS", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		self.codigo_producto = Entry(self.frame_registro_venta, width=25)
		self.codigo_producto.grid(row=0, column=3, padx=5, pady=10)

		label_codigo_cliente = Label(self.frame_registro_venta, text="Codigo del cliente", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		self.codigo_cliente = Entry(self.frame_registro_venta, width=25)
		self.codigo_cliente.grid(row=1, column=1, padx=5, pady=10)

		label_combo_categoria = Label(self.frame_registro_venta, text="Categoria del producto", font=("Comic Sans MS", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		self.combo_categoria = ttk.Combobox(self.frame_registro_venta, values=["Computadores", "Perifericos"], width=22, state="readonly")
		self.combo_categoria.current(0)
		self.combo_categoria.grid(row=1, column=3, padx=5, pady=8)

		label_cantidad = Label(self.frame_registro_venta, text="Cantidad del producto", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		self.cantidad = Entry(self.frame_registro_venta, width=25)
		self.cantidad.grid(row=2, column=1, padx=5, pady=10)

		label_precio = Label(self.frame_registro_venta, text="Precio del producto", font=("Comic Sans MS", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		self.precio = Entry(self.frame_registro_venta, width=25)
		self.precio.grid(row=2, column=3, padx=5, pady=10)

		#Frame botones
		self.frame_botones_venta.grid(row=3, column=0, padx=5, pady=5)

		#botones de la venta
		boton_registrar = Button(self.frame_botones_venta, text="REGISTRAR", height=2, command=self.agregar_venta, width=10, bg="green", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=0, padx=10, pady=15)
		boton_editar = Button(self.frame_botones_venta, text="EDITAR", height=2, command=self.editar_venta, width=10, bg="grey", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=1, padx=10, pady=15)
		boton_salir = Button(self.frame_botones_venta, text="SALIR", height=2, command=ventana_productos.quit, width=10, bg="lightseagreen", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=2, padx=10, pady=15)
		boton_eliminar = Button(self.frame_botones_venta, text="ELIMINAR", height=2, command=self.eliminar_venta, width=10, bg="red", fg="white", font=("Comic Sans", 9, "bold")).grid(row=0, column=3, padx=10, pady=15)

		#Tabla de la lista de las ventas
		self.frame_tabla_venta.grid(row=4, column=0, padx=5, pady=5)
		self.tree = ttk.Treeview(self.frame_tabla_venta, height=13, columns=("columna_1", "columna_2", "columna_3", "columna_4", "columna_5"))
		self.tree.heading("#0", text="Codigo", anchor=CENTER) #ENCABEZADO, CENTRAR LA INFORMACION
		self.tree.column("#0", width=90, minwidth=75, stretch=False) #stretch=False - Permite mover la columna

		#columnas y titulos de las columnas
		self.tree.heading("columna_1", text='codigo producto', anchor=CENTER)
		self.tree.column("columna_1", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna_2", text='Codigo cliente', anchor=CENTER)
		self.tree.column("columna_2", width=150, minwidth=75, stretch=False)

		self.tree.heading("columna_3", text='Categoria', anchor=CENTER)
		self.tree.column("columna_3", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna_4", text='Cantidad', anchor=CENTER)
		self.tree.column("columna_4", width=70, minwidth=75, stretch=False)

		self.tree.heading("columna_5", text='Precio', anchor=CENTER)
		self.tree.column("columna_5", width=150, minwidth=75, stretch=False)

		self.tree.grid(row=0, column=0, sticky=E)
		self.listar_ventas()


		'''Acaaaaa tambiennnnn puse removess'''
		self.widgets_crud_cliente_remove()
		self.widgets_buscador_remove()
		self.widgets_crud_remove()
		self.label_informacion.grid_remove()
		self.widgets_buscador_cliente_remove()
		self.frame_tabla_clientes.grid_remove()
		self.frame_tabla_crud.grid_remove()

	def agregar_venta(self):
		if self.validar_codigo_producto():
			if self.validar_existencia_producto():
				if self.validar_codigo_cliente():
					if self.validar_disponibilidad_producto(self.codigo_producto.get(), self.cantidad.get()):
						if self.validar_formulario_completo_venta():
							query = 'INSERT INTO ventas VALUES(NULL, ?, ?, ?, ?, ?, ?)'
							parameters = (self.codigo_venta.get(), self.codigo_producto.get(), self.codigo_cliente.get(), self.combo_categoria.get(), self.cantidad.get(), self.precio.get())
							self.ejecutar_consulta(query, parameters)
							messagebox.showinfo("REGISTRO EXITOSO", f'Venta registrada: {self.codigo_venta.get()}')
		self.limpiar_formulario_venta()
		self.listar_ventas()

	def validar_disponibilidad_producto(self, codigo, cantidad):
		query = "SELECT cantidad FROM productos WHERE codigo = ?"
		parameters = (codigo,)
		cursor = self.ejecutar_consulta(query, parameters)
		resultado = cursor.fetchone()

		if resultado:
			stock = resultado[0]
			if stock >= int(cantidad):
				stock -= int(cantidad)
				self.restar_cantidad(codigo, stock)
				messagebox.showinfo('COMPRA EXITOSA', f'Cantidad restante: {stock}')
				return True 
			else:
				messagebox.showerror("ERROR", "No hay Stock disponible para la venta.")
				return False 
		else:
			messagebox.showerror("ERROR", f"No se encontro ningun producto con el codigo: {codigo}")
			return False 
		
	def restar_cantidad(self, codigo, cantidad):
		query = 'UPDATE productos SET cantidad = ? WHERE codigo = ?'
		parameters = (cantidad, codigo)
		cursor = self.ejecutar_consulta(query, parameters)
		resultado = cursor.fetchone()

	def validar_existencia_producto(self):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			query = f"SELECT * FROM productos WHERE cantidad >= {self.cantidad.get()}"
			cursor.execute(query)
			validacion = cursor.fetchall()
			cursor.close()
			if validacion:
				return True 
			else:
				messagebox.showerror("ERROR", "El producto no tiene existencia")

	def validar_codigo_producto(self):
		with sqlite3.connect(self.db_name) as conexion:
			cursor = conexion.cursor()
			query = f"SELECT * FROM productos WHERE codigo = {self.codigo_producto.get()}"
			cursor.execute(query)
			validacion = cursor.fetchall()
			cursor.close()
			if validacion:
				return True
			else:
				messagebox.showerror("ERROR", "El producto no existe")

	def validar_formulario_completo_venta(self):
		if len(self.codigo_venta.get()) != 0 and len(self.codigo_producto.get()) != 0 and len(self.codigo_cliente.get()) != 0 and len(self.combo_categoria.get()) != 0 and len(self.cantidad.get()) != 0 and len(self.precio.get()) != 0:
			return True
		else:
			messagebox.showerror("ERROR", "Complete todos los campos del formulario")

	def limpiar_formulario_venta(self):
		self.codigo_venta.delete(0, END)
		self.codigo_producto.delete(0, END)
		self.codigo_cliente.delete(0, END)
		self.cantidad.delete(0, END)
		self.precio.delete(0, END)

	def listar_ventas(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)

		query = 'SELECT * FROM ventas ORDER BY codigo_venta DESC'
		db_rows = self.ejecutar_consulta(query)
		for row in db_rows:
			self.tree.insert("",0, text=row[1], values=(row[2], row[3], row[4], row[5], row[6]))

	def eliminar_venta(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar una venta de la tabla")
		dato = self.tree.item(self.tree.selection())['text']
		codigo_venta = self.tree.item(self.tree.selection())['values'][0]
		query = "DELETE FROM ventas WHERE codigo_venta = ?"
		respuesta = messagebox.askquestion("ADVERTENCIA",f'¿Esta seguro que desea eliminar la venta: {codigo_venta}?')
		if respuesta == 'yes':
			self.ejecutar_consulta(query,(dato,))
			self.listar_ventas()
			messagebox.showinfo('EXITO',f'Venta eliminada: {codigo_venta}')
		else:
			messagebox.showerror('ERROR',f'Error al eliminar la venta: {codigo_venta}')

		
	def editar_venta(self):
		try:
			self.tree.item(self.tree.selection())['values'][0]
		except IndexError as e:
			messagebox.showerror("ERROR", "Debe seleccionar una venta de la tabla")

		codigo_venta = self.tree.item(self.tree.selection())['text']
		codigo_producto = self.tree.item(self.tree.selection())['values'][0]
		codigo_cliente = self.tree.item(self.tree.selection())['values'][1]
		combo_categoria = self.tree.item(self.tree.selection())['values'][2]
		cantidad = self.tree.item(self.tree.selection())['values'][3]
		precio = self.tree.item(self.tree.selection())['values'][4]

		self.ventana_editar = Toplevel()
		self.ventana_editar.title("EDITAR VENTA")
		#incluir un icono a la ventana
		self.ventana_editar.iconbitmap("C:/Users/YURANY HENAO/Desktop/Tienda2/img/ventas.ico")
		#modificar o no las dimensiones de la ventana
		self.ventana_editar.resizable(1,1)

		label_codigo_venta = Label(self.ventana_editar, text="Codigo de la venta: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo_venta = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo_venta), width=25)
		nuevo_codigo_venta.grid(row=0, column=1, padx=5, pady=8)

		label_codigo_producto = Label(self.ventana_editar, text="Codigo del producto: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=2, sticky='s', padx=5, pady=8)
		nuevo_codigo_producto = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo_producto), width=25)
		nuevo_codigo_producto.grid(row=0, column=3, padx=5, pady=0)

		label_codigo_cliente = Label(self.ventana_editar, text="Codigo del cliente: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=5, pady=8)
		nuevo_codigo_cliente = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=codigo_cliente), width=25)
		nuevo_codigo_cliente.grid(row=1, column=1, padx=5, pady=0)

		label_combo_categoria = Label(self.ventana_editar, text="Categoria: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=2, sticky='s', padx=5, pady=8)
		nuevo_combo_categoria = ttk.Combobox(self.ventana_editar, values=["Computadores", "Perifericos"], width=22, state="readonly")
		nuevo_combo_categoria.set(combo_categoria)
		nuevo_combo_categoria.grid(row=1, column=3, padx=5, pady=0)

		label_cantidad = Label(self.ventana_editar, text="Cantidad: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=0, sticky='s', padx=5, pady=8)
		nueva_cantidad = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=cantidad), width=25)
		nueva_cantidad.grid(row=2, column=1, padx=5, pady=0)

		label_precio = Label(self.ventana_editar, text="Precio: ", font=("Comic Sans", 10, "bold")).grid(row=2, column=2, sticky='s', padx=5, pady=8)
		nuevo_precio = Entry(self.ventana_editar, textvariable=StringVar(self.ventana_editar, value=precio), width=25)
		nuevo_precio.grid(row=2, column=3, padx=5, pady=0)

		boton_actualizar = Button(self.ventana_editar, text="ACTUALIZAR", command=lambda:self.actualizar(nuevo_codigo_venta.get(), nuevo_codigo_producto.get(), nuevo_codigo_cliente.get(), nuevo_combo_categoria.get(), nueva_cantidad.get(), nuevo_precio.get(), codigo_venta), height=2, width=20, bg="blue", fg="white", font=("Comic Sans MS", 9, "bold"))
		boton_actualizar.grid(row=3, column=1, columnspan=2, padx=10, pady=15)

		self.ventana_editar.mainloop() 

	def actualizar(self, nuevo_codigo_venta, nuevo_codigo_producto, nuevo_codigo_cliente, nuevo_combo_categoria, nueva_cantidad, nuevo_precio, codigo_venta):
		query = 'UPDATE ventas SET codigo_venta = ?, codigo_producto = ?, codigo_cliente = ?, combo_categoria = ?, cantidad = ?, precio = ? WHERE codigo_venta = ?'
		parameters = (nuevo_codigo_venta, nuevo_codigo_producto, nuevo_codigo_cliente, nuevo_combo_categoria, nueva_cantidad, nuevo_precio, codigo_venta)
		self.ejecutar_consulta(query, parameters)
		messagebox.showinfo('EXITO',f'Venta Actualizada: {nuevo_codigo_venta}')
		self.ventana_editar.destroy()
		self.listar_ventas()

	def buscar_ventas(self):
		if(self.validar_busqueda_venta()):
			records = self.tree.get_children()
			for element in records:
				self.tree.delete(element)

			#sentencia SQL LIKE-> inicie por una letra o varias o completas
			query = ("SELECT * FROM ventas WHERE codigo_venta LIKE ? ") 
			#% permite realizar la busqueda sin tener completa del codigo a buscar (busqueda parcial de la palabra y luego clic en buscar)
			parameters = (self.codigo_venta.get()+"%")
			db_rows = self.ejecutar_consulta(query,(parameters,))
				
			for row in db_rows:
				self.tree.insert("",0, text=row[1],values=(row[2],row[3],row[4],row[5],row[6]))
				
			if(list(self.tree.get_children()) == []):
				messagebox.showerror("ERROR","La venta no  fue encontrada")

	def validar_busqueda_venta(self):
		if len(self.codigo_venta.get()) !=0:
			return True
		else:
			self.tree.delete(*self.tree.get_children())
			messagebox.showerror("ERROR", "Complete todos los campos para la busqueda")


	def widgets_buscador_venta(self):
		#Se carga el buscardor
		self.label_titulo_buscador_ventas.config(bd=0)
		self.label_titulo_buscador_ventas.grid(row=0, column=0, padx=5, pady=5)

		'''---------------------Titulo----------------------'''
		self.titulo_buscador_ventas = Label(self.label_titulo_buscador_ventas, text="BUSCADOR DE VENTAS", fg="black", font=("Comic Sans", 17, "bold"))
		self.titulo_buscador_ventas.grid(row=0, column=0)

		'''--------------------Frame buscar--------------------'''
		self.frame_buscar_venta.config(bd=2)
		self.frame_buscar_venta.grid(row=2, column=0, padx=5, pady=5)

		'''-------------------Formulario buscar---------------------'''
		label_codigo = Label(self.frame_buscar_venta, text="Buscar codigo de la venta: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=5)
		self.codigo_venta = Entry(self.frame_buscar_venta, width=25)
		self.codigo_venta.focus()
		self.codigo_venta.grid(row=0, column=1, padx=10, pady=5)

		'''-----------------Frame marco-----------------------------'''
		self.frame_boton_buscar_venta.config(bd=0)
		self.frame_boton_buscar_venta.grid(row=3, column=0, padx=5, pady=5)

		'''-----------------------Boton-------------------------'''
		self.boton_buscar = Button(self.frame_boton_buscar_venta, text="BUSCAR", height=2, command=self.buscar_ventas, width=20, bg="black", fg="white", font=("Comic Sans", 10, "bold"))
		self.boton_buscar.grid(row=0, column=0, padx=5, pady=5)

		#se carga la tabla pero sin datos
		self.tree.delete(*self.tree.get_children())

		#REMOVER OTROS WIDGETS de otros formularios
		self.widgets_crud_remove()
		self.label_informacion.grid_remove()
		self.widgets_crud_cliente_remove()
		self.widgets_buscador_remove()
		self.widgets_buscador_cliente_remove()
		



	def widgets_crud_cliente_remove(self):
		self.label_titulo_cliente.grid_remove()
		self.frame_registro_cliente.grid_remove()
		self.frame_botones_cliente.grid_remove()
		self.frame_logo_cliente.grid_remove()
		#self.frame_tabla_clientes.grid_remove()
  
	def widgets_crud_ventas_remove(self):
		self.label_titulo_venta.grid_remove()
		self.frame_registro_venta.grid_remove()
		self.frame_botones_venta.grid_remove()
		self.frame_logo_venta.grid_remove()
		#self.frame_tabla_venta.grid_remove()

	def widgets_buscador_venta_remove(self):
		self.label_titulo_buscador_ventas.grid_remove()
		self.frame_buscar_venta.grid_remove()
		self.frame_boton_buscar_venta.grid_remove()
  
if __name__ == '__main__':
	ventana_productos = Tk()
	application = Productos(ventana_productos)
	ventana_productos.mainloop()