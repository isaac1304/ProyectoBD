import tkinter as tk
from tkinter import messagebox


class consultarInventario:
    def __init__(self):
        self.root_cInv = tk.Tk()
        self.root_cInv.title("Consultar Inventario")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_cInv.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_cInv.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_cInv.geometry(posicion)

        self.root_cInv.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_cInv.mainloop()

    # Creacion Widgets
    def widgets(self):

        self.btn_menu = tk.Button(
            self.root_cInv, text="Volver al menu", font=('Arial', 12), command=self.volverMenu)
        self.btn_menu.pack()

        self.frame = tk.Frame(self.root_cInv)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

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

        registroCod2 = tk.Button(self.frame, text="02", font=(
            'Arial', 12)).grid(row=2, column=0, sticky=tk.W+tk.E)
        registroNom2 = tk.Button(self.frame, text="NombreProducto01", font=(
            'Arial', 12)).grid(row=2, column=1, sticky=tk.W+tk.E)
        registroCat2 = tk.Button(self.frame, text="CategoriaProducto01", font=(
            'Arial', 12)).grid(row=2, column=2, sticky=tk.W+tk.E)
        registroPrec2 = tk.Button(self.frame, text="1111", font=(
            'Arial', 12)).grid(row=2, column=3, sticky=tk.W+tk.E)

        registroCod3 = tk.Button(self.frame, text="03", font=(
            'Arial', 12)).grid(row=3, column=0, sticky=tk.W+tk.E)
        registroNom3 = tk.Button(self.frame, text="NombreProducto01", font=(
            'Arial', 12)).grid(row=3, column=1, sticky=tk.W+tk.E)
        registroCat3 = tk.Button(self.frame, text="CategoriaProducto01", font=(
            'Arial', 12)).grid(row=3, column=2, sticky=tk.W+tk.E)
        registroPrec3 = tk.Button(self.frame, text="1111", font=(
            'Arial', 12)).grid(row=3, column=3, sticky=tk.W+tk.E)

        registroCod4 = tk.Button(self.frame, text="04", font=(
            'Arial', 12)).grid(row=4, column=0, sticky=tk.W+tk.E)
        registroNom4 = tk.Button(self.frame, text="NombreProducto01", font=(
            'Arial', 12)).grid(row=4, column=1, sticky=tk.W+tk.E)
        registroCat4 = tk.Button(self.frame, text="CategoriaProducto01", font=(
            'Arial', 12)).grid(row=4, column=2, sticky=tk.W+tk.E)
        registroPrec4 = tk.Button(self.frame, text="1111", font=(
            'Arial', 12)).grid(row=4, column=3, sticky=tk.W+tk.E)

        self.frame.pack(padx=10, pady=30)

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_cInv.destroy()

    def volverMenu(self):
        if messagebox.askyesno(title="Volver al menu", message="Desea volver al menu inicial?"):
            self.root_cInv.withdraw()
            from menu import Menu
            self.root_cInv.destroy()
            Menu()


consulta = consultarInventario()
