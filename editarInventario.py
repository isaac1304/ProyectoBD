import tkinter as tk
from tkinter import messagebox


class verInventario:
    def __init__(self):
        self.root_vInv = tk.Tk()
        self.root_vInv.title("Ver Producto")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_vInv.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_vInv.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_vInv.geometry(posicion)

        self.root_vInv.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_vInv.mainloop()

    def widgets(self):
        self.btn_menu = tk.Button(
            self.root_vInv, text="Volver al menu", font=('Arial', 12), command=self.volverMenu)
        self.btn_menu.pack(pady=8)

        self.frame = tk.Frame(self.root_vInv)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        btn1 = tk.Button(self.frame, text="Codigo", font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn2 = tk.Button(self.frame, text="Nombre", font=('Arial', 18))
        btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        btn3 = tk.Button(self.frame, text="Categoria", font=('Arial', 18))
        btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

        btn4 = tk.Button(self.frame, text="Precio", font=('Arial', 18))
        btn4.grid(row=0, column=3, sticky=tk.W+tk.E)

        registroCod1 = tk.Button(self.frame, text="01", font=(
            'Arial', 12)).grid(row=1, column=0, sticky=tk.W+tk.E)
        registroNom1 = tk.Button(self.frame, text="NombreProducto01", font=(
            'Arial', 12)).grid(row=1, column=1, sticky=tk.W+tk.E)
        registroCat1 = tk.Button(self.frame, text="CategoriaProducto01", font=(
            'Arial', 12)).grid(row=1, column=2, sticky=tk.W+tk.E)
        registroPrec1 = tk.Button(self.frame, text="1111", font=(
            'Arial', 12)).grid(row=1, column=3, sticky=tk.W+tk.E)
        registroEd1 = tk.Button(self.frame, text="Editar", font=(
            'Arial', 12)).grid(row=1, column=4, sticky=tk.W+tk.E)

        self.frame.pack(fill="x")

    def volverMenu(self):
        if messagebox.askyesno(title="Volver al menu", message="Desea volver al menu inicial?"):
            self.root_vInv.withdraw()
            from menu import Menu
            self.root_vInv.destroy()
            Menu()

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_vInv.destroy()


verInv = verInventario()
