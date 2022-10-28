import pandas as pd
from sqlalchemy import create_engine
from genericpath import isdir, isfile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from io import *
import os
from tkinter import filedialog as fd
#Definir ventana
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500,500)
ventana.title("Latitud - Longitud")
ventana.resizable(0,0)

def obtener_lat_long(): 

    engine = create_engine('mysql://root:matias1997@localhost/prueba_python')

    df=pd.read_sql_query("SELECT * FROM clientes c JOIN BI_CLIENTES_GEO g ON c.domicilio = g.domicilio; ", engine)
    df.to_csv('BI_CLIENTES_GEO.csv')



#Definir campos:
home_label = Label(ventana,
text="Latitud/Longitud",
font=("arial", 18),
bg = "lightgreen",fg="darkblue",
relief = GROOVE,
padx=20,pady=20)
home_label.pack()

opcion = Label(ventana,
text= "¿Qué desea hacer?",
font=("arial",18),
bg="darkgreen",fg="lightblue",
padx=20,pady=2)
opcion.pack()

elegir = Button(ventana, 
    text = "ELEGIR",
    font = ("arial", 18),
    bg = "lightgrey", fg = "black",
    padx = 20, pady = 20, 
    relief = "groove", bd = 10,
    command = obtener_lat_long())
elegir.pack()

#add_label = Label(ventana,text="Obtener Lat-Long")
#info_label = Label(ventana,text="Información")
#data_label = Label(ventana,text="Creado por SDS - 2022")
#add_frame = Frame(ventana)

#boton2 = Button(ventana, text="BIENVENIDO")

"""def home():    
    home_label.config(
            fg="white",
            bg="black",
            font=("Arial",30),
            padx=170,
            pady=20
    )
    home_label.grid(row=0,column=0)
    boton2.config(
        padx=15,
        bg="green",
        fg="white"
    )
    boton2.grid(row=1,column=0)
    boton2.config(command=obtenerlatlong)

    #Ocultar pantalla:
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

def obtenerlatlong():    
    add_label.config(
            fg="white",
            bg="black",
            font=("Arial",30),
            padx=110,
            pady=20
    )
    add_label.grid(row=0,column=0,columnspan=10)
    #Campos del formulario:
    add_frame.grid(row=1)
    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    add_separator.grid(row=4,column=1)
    boton.grid(row=5,column=1,sticky=E)
    boton.config(
        padx=15,
        bg="green",
        fg="white"
    )
    #Ocultar pantalla:
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    boton2.grid_remove()
 #   productos_box.grid_remove()

def getInfo():  
    info_label.config(
            fg="white",
            bg="black",
            font=("Arial",30),
            padx=150,
            pady=20
    )
    info_label.grid(row=0,column=0)
    data_label.grid(row=1,column=0)

    #Ocultar pantalla:
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
#    productos_box.grid_remove()
"""





#home()
#add_separator = Label(add_frame)
#boton = Button(add_frame,text="Obtener")#,command=sacarAlerta)

#Hacer el menú superior
#menu_superior = Menu(ventana)
#menu_superior.add_command(label="Inicio",command=home)
#menu_superior.add_command(label="Obtener Lat-Long",command=obtenerlatlong)
#menu_superior.add_command(label="Información",command=getInfo)
#menu_superior.add_command(label="Salir",command=ventana.quit)

#Cargar menú
#ventana.config(menu=menu_superior)

ventana.mainloop()