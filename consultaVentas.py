import tkinter as tk
from tkinter import messagebox


class consultarVentas:
    def __init__(self):
        self.root_cVent = tk.Tk()
        self.root_cVent.title("Ver Venta")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_cVent.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_cVent.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_cVent.geometry(posicion)

        self.root_cVent.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_cVent.mainloop()

    # Declaracion widgets
    def widgets(self):
        self.btn_menu = tk.Button(
            self.root_cVent, text="Volver al menu", font=('Arial', 12), command=self.volverMenu)
        self.btn_menu.pack(pady=8)

        self.frame = tk.Frame(self.root_cVent)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        btn1 = tk.Button(self.frame, text="Codigo", font=('Arial', 18))
        btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        btn2 = tk.Button(self.frame, text="Cedula", font=('Arial', 18))
        btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        btn3 = tk.Button(self.frame, text="Producto", font=('Arial', 18))
        btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

        btn4 = tk.Button(self.frame, text="Fecha", font=('Arial', 18))
        btn4.grid(row=0, column=3, sticky=tk.W+tk.E)

        btn5 = tk.Button(self.frame, text="Empleado", font=('Arial', 18))
        btn5.grid(row=0, column=4, sticky=tk.W+tk.E)

        btn6 = tk.Button(self.frame, text="Total", font=('Arial', 18))
        btn6.grid(row=0, column=5, sticky=tk.W+tk.E)

        registroCod1 = tk.Button(self.frame, text="01", font=(
            'Arial', 12)).grid(row=1, column=0, sticky=tk.W+tk.E)
        registroCed1 = tk.Button(self.frame, text="Cedula01", font=(
            'Arial', 12)).grid(row=1, column=1, sticky=tk.W+tk.E)
        registroProd1 = tk.Button(self.frame, text="Producto01", font=(
            'Arial', 12)).grid(row=1, column=2, sticky=tk.W+tk.E)
        registroFech1 = tk.Button(self.frame, text="01/01/2023",
                                  font=('Arial', 12)).grid(row=1, column=3, sticky=tk.W+tk.E)
        registroEmp1 = tk.Button(self.frame, text="Empleado01", font=(
            'Arial', 12)).grid(row=1, column=4, sticky=tk.W+tk.E)
        registroTot1 = tk.Button(self.frame, text="1111", font=(
            'Arial', 12)).grid(row=1, column=5, sticky=tk.W+tk.E)

        registroCod2 = tk.Button(self.frame, text="02", font=(
            'Arial', 12)).grid(row=2, column=0, sticky=tk.W+tk.E)
        registroCed2 = tk.Button(self.frame, text="Cedula02", font=(
            'Arial', 12)).grid(row=2, column=1, sticky=tk.W+tk.E)
        registroProd2 = tk.Button(self.frame, text="Producto02", font=(
            'Arial', 12)).grid(row=2, column=2, sticky=tk.W+tk.E)
        registroFech2 = tk.Button(self.frame, text="02/02/2023",
                                  font=('Arial', 12)).grid(row=2, column=3, sticky=tk.W+tk.E)
        registroEmp2 = tk.Button(self.frame, text="Empleado02", font=(
            'Arial', 12)).grid(row=2, column=4, sticky=tk.W+tk.E)
        registroTot2 = tk.Button(self.frame, text="2222", font=(
            'Arial', 12)).grid(row=2, column=5, sticky=tk.W+tk.E)

        registroCod3 = tk.Button(self.frame, text="03", font=(
            'Arial', 12)).grid(row=3, column=0, sticky=tk.W+tk.E)
        registroCed3 = tk.Button(self.frame, text="Cedula03", font=(
            'Arial', 12)).grid(row=3, column=1, sticky=tk.W+tk.E)
        registroProd3 = tk.Button(self.frame, text="Producto03", font=(
            'Arial', 12)).grid(row=3, column=2, sticky=tk.W+tk.E)
        registroFech3 = tk.Button(self.frame, text="03/03/2023",
                                  font=('Arial', 12)).grid(row=3, column=3, sticky=tk.W+tk.E)
        registroEmp3 = tk.Button(self.frame, text="Empleado03", font=(
            'Arial', 12)).grid(row=3, column=4, sticky=tk.W+tk.E)
        registroTot3 = tk.Button(self.frame, text="3333", font=(
            'Arial', 12)).grid(row=3, column=5, sticky=tk.W+tk.E)

        self.frame.pack(fill="x")

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_cVent.destroy()

    def volverMenu(self):
        if messagebox.askyesno(title="Volver al menu", message="Desea volver al menu inicial?"):
            self.root_cVent.withdraw()
            from menu import Menu
            self.root_cVent.destroy()
            Menu()


verInv = consultarVentas()
