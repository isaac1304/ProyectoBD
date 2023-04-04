import tkinter as tk
from tkinter import messagebox


class Menu:

    def __init__(self):
        self.root_menu = tk.Tk()
        self.root_menu.geometry("800x300")
        self.root_menu.title("Menu Opciones")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        #Proceso para centrar ventana en la pantalla
        x_ventana = self.root_menu.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_menu.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
               "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_menu.geometry(posicion)

        
        self.root_menu.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_menu.mainloop()

    def widgets(self):
        #Creacion widgets
        label = tk.Label(self.root_menu, text="Menu Sistema", font=(
            'Arial', 20)).pack()

        self.frame = tk.Frame(self.root_menu)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        btn1 = tk.Button(self.frame, text="Consultar Ventas", font=(
            'Arial', 18), command=self.cVent).grid(row=0, column=0, sticky=tk.W+tk.E)

        btn2 = tk.Button(self.frame, text="Editar Ventas", font=('Arial', 18), command=self.eVent).grid(
            row=0, column=1, sticky=tk.W+tk.E)

        btn3 = tk.Button(self.frame, text="Consultar Inventario", font=('Arial', 18), command=self.cInv).grid(
            row=1, column=0, sticky=tk.W+tk.E)

        btn4 = tk.Button(self.frame, text="Editar inventario", font=('Arial', 18), command=self.eInv).grid(
            row=1, column=1, sticky=tk.W+tk.E)

        self.frame.pack(fill='x', pady=20)
        btn5 = tk.Button(self.root_menu, text="Generar Reportes",
                         font=('Arial', 18), command=self.report).pack(fill='x')
        
        self.usuario = tk.Label(self.root_menu, text="Usuario: INSERTE NOMBRE DE USUARIO", font=('Arial',10)).pack(pady=25)



    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_menu.destroy()

    def cInv(self):
        self.root_menu.withdraw()
        from consultarInventario import consultarInventario
        self.root_menu.destroy()
        consultarInventario()

    def eInv(self):
        self.root_menu.withdraw()
        from buscarInventario import buscarInventario
        self.root_menu.destroy()
        buscarInventario()

    def cVent(self):
        self.root_menu.withdraw()
        from consultaVentas import consultarVentas
        self.root_menu.destroy()
        consultarVentas()

    def eVent(self):
        self.root_menu.withdraw()
        from buscarVentas import buscarVentas
        self.root_menu.destroy()
        buscarVentas()

    def report(self):
        self.root_menu.withdraw()
        from generarReporte import generarReporte
        self.root_menu.destroy()
        generarReporte()


menu = Menu()
# FIN CLASE MENU
