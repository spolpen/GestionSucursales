__author__ = 'Luzu'

from Interfaz import *


#SUCURSALES
sucursal1 = Sucursal("Sevilla", "Pino Montano", "TCE Sevilla")

sucursal2 = Sucursal("Malaga", "Malaga", "TCE Malaga")

lista_sucursales.append(sucursal1)
lista_sucursales.append(sucursal2)

#PRODUCTOS
producto1 = Producto("Televisor", "TV LED 32'' Panasonic", 329)
producto2 = Producto("Impresora", "Impresora Multifuncion Epson ", 59)
producto3 = Producto("HDD", "Disco Duro portatil Toshiba 1 TB", 69)
producto4 = Producto("Tablet", "Tablet Samsung Galaxy Tab 4", 239)
producto5 = Producto("USB", "Pen Drive Toshiba 8", 4)
producto6 = Producto("Raton", "Raton Microsoft 1850", 15)

#EMPLEADOS


empleado1 = Empleado("Miguel", "30568123B", "Miguel Bermejo", 954951202, "Sevilla", 1200, "8:00-15:00")
empleado2 = Empleado("Sergio", "49501120V", "Sergio Polo", 954951289, "Sevilla", 1200, "8:00-15:00")
empleado3 = Empleado("Alejandro", "34968372X", "Alejandro Luzuriaga", 954128931, "Dos Hermanas",
                     1200, "16:00-21:00")
empleado4 = Empleado("Juan", "29808123F", "Juan Perez", 954955789, "Sevilla", 2400, "10:00-20:00")


#PROVEEDORES
proveedor1 = Proveedor("Manuel", "48102981A", "Manuel Garcia", 912018391, "Madrid")


#INCIDENCIAS
incidencia1 = Incidencia("Incidencia1", "Baja empleado", "Juan Perez baja por enfermedad")
incidencia2 = Incidencia("Incidencia2", "Pago atrasado", "Hay que efectuar un pago atrasado al proveedor")


sucursal1.aniadir_producto(producto1)
sucursal1.aniadir_producto(producto2)
sucursal1.aniadir_producto(producto3)

sucursal2.aniadir_producto(producto1)
sucursal2.aniadir_producto(producto4)
sucursal2.aniadir_producto(producto5)
sucursal2.aniadir_producto(producto6)


sucursal1.aniadir_empleado(empleado1)
sucursal1.aniadir_empleado(empleado2)

sucursal2.aniadir_empleado(empleado3)
sucursal2.aniadir_empleado(empleado4)


sucursal1.aniadir_proveedor(proveedor1)

sucursal2.aniadir_proveedor(proveedor1)


sucursal1.aniadir_incidencia(incidencia1)
sucursal2.aniadir_incidencia(incidencia2)


win = make_window()
set_select_sucursal()
win.mainloop()

