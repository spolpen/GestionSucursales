__author__ = 'Polo'

from Tkinter import *
from Producto import *
from Sucursal import *
from Empleado import *
from Proveedor import *
from Incidencia import *
import ttk

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
listaSucursales =[]
listaSucursales.append(sucursal1)
listaSucursales.append(sucursal2)

def limpiarVariables () :
    """Limpieza de variables

    Metodo que elimina los datos de los campos de producto, empleado, proveedor e incidencia.

    :return:
    """
    nameProd.set("")
    priceProd.set("")
    idProd.set("")
    idEmp.set("")
    dniEmp.set("")
    nameEmp.set("")
    telEmp.set("")
    dirEmp.set("")
    salEmp.set("")
    horEmp.set("")
    idPro.set("")
    dniPro.set("")
    namePro.set("")
    telPro.set("")
    dirPro.set("")
    telEmp.set("")
    dirEmp.set("")
    idInc.set("")
    asuInc.set("")
    desInc.set("")
    estInc.set("")


#Metodos productos
def whichProductoSelected () :
    """Producto seleccionado

    Metodo que nos devuelve el producto que tenemos seleccionado en la lista de productos.

    :return: producto seleccionado
    """
    return int(selectProducto.curselection()[0])

def addProducto () :
    """Agregar producto

    Metodo que crea un nuevo producto con los datos que hay en los campos y lo agrega a la lista de productos de la sucursal

    :return:
    """
    sucursal = sucursalSeleccionada
    producto = Producto(idProd.get(),nameProd.get(),priceProd.get())
    sucursal.aniadirProducto(producto)

    setSelectProducto ()

def updateProducto() :
    """Modificar producto

    Metodo que actualiza el producto con los datos que hay en los campos.

    :return:
    """
    producto = productoSeleccionado
    producto.set_ID(idProd.get())
    producto.set_nombre(nameProd.get())
    producto.set_precio(priceProd.get())

    setSelectProducto ()

def deleteProducto() :
    """Eliminar producto

    Metodo que elimina el producto seleccionado en la lista de productos.

    :return:
    """
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaProductos()
    producto = lista[whichProductoSelected()]
    sucursal.eliminarProducto(producto)

    setSelectProducto ()

def loadProducto() :
    """Consultar producto

    Metodo que lee el producto seleccionado y coloca sus datos en los campos.

    :return:
    """
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
    """Sucursal seleccionada

    Metodo que nos devuelve la sucursal que tenemos seleccionada en la lista de sucursales.

    :return: sucursal seleccionada
    """
    return int(selectSucursal.curselection()[0])

def addSucursal() :
    """Agregar sucursal

    Metodo que crea una sucursal con los datos que hay en los campos y la agrega a la lista de sucursales.

    :return:
    """
    sucursal = Sucursal(nameSuc.get(),dirSuc.get(),idSuc.get())
    listaSucursales.append(sucursal)

    setSelectSucursal ()


def updateSucursal() :
    """Modificar sucursal

    Metodo que actualiza la sucursal con los datos que hay en los campos.

    :return:
    """
    sucursal = sucursalSeleccionada
    sucursal.set_nombre(nameSuc.get())
    sucursal.set_direccion(dirSuc.get())
    sucursal.set_ID(idSuc.get())
    setSelectSucursal ()



def deleteSucursal() :
    """Eliminar sucursal

    Metodo que elimina la sucursal seleccionada en la lista de sucursales.

    :return:
    """
    del listaSucursales[whichSucursalSelected()]
    setSelectSucursal ()


def loadSucursal() :
    """Consultar sucursal

    Metodo que lee la sucursal seleccionada y coloca sus datos en los campos.
    Este metodo ademas muestra las listas de productos, empleados, proveedores e incidencias de la sucursal.

    :return:
    """
    global sucursalSeleccionada
    sucursal = listaSucursales[whichSucursalSelected()]
    sucursalSeleccionada = sucursal
    nameSuc.set(sucursal.get_nombre())
    dirSuc.set(sucursal.get_direccion())
    idSuc.set(sucursal.get_ID())
    limpiarVariables()
    setSelectProducto ()
    setSelectEmpleado()
    setSelectProveedor()
    setSelectIncidencia()

#Metodos empleados
def whichEmpleadoSelected() :
    """Empleado seleccionado

    Metodo que nos devuelve el empleado que tenemos seleccionado en la lista de empleados.

    :return: empleado seleccionado
    """
    return int(selectEmpleado.curselection()[0])

def addEmpleado() :
    """Agregar empleado

    Metodo que crea un nuevo empleado con los datos que hay en los campos y lo agrega a la lista de empleados de la sucursal

    :return:
    """
    sucursal = sucursalSeleccionada
    empleado = Empleado(idEmp.get(),dniEmp.get(),nameEmp.get(),telEmp.get(),dirEmp.get(),salEmp.get(),horEmp.get())
    sucursal.aniadirEmpleado(empleado)
    setSelectEmpleado ()

def updateEmpleado() :
    """Modificar empleado

    Metodo que actualiza el empleado con los datos que hay en los campos.

    :return:
    """
    empleado = empleadoSeleccionado
    empleado.set_nombre(nameEmp.get())
    empleado.set_ID(idEmp.get())
    empleado.set_direccion(dirEmp.get())
    empleado.set_DNI(dniEmp.get())
    empleado.set_telefono(telEmp.get())
    empleado.set_salario(salEmp.get())
    empleado.set_horario(horEmp.get())
    setSelectEmpleado ()

def deleteEmpleado() :
    """Eliminar empleado

    Metodo que elimina el empleado seleccionado en la lista de empleados.

    :return:
    """
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaEmpleados()
    empleado = lista[whichEmpleadoSelected()]
    sucursal.eliminarEmpleado((empleado))
    setSelectEmpleado ()

def loadEmpleado() :
    """Consultar empleado

    Metodo que lee el empleado seleccionado y coloca sus datos en los campos.

    :return:
    """
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
    salEmp.set(empleado.get_salario())
    horEmp.set(empleado.get_horario())

def salTotalEmpleado() :
    """Salario total

    Metodo que obtiene el salario total de los empleados de la sucursal seleccionada

    :return:
    """
    sucursal = sucursalSeleccionada
    salTotalEmp.set(sucursal.get_salario_total())

#Metodos proveedores
def whichProveedorSelected() :
    """Proveedor seleccionado

    Metodo que nos devuelve el proveedor que tenemos seleccionado en la lista de proveedores.

    :return: proveedor seleccionado
    """
    return int(selectProveedor.curselection()[0])

def addProveedor() :
    """Agregar proveedor

    Metodo que crea un nuevo proveedor con los datos que hay en los campos y lo agrega a la lista de proveedores de la sucursal

    :return:
    """
    sucursal = sucursalSeleccionada
    proveedor = Proveedor(idPro.get(),dniPro.get(),namePro.get(),telPro.get(),dirPro.get())
    sucursal.aniadirProveedor(proveedor)
    setSelectProveedor ()

def updateProveedor() :
    """Modificar proveedor

    Metodo que actualiza el proveedor con los datos que hay en los campos.

    :return:
    """
    proveedor = proveedorSeleccionado
    proveedor.set_nombre(namePro.get())
    proveedor.set_ID(idPro.get())
    proveedor.set_direccion(dirPro.get())
    proveedor.set_DNI(dniPro.get())
    proveedor.set_telefono(telPro.get())
    setSelectProveedor()

def deleteProveedor() :
    """Eliminar proveedor

    Metodo que elimina el proveedor seleccionado en la lista de proveedores.

    :return:
    """
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaProveedores()
    proveedor = lista[whichProveedorSelected()]
    sucursal.eliminarProveedor(proveedor)
    setSelectProveedor ()

def loadProveedor() :
    """Consultar proveedor

    Metodo que lee el proveedor seleccionado y coloca sus datos en los campos.

    :return:
    """
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

#INCIDENCIA
def whichIncidenciaSelected() :
    """Incidencia seleccionada

    Metodo que nos devuelve la incidencia que tenemos seleccionad en la lista de incidencias.

    :return: incidencia seleccionada
    """
    return int(selectIncidencia.curselection()[0])

def addIncidencia() :
    """Agregar incidencia

    Metodo que crea una nueva incidencia con los datos que hay en los campos y la agrega a la lista de incidencias de la sucursal

    :return:
    """
    sucursal = sucursalSeleccionada
    incidencia = Incidencia(idInc.get(),asuInc.get(),desInc.get())
    sucursal.aniadirIncidencia(incidencia)
    setSelectIncidencia ()

def updateIncidencia() :
    """Modificar incidencia

    Metodo que actualiza la incidencia con los datos que hay en los campos.

    :return:
    """
    incidencia = incidenciaSeleccionada
    incidencia.set_ID(idInc.get())
    incidencia.set_asunto(asuInc.get())
    incidencia.set_descripcion(desInc.get())
    setSelectIncidencia()

def deleteIncidencia() :
    """Eliminar incidencia

    Metodo que elimina la incidencia seleccionada en la lista de incidencias.

    :return:
    """
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaIncidencias()
    incidencia = lista[whichIncidenciaSelected()]
    sucursal.eliminarIncidencia(incidencia)
    setSelectIncidencia ()

def loadIncidencia() :
    """Consultar incidencia

    Metodo que lee la incidencia seleccionada y coloca sus datos en los campos.

    :return:
    """
    global incidenciaSeleccionada
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaIncidencias()
    incidencia  = lista[whichIncidenciaSelected()]
    incidenciaSeleccionada = incidencia
    idInc.set(incidencia.get_ID())
    asuInc.set(incidencia.get_asunto())
    desInc.set(incidencia.get_descripcion())
    estInc.set(incidencia.get_estado())

def resolverIncidencia() :
    """Resolver incidencia

    Metodo que cambia el estado de la incidencia de "Abierta" a "Resuelta".

    :return:
    """
    sucursal = sucursalSeleccionada
    lista = sucursal.get_listaIncidencias()
    incidencia = lista[whichIncidenciaSelected()]
    incidencia.resolver()
    estInc.set(incidencia.get_estado())
    setSelectIncidencia ()

def makeWindow () :
    """Crear ventana

    Metodo que crea la interfaz grafica para el usuario. En este metodo se reune la creacion de todos los botones, campos, pestañas, etc de la ventana de la aplicacion.

    :return:
    """
    global nameProd, priceProd, idProd, nameSuc, dirSuc, idSuc, idEmp, dniEmp, nameEmp, telEmp, dirEmp, salEmp, horEmp, idPro, dniPro, namePro,telPro,dirPro, telEmp, dirEmp, salTotalEmp, idInc, asuInc, desInc, estInc, selectIncidencia, selectProducto, selectSucursal, selectEmpleado, selectProveedor
    win = Tk()
    win.title("Gestion de Sucursales")
    frameSucursal = ttk.Labelframe(win, text="Lista de Sucursales")

    frame1 = Frame(frameSucursal)
    frameSucursal.pack()
    frame1.pack()
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
    b6 = Button(frame2,text="Modificar",command=updateSucursal)
    b7 = Button(frame2,text="Eliminar",command=deleteSucursal)
    b8 = Button(frame2,text=" Consultar ",command=loadSucursal)
    b5.pack(side=LEFT); b6.pack(side=LEFT)
    b7.pack(side=LEFT); b8.pack(side=LEFT)

    frame3 = Frame(frameSucursal)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    selectSucursal = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectSucursal.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectSucursal.pack(side=LEFT,  fill=BOTH, expand=1)

    n = ttk.Notebook(win)
    n.pack()

    #PRODUCTOS

    frameProducto = ttk.Labelframe(n, text="Lista de Productos")
    frameProducto.pack()
    n.add(frameProducto, text="Productos")

    frame4 = Frame(frameProducto)
    frame4.pack()
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

    frameEmpleado = ttk.Labelframe(n, text="Lista de Empleados")
    frameEmpleado.pack(fill = BOTH)
    n.add(frameEmpleado, text="Empleados")
    frame7 = Frame(frameEmpleado)
    frame7.pack()
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

    Label(frame7, text="Salario").grid(row=6, column=4, sticky=W)
    salEmp= StringVar()
    sal= Entry(frame7, textvariable=salEmp)
    sal.grid(row=6, column=5, sticky=W)

    Label(frame7, text="Horario").grid(row=7, column=4, sticky=W)
    horEmp= StringVar()
    hor= Entry(frame7, textvariable=horEmp)
    hor.grid(row=7, column=5, sticky=W)

    frame8 = Frame(frameEmpleado)       # Row of buttons
    frame8.pack()
    b9 = Button(frame8,text=" Agregar",command=addEmpleado)
    b10 = Button(frame8,text="Modificar",command=updateEmpleado)
    b11 = Button(frame8,text="Eliminar",command=deleteEmpleado)
    b12 = Button(frame8,text="Consultar",command=loadEmpleado)

    b9.pack(side=LEFT); b10.pack(side=LEFT)
    b11.pack(side=LEFT); b12.pack(side=LEFT)


    frame9 = Frame(frameEmpleado)       # select of names
    frame9.pack()
    scroll = Scrollbar(frame9, orient=VERTICAL)
    selectEmpleado = Listbox(frame9, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectEmpleado.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectEmpleado.pack(side=LEFT, expand=1)

    b12a = Button(frameEmpleado,text="Salario total",command=salTotalEmpleado)
    b12a.pack(side=LEFT)
    salTotalEmp = StringVar()
    salTotal= Entry(frameEmpleado, textvariable=salTotalEmp, state=DISABLED)
    salTotal.pack(side=LEFT)




    #Proveedores

    frameProveedor = ttk.Labelframe(n, text="Lista de Proveedores")
    frameProveedor.pack(side = LEFT)
    n.add(frameProveedor, text="Proveedores")
    frame10 = Frame(frameProveedor)
    frame10.pack()
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
    b13 = Button(frame11,text=" Agregar",command=addProveedor)
    b14 = Button(frame11,text="Modificar",command=updateProveedor)
    b15 = Button(frame11,text="Eliminar",command=deleteProveedor)
    b16 = Button(frame11,text=" Consultar",command=loadProveedor)
    b13.pack(side=LEFT); b14.pack(side=LEFT)
    b15.pack(side=LEFT); b16.pack(side=LEFT)

    frame12 = Frame(frameProveedor)       # select of names
    frame12.pack()
    scroll = Scrollbar(frame12, orient=VERTICAL)
    selectProveedor = Listbox(frame12, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectProveedor.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectProveedor.pack(side=LEFT,  fill=BOTH, expand=1)

    #Incidencias
    frameIncidencia = ttk.Labelframe(n, text="Lista de Incidencias")
    frameIncidencia.pack(side = LEFT)
    n.add(frameIncidencia, text="Incidencias")
    frame13 = Frame(frameIncidencia)
    frame13.pack()
    Label(frame13, text="ID").grid(row=6, column=4, sticky=W)
    idInc = StringVar()
    id5 = Entry(frame13, textvariable=idInc)
    id5.grid(row=6, column=5, sticky=W)

    Label(frame13, text="Asunto").grid(row=7, column=4, sticky=W)
    asuInc = StringVar()
    asu= Entry(frame13, textvariable=asuInc)
    asu.grid(row=7, column=5, sticky=W)

    Label(frame13, text="Descripcion").grid(row=8, column=4, sticky=W)
    desInc= StringVar()
    des= Entry(frame13, textvariable=desInc)
    des.grid(row=8, column=5, sticky=W)

    Label(frame13, text="Estado").grid(row=9, column=4, sticky=W)
    estInc= StringVar()
    est= Entry(frame13, textvariable=estInc, state=DISABLED)
    est.grid(row=9, column=5, sticky=W)

    frame14 = Frame(frameIncidencia)       # Row of buttons
    frame14.pack()
    b17 = Button(frame14,text=" Agregar",command=addIncidencia)
    b18 = Button(frame14,text="Modificar",command=updateIncidencia)
    b19 = Button(frame14,text="Eliminar",command=deleteIncidencia)
    b20 = Button(frame14,text="Consultar",command=loadIncidencia)
    b21 = Button(frame14,text="Resolver",command=resolverIncidencia)

    b17.pack(side=LEFT); b18.pack(side=LEFT);
    b19.pack(side=LEFT); b20.pack(side=LEFT);b21.pack(side=LEFT)

    frame15 = Frame(frameIncidencia)       # select of names
    frame15.pack()
    scroll = Scrollbar(frame15, orient=VERTICAL)
    selectIncidencia = Listbox(frame15, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectIncidencia.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectIncidencia.pack(side=LEFT,  fill=BOTH, expand=1)

    return win

def setSelectSucursal () :
    """Lista seleccion sucursales

    Metodo que actualiza la lista de sucursales en el cuadro de seleccion.

    :return:
    """

    listaSucursales.sort()
    selectSucursal.delete(0,END)
    for sucursal in listaSucursales :
        selectSucursal.insert(END, sucursal.get_ID())

def setSelectProducto () :
    """Lista seleccion productos

    Metodo que actualiza la lista de productos en el cuadro de seleccion.

    :return:
    """

    sucursal = sucursalSeleccionada
    selectProducto.delete(0,END)
    lista = sucursal.get_listaProductos()
    for producto in lista :
        selectProducto.insert (END, producto.get_ID())

def setSelectEmpleado() :
    """Lista seleccion empleados

    Metodo que actualiza la lista de empleados en el cuadro de seleccion.

    :return:
    """
    sucursal = sucursalSeleccionada
    selectEmpleado.delete(0,END)
    lista = sucursal.get_listaEmpleados()
    for empleado in lista :
        selectEmpleado.insert(END, empleado.get_ID())

def setSelectProveedor() :
    """Lista seleccion proveedores

    Metodo que actualiza la lista de proveedores en el cuadro de seleccion.

    :return:
    """
    sucursal = sucursalSeleccionada
    selectProveedor.delete(0,END)
    lista = sucursal.get_listaProveedores()
    for proveedor in lista :
        selectProveedor.insert(END, proveedor.get_ID())

def setSelectIncidencia() :
    """Lista seleccion incidencias

    Metodo que actualiza la lista de incidencias en el cuadro de seleccion.

    :return:
    """
    sucursal = sucursalSeleccionada
    selectIncidencia.delete(0,END)
    lista = sucursal.get_listaIncidencias()
    for incidencia in lista :
        selectIncidencia.insert(END, incidencia.get_ID())

win = makeWindow()
setSelectSucursal ()
win.mainloop()