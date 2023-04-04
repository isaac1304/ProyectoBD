import tkinter as tk
from tkinter import messagebox, ttk


class generarReporte:
    def __init__(self):
        self.root_rep = tk.Tk()
        self.root_rep.title("Generar Reporte")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_rep.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_rep.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_rep.geometry(posicion)

        self.root_rep.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_rep.mainloop()

    def widgets(self):

        self.btn_menu = tk.Button(
            self.root_rep, text="Volver al menu", font=('Arial', 12), command=self.volverMenu)
        self.btn_menu.pack()

        self.label = tk.Label(
            self.root_rep, text="Generacion de Reportes", font=('Arial', 18)).pack(pady=5)

        # 1 si el checkbox esta seleccionado, 0 si no lo esta
        self.check_estado_sem = tk.IntVar()
        self.check_estado_men = tk.IntVar()
        self.check_estado_an = tk.IntVar()

        self.check_sem = tk.Checkbutton(
            self.root_rep, text="Semanal", font=('Arial', 14), variable=self.check_estado_sem)
        self.check_men = tk.Checkbutton(
            self.root_rep, text="Mensual", font=('Arial', 14), variable=self.check_estado_men)
        self.check_an = tk.Checkbutton(
            self.root_rep, text="Anual", font=('Arial', 14), variable=self.check_estado_an)

        self.check_sem.pack()
        self.check_men.pack()
        self.check_an.pack()

        self.combo = ttk.Combobox(
            self.root_rep,
            values=["Inventario", "Facturas", "Colaboradores", "Proveedores"]
        )
        self.combo.pack(padx=150, pady=10)
        self.btn = tk.Button(self.root_rep, text="Generar",
                             font=('Arial', 14), command=self.generar).pack(pady=5)

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_rep.destroy()

    def generar(self):
        # Obtener la opción seleccionada.
        self.reporte = self.combo.get()

        if self.check_estado_sem.get() == 1:
            messagebox.showinfo(
                message=f"Reporte Semanal de {self.reporte}",
                title="Reporte")
        else:
            if self.check_estado_men.get() == 1:
                messagebox.showinfo(
                    message=f"Reporte Mensual de {self.reporte}",
                    title="Reporte")
            else:
                if self.check_estado_an.get() == 1:
                    messagebox.showinfo(
                        message=f"Reporte Anual de {self.reporte}",
                        title="Reporte")
                else:
                    messagebox.showerror(
                        message=f"No se ha seleccionado el tipo de reporte deseado!", title="ERROR")

    def volverMenu(self):
        if messagebox.askyesno(title="Volver al menu", message="Desea volver al menu inicial?"):
            self.root_rep.withdraw()
            from menu import Menu
            self.root_rep.destroy()
            Menu()


report = generarReporte()
