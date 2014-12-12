__author__ = 'Polo'

from Tkinter import *
from Producto import *
from Sucursal import *
from Empleado import *
from Proveedor import *

#PRODUCTOS
producto = Producto("Producto1","Televisor",200)
#EMPLEADO
empleado = Empleado(1,"29808123F","Juan Perez",954951289,"Sevilla",100,100)
#PROVEEDOR
proveedor = Proveedor(1,"48102981A","Manuel Garcia",912018391,"Madrid")

#SUCURSALES
sucursal = Sucursal("Sevilla","Pino Montano","Sucursal1")
sucursal.aniadirProducto(producto)
sucursal.aniadirEmpleado(empleado)
sucursal.aniadirProveedor(proveedor)
sucursal2 = Sucursal("Malaga","Malaga","Sucursal2")
listaSucursales =[]
listaSucursales.append(sucursal)
listaSucursales.append(sucursal2)


#Metodos productos
def whichProductoSelected () :
    return int(selectProducto.curselection()[0])

def addProducto () :
    sucursal = sucursalSeleccionada
    producto = Producto(idProd.get(),nameProd.get(),priceProd.get())
    sucursal.aniadirProducto(producto)

    setSelectProducto ()

def updateProducto() :
    producto = productoSeleccionado
    producto.set_ID(idProd.get())
    producto.set_nombre(nameProd.get())
    producto.set_precio(priceProd.get())

    setSelectProducto ()

def deleteProducto() :
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaProductos()
    producto = lista[whichProductoSelected()]
    sucursal.eliminarProducto(producto)

    setSelectProducto ()

def loadProducto() :
    global productoSeleccionado
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaProductos()
    producto = lista[whichProductoSelected()]
    productoSeleccionado = producto
    idProd.set(producto.get_ID())
    nameProd.set(producto.get_nombre())
    priceProd.set(producto.get_precio())


#Metodos sucursales
def whichSucursalSelected () :
    return int(selectSucursal.curselection()[0])

def addSucursal() :
    sucursal = Sucursal(nameSuc.get(),dirSuc.get(),idSuc.get())
    listaSucursales.append(sucursal)

    setSelectSucursal ()


def updateSucursal() :
    sucursal = sucursalSeleccionada
    sucursal.set_nombre(nameSuc.get())
    sucursal.set_direccion(dirSuc.get())
    sucursal.set_ID(idSuc.get())
    setSelectSucursal ()



def deleteSucursal() :
    del listaSucursales[whichSucursalSelected()]
    setSelectSucursal ()


def loadSucursal() :
    global sucursalSeleccionada
    sucursal = listaSucursales[whichSucursalSelected()]
    sucursalSeleccionada = sucursal
    nameSuc.set(sucursal.get_nombre())
    dirSuc.set(sucursal.get_direccion())
    idSuc.set(sucursal.get_ID())

    setSelectProducto ()
    setSelectEmpleado()
    setSelectProveedor()

#Metodos empleados
def whichEmpleadoSelected() :
    return int(selectEmpleado.curselection()[0])

def addEmpleado() :
    sucursal = sucursalSeleccionada
    empleado = Empleado(idEmp.get(),dniEmp.get(),nameEmp.get(),telEmp.get(),dirEmp.get())
    sucursal.aniadirEmpleado(empleado)
    setSelectEmpleado ()

def updateEmpleado() :
    empleado = empleadoSeleccionado
    empleado.set_nombre(nameEmp.get())
    empleado.set_ID(idEmp.get())
    empleado.set_direccion(dirEmp.get())
    empleado.set_DNI(dniEmp.get())
    empleado.set_telefono(telEmp.get())
    setSelectEmpleado ()

def deleteEmpleado() :
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaEmpleados()
    empleado = lista[whichEmpleadoSelected()]
    sucursal.eliminarEmpleado((empleado))
    setSelectEmpleado ()

def loadEmpleado() :
    global empleadoSeleccionado
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaEmpleados()
    empleado = lista[whichEmpleadoSelected()]
    empleadoSeleccionado = empleado
    idEmp.set(empleado.get_ID())
    dniEmp.set(empleado.get_DNI())
    nameEmp.set(empleado.get_nombre())
    telEmp.set(empleado.get_telefono())
    dirEmp.set(empleado.get_direccion())

#Metodos proveedores
def whichProveedorSelected() :
    return int(selectProveedor.curselection()[0])

def addProveedor() :
    sucursal = sucursalSeleccionada
    proveedor = Proveedor(idPro.get(),dniPro.get(),namePro.get(),telPro.get(),dirPro.get())
    sucursal.aniadirProveedor(proveedor)
    setSelectProveedor ()

def updateProveedor() :
    proveedor = proveedorSeleccionado
    proveedor.set_nombre(namePro.get())
    proveedor.set_ID(idPro.get())
    proveedor.set_direccion(dirPro.get())
    proveedor.set_DNI(dniPro.get())
    proveedor.set_telefono(telPro.get())
    setSelectProveedor()

def deleteProveedor() :
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaProveedores()
    proveedor = lista[whichProveedorSelected()]
    sucursal.eliminarProveedor(proveedor)
    setSelectProveedor ()

def loadProveedor() :
    global proveedorSeleccionado
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaProveedores()
    proveedor = lista[whichProveedorSelected()]
    proveedorSeleccionado = proveedor
    idPro.set(proveedor.get_ID())
    dniPro.set(proveedor.get_DNI())
    namePro.set(proveedor.get_nombre())
    telPro.set(proveedor.get_telefono())
    dirPro.set(proveedor.get_direccion())

def makeWindow () :
    global nameProd, priceProd, idProd, nameSuc, dirSuc, idSuc, idEmp, dniEmp, nameEmp, telEmp, dirEmp, idPro, dniPro, namePro, telEmp, dirEmp, selectProducto, selectSucursal, selectEmpleado, selectProveedor
    win = Tk()

    frameSucursal = Frame(win)

    frame1 = Frame(frameSucursal)
    frameSucursal.pack()
    frame1.pack()
    Label(frame1, text="Lista de sucursales").grid(row=0, column=0, sticky=W)
    Label(frame1, text="Nombre").grid(row=1, column=0, sticky=W)
    nameSuc = StringVar()
    name2 = Entry(frame1, textvariable=nameSuc)
    name2.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Direccion").grid(row=2, column=0, sticky=W)
    dirSuc = StringVar()
    dir2= Entry(frame1, textvariable=dirSuc)
    dir2.grid(row=2, column=1, sticky=W)

    Label(frame1, text="ID").grid(row=3, column=0, sticky=W)
    idSuc= StringVar()
    id2= Entry(frame1, textvariable=idSuc)
    id2.grid(row=3, column=1, sticky=W)

    frame2 = Frame(frameSucursal)       # Row of buttons
    frame2.pack()
    b5 = Button(frame2,text=" Agregar",command=addSucursal)
    b6 = Button(frame2,text="Modificar2",command=updateSucursal)
    b7 = Button(frame2,text="Eliminar2",command=deleteSucursal)
    b8 = Button(frame2,text=" Consultar2 ",command=loadSucursal)
    b5.pack(side=LEFT); b6.pack(side=LEFT)
    b7.pack(side=LEFT); b8.pack(side=LEFT)

    frame3 = Frame(frameSucursal)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    selectSucursal = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectSucursal.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectSucursal.pack(side=LEFT,  fill=BOTH, expand=1)

    #PRODUCTOS

    frameProducto = Frame(win)
    frameProducto.pack(side = LEFT)
    frame4 = Frame(frameProducto)
    frame4.pack()
    Label(frame4, text="Lista de productos").grid(row=4, column=0, sticky=W)
    Label(frame4, text="Nombre").grid(row=5, column=0, sticky=W)
    nameProd = StringVar()
    name = Entry(frame4, textvariable=nameProd)
    name.grid(row=5, column=1, sticky=W)

    Label(frame4, text="Precio").grid(row=6, column=0, sticky=W)
    priceProd= StringVar()
    price= Entry(frame4, textvariable=priceProd)
    price.grid(row=6, column=1, sticky=W)

    Label(frame4, text="ID").grid(row=7, column=0, sticky=W)
    idProd= StringVar()
    id= Entry(frame4, textvariable=idProd)
    id.grid(row=7, column=1, sticky=W)


    frame5 = Frame(frameProducto)       # Row of buttons
    frame5.pack()
    b1 = Button(frame5,text=" Agregar",command=addProducto)
    b2 = Button(frame5,text="Modificar",command=updateProducto)
    b3 = Button(frame5,text="Eliminar",command=deleteProducto)
    b4 = Button(frame5,text=" Consultar ",command=loadProducto)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    frame6 = Frame(frameProducto)       # select of names
    frame6.pack()
    scroll = Scrollbar(frame6, orient=VERTICAL)
    selectProducto = Listbox(frame6, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectProducto.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectProducto.pack(side=LEFT,  fill=BOTH, expand=1)

    #Empleados
    frameEmpleado = Frame(win)
    frameEmpleado.pack(side = LEFT)
    frame7 = Frame(frameEmpleado)
    frame7.pack()
    Label(frame7, text="Lista de empleados").grid(row=0, column=4, sticky=W)
    Label(frame7, text="Nombre empleado").grid(row=1, column=4, sticky=W)
    nameEmp = StringVar()
    name3 = Entry(frame7, textvariable=nameEmp)
    name3.grid(row=1, column=5, sticky=W)

    Label(frame7, text="Direccion").grid(row=2, column=4, sticky=W)
    dirEmp = StringVar()
    dir3= Entry(frame7, textvariable=dirEmp)
    dir3.grid(row=2, column=5, sticky=W)

    Label(frame7, text="ID empleado").grid(row=3, column=4, sticky=W)
    idEmp= StringVar()
    id3= Entry(frame7, textvariable=idEmp)
    id3.grid(row=3, column=5, sticky=W)

    Label(frame7, text="DNI").grid(row=4, column=4, sticky=W)
    dniEmp= StringVar()
    dni= Entry(frame7, textvariable=dniEmp)
    dni.grid(row=4, column=5, sticky=W)

    Label(frame7, text="Telefono").grid(row=5, column=4, sticky=W)
    telEmp= StringVar()
    tel= Entry(frame7, textvariable=telEmp)
    tel.grid(row=5, column=5, sticky=W)

    frame8 = Frame(frameEmpleado)       # Row of buttons
    frame8.pack()
    b9 = Button(frame8,text=" Agregar3",command=addEmpleado)
    b10 = Button(frame8,text="Modificar3",command=updateEmpleado)
    b11 = Button(frame8,text="Eliminar3",command=deleteEmpleado)
    b12 = Button(frame8,text=" Consultar3 ",command=loadEmpleado)
    b9.pack(side=LEFT); b10.pack(side=LEFT)
    b11.pack(side=LEFT); b12.pack(side=LEFT)

    frame9 = Frame(frameEmpleado)       # select of names
    frame9.pack()
    scroll = Scrollbar(frame9, orient=VERTICAL)
    selectEmpleado = Listbox(frame9, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectEmpleado.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectEmpleado.pack(side=LEFT,  fill=BOTH, expand=1)

    #Proveedores
    frameProveedor = Frame(win)
    frameProveedor.pack(side = BOTTOM)
    frame10 = Frame(frameProveedor)
    frame10.pack()
    Label(frame10, text="Lista de proveedores").grid(row=5, column=4, sticky=W)
    Label(frame10, text="Nombre proveedores").grid(row=6, column=4, sticky=W)
    namePro = StringVar()
    name4 = Entry(frame10, textvariable=namePro)
    name4.grid(row=6, column=5, sticky=W)

    Label(frame10, text="Direccion").grid(row=7, column=4, sticky=W)
    dirPro = StringVar()
    dir4= Entry(frame10, textvariable=dirPro)
    dir4.grid(row=7, column=5, sticky=W)

    Label(frame10, text="ID proveedor").grid(row=8, column=4, sticky=W)
    idPro= StringVar()
    id4= Entry(frame10, textvariable=idPro)
    id4.grid(row=8, column=5, sticky=W)

    Label(frame10, text="DNI").grid(row=9, column=4, sticky=W)
    dniPro= StringVar()
    dni2= Entry(frame10, textvariable=dniPro)
    dni2.grid(row=9, column=5, sticky=W)

    Label(frame10, text="Telefono").grid(row=10, column=4, sticky=W)
    telPro= StringVar()
    tel2= Entry(frame10, textvariable=telPro)
    tel2.grid(row=10, column=5, sticky=W)

    frame11 = Frame(frameProveedor)       # Row of buttons
    frame11.pack()
    b13 = Button(frame11,text=" Agregar4",command=addProveedor)
    b14 = Button(frame11,text="Modificar4",command=updateProveedor)
    b15 = Button(frame11,text="Eliminar4",command=deleteProveedor)
    b16 = Button(frame11,text=" Consultar4 ",command=loadProveedor)
    b13.pack(side=LEFT); b14.pack(side=LEFT)
    b15.pack(side=LEFT); b16.pack(side=LEFT)

    frame12 = Frame(frameProveedor)       # select of names
    frame12.pack()
    scroll = Scrollbar(frame12, orient=VERTICAL)
    selectProveedor = Listbox(frame12, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectProveedor.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectProveedor.pack(side=LEFT,  fill=BOTH, expand=1)


    return win

def setSelectSucursal () :

    listaSucursales.sort()
    selectSucursal.delete(0,END)
    for sucursal in listaSucursales :
        selectSucursal.insert(END, sucursal.get_ID())

def setSelectProducto () :

    sucursal = sucursalSeleccionada
    selectProducto.delete(0,END)
    lista = sucursal.get_listaProductos()
    for producto in lista :
        selectProducto.insert (END, producto.get_ID())

def setSelectEmpleado() :
    sucursal = sucursalSeleccionada
    selectEmpleado.delete(0,END)
    lista = sucursal.get_listaEmpleados()
    for empleado in lista :
        selectEmpleado.insert(END, empleado.get_ID())

def setSelectProveedor() :
    sucursal = sucursalSeleccionada
    selectProveedor.delete(0,END)
    lista = sucursal.get_listaProveedores()
    for proveedor in lista :
        selectProveedor.insert(END, proveedor.get_ID())


win = makeWindow()
setSelectSucursal ()
win.mainloop()
