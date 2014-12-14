__author__ = 'Luzu'

from Interfaz import *

#PRODUCTOS
producto1 = Producto("Producto1","Televisor",200)
#EMPLEADO
empleado1 = Empleado("Empleado1","29808123F","Juan Perez",954951289,"Sevilla",1200,"8:00-15:00")
#PROVEEDOR
proveedor1 = Proveedor("Proveedor1","48102981A","Manuel Garcia",912018391,"Madrid")

#SUCURSALES
sucursal1 = Sucursal("Sevilla","Pino Montano","Sucursal1")
sucursal1.aniadirProducto(producto1)
sucursal1.aniadirEmpleado(empleado1)
sucursal1.aniadirProveedor(proveedor1)
sucursal2 = Sucursal("Malaga","Malaga","Sucursal2")

listaSucursales.append(sucursal1)
listaSucursales.append(sucursal2)


win = makeWindow()
setSelectSucursal ()
win.mainloop()

