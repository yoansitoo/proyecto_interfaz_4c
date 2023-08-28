import tkinter as tk  
from tkinter import ttk
import tkinter as tk
import json
import ttkbootstrap as ttk 
with open('errores.json','r') as file:
    data = json.load(file)


def obtenerDesc():
        datos = codigo_entry.get()

        for dato in data['errores']:
             if dato['codigo'] == datos:
                  descripcion.config(text= dato['desc'])
                  break
             else:
                  descripcion.config(text="Codigo Erroneo")
#Crear ventana del programa
ventana = ttk.Window(themename="superhero") #crear pantalla
ventana.title("Scanner OBD")
# ventana.geometry("500x300")
ventana.resizable(0,0)

#mensaje
codigo = ttk.Label(ventana, text= "Ingrese el codigo de error:")
codigo.pack(pady=10, padx=10)
#cuadro de texto
codigo_entry = ttk.Entry(ventana)
codigo_entry.pack(pady=10, padx=10)
#boton
buscar_btn = ttk.Button(ventana, text="Buscar error", command=obtenerDesc)
buscar_btn.pack(pady=10, padx=10)

descripcion = ttk.Label(ventana, text="")
descripcion.pack()

ventana.mainloop() #mantendra ventana abierta

# #crear la ventana
# ventana = tk.Tk()
# ventana.title("Busqueda de error")

# titulo = ttk.Label(ventana, text="Ingresa el codigo", font="Calibri 24")
# titulo.pack(padx=10, pady=10)

# entrada_texto = ttk.Entry(ventana)
# entrada_texto.pack(padx=10, pady=10)

# btn_buscar = ttk.Button(ventana, text="Buscar codigo", command=obtenerValor)
# btn_buscar.pack(padx=10, pady=10)

# descripcion = ttk.Label(ventana,text="")
# descripcion.pack(padx=10, pady=10)

# ventana.mainloop() #va al final
