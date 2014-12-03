__author__ = 'Raul'

from Tkinter import *
from Empresa import *




def whichSelected () :
    print "At %s of %d" % (select.curselection(), len(sucursalList))
    return int(select.curselection()[0])

def addEntry () :
   sucursalList.append ([nameVar.get(), direcVar.get(),idVar.get()])
   setSelect ()

def updateEntry() :
    sucursalList[whichSelected()] = [nameVar.get(), direcVar.get(),idVar.get()]
    setSelect ()

def deleteEntry() :
    del sucursalList[whichSelected()]
    setSelect ()

def loadEntry  () :
    name,direc,id = sucursalList[whichSelected()]
    nameVar.set(name)
    direcVar.set(direc)
    idVar.set(id)

def makeWindow () :
    global nameVar, direcVar,idVar, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Nombre").grid(row=2, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Direccion").grid(row=1, column=0, sticky=W)
    direcVar= StringVar()
    direc= Entry(frame1, textvariable=direcVar)
    direc.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Id").grid(row=0, column=0, sticky=W)
    idVar = StringVar()
    id = Entry(frame1, textvariable=idVar)
    id.grid(row=0, column=1, sticky=W)

    frame2 = Frame(win)
    frame2.pack()
    b1 = Button(frame2,text="Dar de alta",command=addEntry)
    b2 = Button(frame2,text="Modificar",command=updateEntry)
    b3 = Button(frame2,text="Borrar",command=deleteEntry)
    b4 = Button(frame2,text=" Consultar ",command=loadEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    frame3 = Frame(win)
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

def setSelect () :
    sucursalList.sort()
    select.delete(0,END)
    for name,direc,id in sucursalList :
        select.insert (END, id)

win = makeWindow()
setSelect ()
win.mainloop()
