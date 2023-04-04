import tkinter as tk
from tkinter import messagebox


class buscarInventario:
    def __init__(self):
        self.root_eInv = tk.Tk()
        self.root_eInv.title("Editar Inventario")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_eInv.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_eInv.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_eInv.geometry(posicion)

        # Ejecuta tikinter
        self.root_eInv.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_eInv.mainloop()

    def widgets(self):
        self.btn_menu = tk.Button(
            self.root_eInv, text="Volver al menu", font=('Arial', 12), command=self.volverMenu)
        self.btn_menu.pack()

        self.frame = tk.Frame(self.root_eInv)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

        self.label = tk.Label(self.root_eInv, text="Ingrese el codigo del Producto", font=(
            'Arial', 18)).pack(pady=20)
        self.text = tk.Text(self.root_eInv, font=(
            'Arial', 12), height=1, width=20).pack(pady=10)
        self.btn = tk.Button(self.root_eInv, text="Buscar", font=(
            'Arial', 14), command=self.buscar).pack()

    def buscar(self):
        self.root_eInv.withdraw()
        from editarInventario import verInventario
        verInventario(self.root_eInv)

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_eInv.destroy()

    def volverMenu(self):
        if messagebox.askyesno(title="Volver al menu", message="Desea volver al menu inicial?"):
            self.root_eInv.withdraw()
            from menu import Menu
            self.root_eInv.destroy()
            Menu()



buscar = buscarInventario()
