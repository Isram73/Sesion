#Crhistopher Isram Mancilla Laure
#07 de Marzo del 2023

from tkinter import* #Esta es una forma de importar paquetes de Python 
from tkinter import ttk 

class Sesion:
    def __init__(self, raiz):
        raiz.title("Inicio de sesión")

        self.usuario = StringVar()
        self.Contraseña = StringVar()

        mainFrame = ttk.Frame(raiz, padding = "12 12 15 15")
        mainFrame.grid(column=0, row=0)

        usuarioEntry = ttk.Entry(mainFrame, width = 30, textvariable=self.usuario)
        usuarioEntry.grid(column=2, row=2)
        contraseñaEntry = ttk.Entry(mainFrame, width = 30, textvariable=self.Contraseña)
        contraseñaEntry.grid(column=2, row=4)

        ttk.Label(mainFrame, text="").grid(column=1, row=3)
        ttk.Label(mainFrame, text="Usuario:").grid(column=1, row=2)
        ttk.Label(mainFrame, text="").grid(column=1, row=5)
        ttk.Label(mainFrame, text="Contraseña: ").grid(column=1, row=4)

        ttk.Button(mainFrame, text="Ingresar").grid(column=2, row=6, sticky=(E))

if __name__=="__main__":
    print("Este es el archivo principal")
    print("Nada más se mostrará esto si es el principal")