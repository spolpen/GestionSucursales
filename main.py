__author__ = 'Polo'

from Tkinter import *
from Producto import *
from Sucursal import *

#PRODUCTOS
producto = Producto("Producto1","Televisor",200)


#SUCURSALES
sucursal = Sucursal("Sevilla","Pino Montano","Sucursal1")
sucursal.aniadirProducto(producto)
sucursal2 = Sucursal("Malaga","Malaga","Sucursal2")
listaSucursales =[]
listaSucursales.append(sucursal)
listaSucursales.append(sucursal2)

#Metodos productos
def whichProductoSelected () :
    return int(select.curselection()[0])

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


def makeWindow () :
    global nameProd, priceProd, idProd, nameSuc, dirSuc, idSuc, select, selectSucursal
    win = Tk()

    frame1 = Frame(win)
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


    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b5 = Button(frame2,text=" Agregar2",command=addSucursal)
    b6 = Button(frame2,text="Modificar2",command=updateSucursal)
    b7 = Button(frame2,text="Eliminar2",command=deleteSucursal)
    b8 = Button(frame2,text=" Consultar2 ",command=loadSucursal)
    b5.pack(side=LEFT); b6.pack(side=LEFT)
    b7.pack(side=LEFT); b8.pack(side=LEFT)

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    selectSucursal = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=selectSucursal.yview)
    scroll.pack(side=RIGHT, fill=Y)
    selectSucursal.pack(side=LEFT,  fill=BOTH, expand=1)

    #PRODUCTOS
    frame4 = Frame(win)
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


    frame5 = Frame(win)       # Row of buttons
    frame5.pack()
    b1 = Button(frame5,text=" Agregar",command=addProducto)
    b2 = Button(frame5,text="Modificar",command=updateProducto)
    b3 = Button(frame5,text="Eliminar",command=deleteProducto)
    b4 = Button(frame5,text=" Consultar ",command=loadProducto)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    frame6 = Frame(win)       # select of names
    frame6.pack()
    scroll = Scrollbar(frame6, orient=VERTICAL)
    select = Listbox(frame6, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)

    return win

def setSelectSucursal () :

    listaSucursales.sort()
    selectSucursal.delete(0,END)
    for sucursal in listaSucursales :
        selectSucursal.insert(END, sucursal.get_ID())

def setSelectProducto () :

    sucursal = sucursalSeleccionada
    select.delete(0,END)
    lista = sucursal.get_listaProductos()
    for producto in lista :
        select.insert (END, producto.get_ID())


win = makeWindow()
setSelectSucursal ()
win.mainloop()
