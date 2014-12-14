__author__ = 'Polo'

from Tkinter import *
from Producto import *
from Sucursal import *
from Empleado import *
from Proveedor import *
from Incidencia import *
import ttk

lista_sucursales = []


def limpiar_variables():
    """Limpieza de variables

    Metodo que elimina los datos de los campos de producto, empleado, proveedor e incidencia.

    :return:
    """
    name_prod.set("")
    price_prod.set("")
    id_prod.set("")
    id_emp.set("")
    dni_emp.set("")
    name_emp.set("")
    tel_emp.set("")
    dir_emp.set("")
    sal_emp.set("")
    hor_emp.set("")
    id_pro.set("")
    dni_pro.set("")
    name_pro.set("")
    tel_pro.set("")
    dir_pro.set("")
    id_inc.set("")
    asu_inc.set("")
    des_inc.set("")
    est_inc.set("")


    #PRODUCTOS

def which_producto_selected():
    """Producto seleccionado

    Metodo que nos devuelve el producto que tenemos seleccionado en la lista de productos.

    :return: producto seleccionado
    """
    return int(select_producto.curselection()[0])


def add_producto():
    """Agregar producto

    Metodo que crea un nuevo producto con los datos que hay en los campos y
    lo agrega a la lista de productos de la sucursal

    :return:
    """
    sucursal = sucursal_seleccionada
    producto = Producto(id_prod.get(), name_prod.get(), price_prod.get())
    sucursal.aniadir_producto(producto)

    set_select_producto()


def update_producto():
    """Modificar producto

    Metodo que actualiza el producto con los datos que hay en los campos.

    :return:
    """
    producto = producto_seleccionado
    producto.set_id(id_prod.get())
    producto.set_nombre(name_prod.get())
    producto.set_precio(price_prod.get())

    set_select_producto()


def delete_producto():
    """Eliminar producto

    Metodo que elimina el producto seleccionado en la lista de productos.

    :return:
    """
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaproductos()
    producto = lista[which_producto_selected()]
    sucursal.eliminar_producto(producto)

    set_select_producto()


def load_producto():
    """Consultar producto

    Metodo que lee el producto seleccionado y coloca sus datos en los campos.

    :return:
    """
    global producto_seleccionado
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaproductos()
    producto = lista[which_producto_selected()]
    producto_seleccionado = producto
    id_prod.set(producto.get_id())
    name_prod.set(producto.get_nombre())
    price_prod.set(producto.get_precio())


    #SUCURSALES

def which_sucursal_selected():
    """Sucursal seleccionada

    Metodo que nos devuelve la sucursal que tenemos seleccionada en la lista de sucursales.

    :return: sucursal seleccionada
    """
    return int(select_sucursal.curselection()[0])


def add_sucursal():
    """Agregar sucursal

    Metodo que crea una sucursal con los datos que hay en los campos y la agrega a la lista de sucursales.

    :return:
    """
    sucursal = Sucursal(name_suc.get(), dir_suc.get(), id_suc.get())
    lista_sucursales.append(sucursal)

    set_select_sucursal()


def update_sucursal():
    """Modificar sucursal

    Metodo que actualiza la sucursal con los datos que hay en los campos.

    :return:
    """
    sucursal = sucursal_seleccionada
    sucursal.set_nombre(name_suc.get())
    sucursal.set_direccion(dir_suc.get())
    sucursal.set_id(id_suc.get())
    set_select_sucursal()


def delete_sucursal():
    """Eliminar sucursal

    Metodo que elimina la sucursal seleccionada en la lista de sucursales.

    :return:
    """
    del lista_sucursales[which_sucursal_selected()]
    set_select_sucursal()


def load_sucursal():
    """Consultar sucursal

    Metodo que lee la sucursal seleccionada y coloca sus datos en los campos.
    Este metodo ademas muestra las listas de productos, empleados, proveedores e incidencias de la sucursal.

    :return:
    """
    global sucursal_seleccionada
    sucursal = lista_sucursales[which_sucursal_selected()]
    sucursal_seleccionada = sucursal
    name_suc.set(sucursal.get_nombre())
    dir_suc.set(sucursal.get_direccion())
    id_suc.set(sucursal.get_id())
    limpiar_variables()
    set_select_producto()
    set_select_empleado()
    set_select_proveedor()
    set_select_incidencia()


    #EMPLEADOS

def which_empleado_selected():
    """Empleado seleccionado

    Metodo que nos devuelve el empleado que tenemos seleccionado en la lista de empleados.

    :return: empleado seleccionado
    """
    return int(select_empleado.curselection()[0])


def add_empleado():
    """Agregar empleado

    Metodo que crea un nuevo empleado con los datos que hay en los campos
    y lo agrega a la lista de empleados de la sucursal

    :return:
    """
    sucursal = sucursal_seleccionada
    empleado = Empleado\
        (id_emp.get(), dni_emp.get(), name_emp.get(), tel_emp.get(), dir_emp.get(), sal_emp.get(), hor_emp.get())
    sucursal.aniadir_empleado(empleado)
    set_select_empleado()


def update_empleado():
    """Modificar empleado

    Metodo que actualiza el empleado con los datos que hay en los campos.

    :return:
    """
    empleado = empleado_seleccionado
    empleado.set_nombre(name_emp.get())
    empleado.set_id(id_emp.get())
    empleado.set_direccion(dir_emp.get())
    empleado.set_dni(dni_emp.get())
    empleado.set_telefono(tel_emp.get())
    empleado.set_salario(sal_emp.get())
    empleado.set_horario(hor_emp.get())
    set_select_empleado()


def delete_empleado():
    """Eliminar empleado

    Metodo que elimina el empleado seleccionado en la lista de empleados.

    :return:
    """
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaempleados()
    empleado = lista[which_empleado_selected()]
    sucursal.eliminar_empleado(empleado)
    set_select_empleado()


def load_empleado():
    """Consultar empleado

    Metodo que lee el empleado seleccionado y coloca sus datos en los campos.

    :return:
    """
    global empleado_seleccionado
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaempleados()
    empleado = lista[which_empleado_selected()]
    empleado_seleccionado = empleado
    id_emp.set(empleado.get_id())
    dni_emp.set(empleado.get_dni())
    name_emp.set(empleado.get_nombre())
    tel_emp.set(empleado.get_telefono())
    dir_emp.set(empleado.get_direccion())
    sal_emp.set(empleado.get_salario())
    hor_emp.set(empleado.get_horario())


def sal_total_empleado():
    """Salario total

    Metodo que obtiene el salario total de los empleados de la sucursal seleccionada

    :return:
    """
    sucursal = sucursal_seleccionada
    sal_total_emp.set(sucursal.get_salario_total())


    #PROVEEDORES

def which_proveedor_selected():
    """Proveedor seleccionado

    Metodo que nos devuelve el proveedor que tenemos seleccionado en la lista de proveedores.

    :return: proveedor seleccionado
    """
    return int(select_proveedor.curselection()[0])


def add_proveedor():
    """Agregar proveedor

    Metodo que crea un nuevo proveedor con los datos que hay en los campos
    y lo agrega a la lista de proveedores de la sucursal

    :return:
    """
    sucursal = sucursal_seleccionada
    proveedor = Proveedor(id_pro.get(), dni_pro.get(), name_pro.get(), tel_pro.get(), dir_pro.get())
    sucursal.aniadir_proveedor(proveedor)
    set_select_proveedor()


def update_proveedor():
    """Modificar proveedor

    Metodo que actualiza el proveedor con los datos que hay en los campos.

    :return:
    """
    proveedor = proveedor_seleccionado
    proveedor.set_nombre(name_pro.get())
    proveedor.set_id(id_pro.get())
    proveedor.set_direccion(dir_pro.get())
    proveedor.set_dni(dni_pro.get())
    proveedor.set_telefono(tel_pro.get())
    set_select_proveedor()


def delete_proveedor():
    """Eliminar proveedor

    Metodo que elimina el proveedor seleccionado en la lista de proveedores.

    :return:
    """
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaproveedores()
    proveedor = lista[which_proveedor_selected()]
    sucursal.eliminar_proveedor(proveedor)
    set_select_proveedor()


def load_proveedor():
    """Consultar proveedor

    Metodo que lee el proveedor seleccionado y coloca sus datos en los campos.

    :return:
    """
    global proveedor_seleccionado
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaproveedores()
    proveedor = lista[which_proveedor_selected()]
    proveedor_seleccionado = proveedor
    id_pro.set(proveedor.get_id())
    dni_pro.set(proveedor.get_dni())
    name_pro.set(proveedor.get_nombre())
    tel_pro.set(proveedor.get_telefono())
    dir_pro.set(proveedor.get_direccion())


    #INCIDENCIAS

def which_incidencia_selected():
    """Incidencia seleccionada

    Metodo que nos devuelve la incidencia que tenemos seleccionad en la lista de incidencias.

    :return: incidencia seleccionada
    """
    return int(select_incidencia.curselection()[0])


def add_incidencia():
    """Agregar incidencia

    Metodo que crea una nueva incidencia con los datos que hay en los campos y
    la agrega a la lista de incidencias de la sucursal

    :return:
    """
    sucursal = sucursal_seleccionada
    incidencia = Incidencia(id_inc.get(), asu_inc.get(), des_inc.get())
    sucursal.aniadir_incidencia(incidencia)
    set_select_incidencia()


def update_incidencia():
    """Modificar incidencia

    Metodo que actualiza la incidencia con los datos que hay en los campos.

    :return:
    """
    incidencia = incidencia_seleccionada
    incidencia.set_id(id_inc.get())
    incidencia.set_asunto(asu_inc.get())
    incidencia.set_descripcion(des_inc.get())
    set_select_incidencia()


def delete_incidencia():
    """Eliminar incidencia

    Metodo que elimina la incidencia seleccionada en la lista de incidencias.

    :return:
    """
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaincidencias()
    incidencia = lista[which_incidencia_selected()]
    sucursal.eliminar_incidencia(incidencia)
    set_select_incidencia()


def load_incidencia():
    """Consultar incidencia

    Metodo que lee la incidencia seleccionada y coloca sus datos en los campos.

    :return:
    """
    global incidencia_seleccionada
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaincidencias()
    incidencia = lista[which_incidencia_selected()]
    incidencia_seleccionada = incidencia
    id_inc.set(incidencia.get_id())
    asu_inc.set(incidencia.get_asunto())
    des_inc.set(incidencia.get_descripcion())
    est_inc.set(incidencia.get_estado())


def resolver_incidencia():
    """Resolver incidencia

    Metodo que cambia el estado de la incidencia de "Abierta" a "Resuelta".

    :return:
    """
    sucursal = sucursal_seleccionada
    lista = sucursal.get_listaincidencias()
    incidencia = lista[which_incidencia_selected()]
    incidencia.resolver()
    est_inc.set(incidencia.get_estado())
    set_select_incidencia()


def make_window():
    """Crear ventana

    Metodo que crea la interfaz grafica para el usuario. En este metodo se reune la creacion de todos los botones,
    campos, etc de la ventana de la aplicacion.

    :return:
    """
    global name_prod, price_prod, id_prod, \
        name_suc, dir_suc, id_suc, \
        id_emp, dni_emp, name_emp, tel_emp, dir_emp,  sal_emp, sal_total_emp, hor_emp, \
        id_pro, dni_pro, name_pro, tel_pro, dir_pro, \
        id_inc, asu_inc, des_inc, est_inc, \
        select_incidencia, select_producto, select_sucursal, select_empleado, select_proveedor
    win = Tk()
    win.title("Gestion de Sucursales")
    frame_sucursal = ttk.Labelframe(win, text="Lista de Sucursales")

    frame1 = Frame(frame_sucursal)
    frame_sucursal.pack()
    frame1.pack()
    Label(frame1, text="Nombre").grid(row=1, column=0, sticky=W)
    name_suc = StringVar()
    name2 = Entry(frame1, textvariable=name_suc)
    name2.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Direccion").grid(row=2, column=0, sticky=W)
    dir_suc = StringVar()
    dir2 = Entry(frame1, textvariable=dir_suc)
    dir2.grid(row=2, column=1, sticky=W)

    Label(frame1, text="ID").grid(row=3, column=0, sticky=W)
    id_suc = StringVar()
    id2 = Entry(frame1, textvariable=id_suc)
    id2.grid(row=3, column=1, sticky=W)

    frame2 = Frame(frame_sucursal)  # Row of buttons
    frame2.pack()
    b5 = Button(frame2, text="Agregar", command=add_sucursal)
    b6 = Button(frame2, text="Modificar", command=update_sucursal)
    b7 = Button(frame2, text="Eliminar", command=delete_sucursal)
    b8 = Button(frame2, text="Consultar ", command=load_sucursal)
    b5.pack(side=LEFT)
    b6.pack(side=LEFT)
    b7.pack(side=LEFT)
    b8.pack(side=LEFT)

    frame3 = Frame(frame_sucursal)  # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select_sucursal = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select_sucursal.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select_sucursal.pack(side=LEFT, fill=BOTH, expand=1)

    n = ttk.Notebook(win)
    n.pack()

    #Productos

    frame_producto = ttk.Labelframe(n, text="Lista de Productos")
    frame_producto.pack()
    n.add(frame_producto, text="Productos")

    frame4 = Frame(frame_producto)
    frame4.pack()
    Label(frame4, text="Nombre").grid(row=5, column=0, sticky=W)
    name_prod = StringVar()
    name = Entry(frame4, textvariable=name_prod)
    name.grid(row=5, column=1, sticky=W)

    Label(frame4, text="Precio").grid(row=6, column=0, sticky=W)
    price_prod = StringVar()
    price = Entry(frame4, textvariable=price_prod)
    price.grid(row=6, column=1, sticky=W)

    Label(frame4, text="ID").grid(row=7, column=0, sticky=W)
    id_prod = StringVar()
    id1 = Entry(frame4, textvariable=id_prod)
    id1.grid(row=7, column=1, sticky=W)

    frame5 = Frame(frame_producto)  # Row of buttons
    frame5.pack()
    b1 = Button(frame5, text="Agregar", command=add_producto)
    b2 = Button(frame5, text="Modificar", command=update_producto)
    b3 = Button(frame5, text="Eliminar", command=delete_producto)
    b4 = Button(frame5, text="Consultar ", command=load_producto)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)

    frame6 = Frame(frame_producto)  # select of names
    frame6.pack()
    scroll = Scrollbar(frame6, orient=VERTICAL)
    select_producto = Listbox(frame6, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select_producto.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select_producto.pack(side=LEFT, fill=BOTH, expand=1)

    #Empleados

    frame_empleado = ttk.Labelframe(n, text="Lista de Empleados")
    frame_empleado.pack(fill=BOTH)
    n.add(frame_empleado, text="Empleados")
    frame7 = Frame(frame_empleado)
    frame7.pack()
    Label(frame7, text="Nombre empleado").grid(row=1, column=4, sticky=W)
    name_emp = StringVar()
    name3 = Entry(frame7, textvariable=name_emp)
    name3.grid(row=1, column=5, sticky=W)

    Label(frame7, text="Direccion").grid(row=2, column=4, sticky=W)
    dir_emp = StringVar()
    dir3 = Entry(frame7, textvariable=dir_emp)
    dir3.grid(row=2, column=5, sticky=W)

    Label(frame7, text="ID empleado").grid(row=3, column=4, sticky=W)
    id_emp = StringVar()
    id3 = Entry(frame7, textvariable=id_emp)
    id3.grid(row=3, column=5, sticky=W)

    Label(frame7, text="DNI").grid(row=4, column=4, sticky=W)
    dni_emp = StringVar()
    dni = Entry(frame7, textvariable=dni_emp)
    dni.grid(row=4, column=5, sticky=W)

    Label(frame7, text="Telefono").grid(row=5, column=4, sticky=W)
    tel_emp = StringVar()
    tel = Entry(frame7, textvariable=tel_emp)
    tel.grid(row=5, column=5, sticky=W)

    Label(frame7, text="Salario").grid(row=6, column=4, sticky=W)
    sal_emp = IntVar()
    sal = Entry(frame7, textvariable=sal_emp)
    sal.grid(row=6, column=5, sticky=W)

    Label(frame7, text="Horario").grid(row=7, column=4, sticky=W)
    hor_emp = StringVar()
    hor = Entry(frame7, textvariable=hor_emp)
    hor.grid(row=7, column=5, sticky=W)

    frame8 = Frame(frame_empleado)  # Row of buttons
    frame8.pack()
    b9 = Button(frame8, text="Agregar", command=add_empleado)
    b10 = Button(frame8, text="Modificar", command=update_empleado)
    b11 = Button(frame8, text="Eliminar", command=delete_empleado)
    b12 = Button(frame8, text="Consultar", command=load_empleado)

    b9.pack(side=LEFT)
    b10.pack(side=LEFT)
    b11.pack(side=LEFT)
    b12.pack(side=LEFT)

    frame9 = Frame(frame_empleado)  # select of names
    frame9.pack()
    scroll = Scrollbar(frame9, orient=VERTICAL)
    select_empleado = Listbox(frame9, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select_empleado.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select_empleado.pack(side=LEFT, expand=1)

    b12a = Button(frame_empleado, text="Salario total", command=sal_total_empleado)
    b12a.pack(side=LEFT)
    sal_total_emp = StringVar()
    sal_total = Entry(frame_empleado, textvariable=sal_total_emp, state=DISABLED)
    sal_total.pack(side=LEFT)

    #Proveedores

    frame_proveedor = ttk.Labelframe(n, text="Lista de Proveedores")
    frame_proveedor.pack(side=LEFT)
    n.add(frame_proveedor, text="Proveedores")
    frame10 = Frame(frame_proveedor)
    frame10.pack()
    Label(frame10, text="Nombre proveedores").grid(row=6, column=4, sticky=W)
    name_pro = StringVar()
    name4 = Entry(frame10, textvariable=name_pro)
    name4.grid(row=6, column=5, sticky=W)

    Label(frame10, text="Direccion").grid(row=7, column=4, sticky=W)
    dir_pro = StringVar()
    dir4 = Entry(frame10, textvariable=dir_pro)
    dir4.grid(row=7, column=5, sticky=W)

    Label(frame10, text="ID proveedor").grid(row=8, column=4, sticky=W)
    id_pro = StringVar()
    id4 = Entry(frame10, textvariable=id_pro)
    id4.grid(row=8, column=5, sticky=W)

    Label(frame10, text="DNI").grid(row=9, column=4, sticky=W)
    dni_pro = StringVar()
    dni2 = Entry(frame10, textvariable=dni_pro)
    dni2.grid(row=9, column=5, sticky=W)

    Label(frame10, text="Telefono").grid(row=10, column=4, sticky=W)
    tel_pro = StringVar()
    tel2 = Entry(frame10, textvariable=tel_pro)
    tel2.grid(row=10, column=5, sticky=W)

    frame11 = Frame(frame_proveedor)  # Row of buttons
    frame11.pack()
    b13 = Button(frame11, text="Agregar", command=add_proveedor)
    b14 = Button(frame11, text="Modificar", command=update_proveedor)
    b15 = Button(frame11, text="Eliminar", command=delete_proveedor)
    b16 = Button(frame11, text="Consultar", command=load_proveedor)
    b13.pack(side=LEFT)
    b14.pack(side=LEFT)
    b15.pack(side=LEFT)
    b16.pack(side=LEFT)

    frame12 = Frame(frame_proveedor)  # select of names
    frame12.pack()
    scroll = Scrollbar(frame12, orient=VERTICAL)
    select_proveedor = Listbox(frame12, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select_proveedor.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select_proveedor.pack(side=LEFT, fill=BOTH, expand=1)

    #Incidencias

    frame_incidencia = ttk.Labelframe(n, text="Lista de Incidencias")
    frame_incidencia.pack(side=LEFT)
    n.add(frame_incidencia, text="Incidencias")
    frame13 = Frame(frame_incidencia)
    frame13.pack()
    Label(frame13, text="ID").grid(row=6, column=4, sticky=W)
    id_inc = StringVar()
    id5 = Entry(frame13, textvariable=id_inc)
    id5.grid(row=6, column=5, sticky=W)

    Label(frame13, text="Asunto").grid(row=7, column=4, sticky=W)
    asu_inc = StringVar()
    asu = Entry(frame13, textvariable=asu_inc)
    asu.grid(row=7, column=5, sticky=W)

    Label(frame13, text="Descripcion").grid(row=8, column=4, sticky=W)
    des_inc = StringVar()
    des = Entry(frame13, textvariable=des_inc)
    des.grid(row=8, column=5, sticky=W)

    Label(frame13, text="Estado").grid(row=9, column=4, sticky=W)
    est_inc = StringVar()
    est = Entry(frame13, textvariable=est_inc, state=DISABLED)
    est.grid(row=9, column=5, sticky=W)

    frame14 = Frame(frame_incidencia)  # Row of buttons
    frame14.pack()
    b17 = Button(frame14, text="Agregar", command=add_incidencia)
    b18 = Button(frame14, text="Modificar", command=update_incidencia)
    b19 = Button(frame14, text="Eliminar", command=delete_incidencia)
    b20 = Button(frame14, text="Consultar", command=load_incidencia)
    b21 = Button(frame14, text="Resolver", command=resolver_incidencia)

    b17.pack(side=LEFT)
    b18.pack(side=LEFT)
    b19.pack(side=LEFT)
    b20.pack(side=LEFT)
    b21.pack(side=LEFT)

    frame15 = Frame(frame_incidencia)  # select of names
    frame15.pack()
    scroll = Scrollbar(frame15, orient=VERTICAL)
    select_incidencia = Listbox(frame15, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select_incidencia.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select_incidencia.pack(side=LEFT, fill=BOTH, expand=1)

    return win


def set_select_sucursal():
    """Lista seleccion sucursales

    Metodo que actualiza la lista de sucursales en el cuadro de seleccion.

    :return:
    """

    lista_sucursales.sort()
    select_sucursal.delete(0, END)
    for sucursal in lista_sucursales:
        select_sucursal.insert(END, sucursal.get_id())


def set_select_producto():
    """Lista seleccion productos

    Metodo que actualiza la lista de productos en el cuadro de seleccion.

    :return:
    """

    sucursal = sucursal_seleccionada
    select_producto.delete(0, END)
    lista = sucursal.get_listaproductos()
    for producto in lista:
        select_producto.insert(END, producto.get_id())


def set_select_empleado():
    """Lista seleccion empleados

    Metodo que actualiza la lista de empleados en el cuadro de seleccion.

    :return:
    """
    sucursal = sucursal_seleccionada
    select_empleado.delete(0, END)
    lista = sucursal.get_listaempleados()
    for empleado in lista:
        select_empleado.insert(END, empleado.get_id())


def set_select_proveedor():
    """Lista seleccion proveedores

    Metodo que actualiza la lista de proveedores en el cuadro de seleccion.

    :return:
    """
    sucursal = sucursal_seleccionada
    select_proveedor.delete(0, END)
    lista = sucursal.get_listaproveedores()
    for proveedor in lista:
        select_proveedor.insert(END, proveedor.get_id())


def set_select_incidencia():
    """Lista seleccion incidencias

    Metodo que actualiza la lista de incidencias en el cuadro de seleccion.

    :return:
    """
    sucursal = sucursal_seleccionada
    select_incidencia.delete(0, END)
    lista = sucursal.get_listaincidencias()
    for incidencia in lista:
        select_incidencia.insert(END, incidencia.get_id())
