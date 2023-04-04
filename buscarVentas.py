import tkinter as tk
from tkinter import messagebox


class buscarVentas:
    def __init__(self):
        self.root_bVent = tk.Tk()
        self.root_bVent.title("Editar Ventas")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_bVent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_bVent.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_bVent.geometry(posicion)

        self.root_bVent.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_bVent.mainloop()

    # Creacion widgets
    def widgets(self):
        self.btn_menu = tk.Button(
            self.root_bVent, text="Volver al menu", font=('Arial', 12), command=self.volverMenu)
        self.btn_menu.pack(pady=8)

        self.frame = tk.Frame(self.root_bVent)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

        self.label = tk.Label(self.root_bVent, text="Ingrese el codigo de factura", font=(
            'Arial', 18)).pack(pady=20)
        self.text = tk.Text(self.root_bVent, font=(
            'Arial', 12), height=1, width=20).pack(pady=10)
        self.btn = tk.Button(self.root_bVent, text="Buscar", font=(
            'Arial', 14), command=self.buscar).pack()

    # Metodos
    def buscar(self):
        self.root_bVent.withdraw()
        from editarVentas import editarVentas
        editarVentas()

    def volverMenu(self):
        if messagebox.askyesno(title="Volver al menu", message="Desea volver al menu inicial?"):
            self.root_bVent.withdraw()
            from menu import Menu
            self.root_bVent.destroy()
            Menu()

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_bVent.destroy()


buscar = buscarVentas()
