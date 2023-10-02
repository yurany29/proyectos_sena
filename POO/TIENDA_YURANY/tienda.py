from vendedor import Vendedor
from producto import Producto
from venta import Venta
from datetime import datetime

class Tienda:

    def __init__(self):
        self.vendedores = []
        self.productos = []
        self.ventas = []
        self.total = []

    def buscar_vendedor(self, id_vendedor):
        for i in range(len(self.vendedores)):
            if self.vendedores[i].id_vendedor == id_vendedor:
                return i
        return -1
    
    def crear_vendedor(self, vendedor):
        if self.buscar_vendedor(vendedor.id_vendedor) == -1:
            self.vendedores.append(vendedor)
            return True
        return False

    def lista_vendedores(self):
        for i in self.vendedores:
            print("|---------------------------------|")
            i.mostrar_vendedores()

    def modificar_vendedor(self, id_vendedor):
        pos = self.buscar_vendedor(id_vendedor)
        if pos != -1:
            if self.vendedores[pos].id_vendedor == id_vendedor:
                print("|---------------------------------|")
                print("|      OPCIONES PARA MODIFICAR    |")
                print("|---------------------------------|")

                try:
                    print("|---------------------------------|")
                    print("|1.Modificar nombre               |")
                    print("|2.Modificar telefono             |")
                    print("|3.Modificar domicilio            |")
                    print("|4.Modificar edad                 |")
                    print("|---------------------------------|")

                    op = int(input("Digite la opcion: "))

                    if op == 1:
                        nombre = input("Ingrese el nuevo nombre: ")
                        self.vendedores[pos].nombre = nombre
                        return True
                    
                    elif op == 2:
                        telefono = input("Ingrese el nuevo telefono: ")
                        self.vendedores[pos].telefono = telefono
                        return True
                    
                    elif op == 3:
                        domicilio = input("Digite el nuevo domicilio: ")
                        self.vendedores[pos].domicilio = domicilio
                        return True
                    
                    elif op == 4:
                        edad = input("Ingrese la nueva edad: ")
                        self.vendedores[pos].edad = edad
                        return True
                    
                    else:
                        return False
                    
                except ValueError:
                    print("|---------------------------------|")
                    print("|  ERROR-EL DATO DEBE SER ENTERO  |")
                    print("|---------------------------------|")
                    input()
            else:
                return False
        else:
            return False

    def eliminar_vendedor(self, id_vendedor):
        pos = self.buscar_vendedor(id_vendedor)
        if pos != -1:
            del (self.vendedores[pos])
            return True
        
        else:
            return False

    def buscar_producto(self, id_producto):
        for i in range(len(self.productos)):
            if self.productos[i].id_producto == id_producto:
                return i
        return -1

    def agregar_producto(self, producto):
        if self.buscar_producto(producto.id_producto) == -1:
            self.productos.append(producto)
            return True
        return False

    def listar_productos(self):
        for i in self.productos:
            print("|---------------------------------|")
            i.mostrar_productos()

    def modificar_productos(self, id_producto):
        pos = self.buscar_producto(id_producto)
        if pos != -1:
            if self.productos[pos].id_producto == id_producto:
                print("|---------------------------------|")
                print("|    OPCIONES PARA MODIFICAR      |")
                print("|---------------------------------|")

                try:
                    print("|---------------------------------|")
                    print("|1.Modificar Nombre               |")
                    print("|2.Modificar cantidad             |")
                    print("|3.Modificar valor unitario       |")
                    print("|---------------------------------|")

                    op = int(input("Digite su opcion: "))

                    if op == 1:
                        nombre = input("Ingrese el nuevo nombre: ")
                        self.productos[pos].nombre = nombre
                        return True

                    elif op == 2:
                        cantidad = input("Ingrese la nueva cantidad: ")
                        self.productos[pos].cantidad = cantidad
                        return True

                    elif op == 3:
                        valor_unitario = input("Ingrese el nuevo valor unitario: ")
                        self.productos[pos].valor_unitario = valor_unitario
                        return True

                    else:
                        return False

                except ValueError:
                    print("|---------------------------------|")
                    print("|  ERROR-EL DATO DEBE SER ENTERO  |")
                    print("|---------------------------------|")

            else:
                return False
        else:
            return False

    def eliminar_productos(self, id_producto):
        pos = self.buscar_producto(id_producto)
        if pos != -1:
            del(self.productos[pos])
            return True
        else:
            return False

    def buscar_venta(self, id_venta):
        for i in range(len(self.ventas)):
            if self.ventas[i].id_venta == id_venta:
                return i
        return -1

    def registrar_venta(self, venta):
        if self.buscar_venta(venta.id_venta) == -1:
            self.ventas.append(venta)
            return True
        return False

    def fecha(self, dia, mes, anio):
        #Este sector valida los datos ingresados
        if mes > 0 and mes <= 12:      
            #Este sector valida si es año bisiesto
            if (anio % 400 == 0) or (anio % 100 != 0 and anio % 4 == 0):      
                dias = [31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                dias = [31,28,31,30,31,30,31,31,30,31,30,31]
            if(dia <= dias[mes-1] and dia > 0):
                self.dia = dia
                self.mes = mes
                self.anio = anio
                return True
            else:
                return False

        else:
            return False

    def descontar_cantidad(self, id_producto, cantidad):
        pos = self.buscar_producto(id_producto)
        if pos != -1:
            if self.productos[pos].descontar_cantidad(cantidad):
                return True
            else:
                return False

    def modificar_venta(self, id_venta):
        pos = self.buscar_venta(id_venta)
        if pos != -1:
            if self.ventas[pos].id_venta == id_venta:
                print("|---------------------------------|")
                print("|      OPCIONES PARA MODIFICAR    |")
                print("|---------------------------------|")

                try:
                    print("|-------------------------------|")
                    print("|1.Modificar fecha              |")
                    print("|2.Modificar cantidad           |")
                    print("|3.Modificar id vendedor        |")
                    print("|4.Modificar id producto        |")
                    print("|-------------------------------|")

                    op = int(input("Digite la opcion: "))

                    if op == 1:
                        dia = int(input("Ingrese el dia: "))
                        mes = int(input("Ingrese el mes: "))
                        anio = int(input("Ingrese el año: "))
                        if self.fecha(dia, mes, anio):
                            self.ventas[pos].dia = dia
                            self.ventas[pos].mes = mes
                            self.ventas[pos].anio = anio 
                            return True

                        else:
                            print("|-------------------------------|")
                            print("|  ERROR-LA FECHA NO ES VALIDA  |")
                            print("|-------------------------------|")
                            input()

                    elif op == 2:
                        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                        self.ventas[pos].cantidad = cantidad
                        return True

                    elif op == 3:
                        id_vendedor = input("Ingrese el id del nuevo vendedor: ")
                        self.ventas[pos].id_vendedor = id_vendedor
                        return True

                    elif op == 4:
                        id_producto = input("Ingrese el id del nuevo producto: ")
                        self.ventas[pos].id_producto = id_producto
                        return True

                    else:
                        return False


                except ValueError:
                    print("|---------------------------------|")
                    print("|  ERROR-EL DATO DEBE SER ENTERO  |")
                    print("|---------------------------------|")
                    input()

            else:
                return False
        else:
            return False

    def ventas_producto(self, id_producto):
        for i in self.ventas:
            if i.id_producto == id_producto:
                i.mostrar_ventas_producto()

    def buscar_valor(self, id_producto):
        pos = self.buscar_producto(id_producto)
        valor = self.productos[pos].get_valor_unitario()
        return valor


    def ventas_fecha(self, dia, mes, anio):
        for i in self.ventas:
            if i.dia == dia:
                if i.mes == mes:
                    if i.anio == anio:
                        i.mostrar_ventas_fecha()

    def ventas_vendedor(self, id_vendedor):
        for i in self.ventas:
            if i.id_vendedor == id_vendedor:
                i.mostrar_ventas_vendedor()




    