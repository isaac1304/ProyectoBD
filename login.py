import tkinter as tk
import hashlib as hl
from tkinter import messagebox


class Login:

    def __init__(self):

        self.root_login = tk.Tk()
        self.root_login.title("Login")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_login.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_login.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_login.geometry(posicion)

        self.root_login.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_login.mainloop()

    # Creacion de widgets
    def widgets(self):
        self.label_user = tk.Label(
            self.root_login, text="Ingrese el nombre de usuario", font=('Arial', 12)).pack(pady=30)

        self.usuario = tk.Text(self.root_login, height=1,
                               width=40, font=('Arial', 10))

        self.usuario.pack(padx=5, pady=5)

        self.label_pwd = tk.Label(
            self.root_login, text="Ingrese la contraseña", font=('Arial', 12)).pack(pady=10)

        self.pwd = tk.Text(self.root_login, height=1,
                           width=40, font=('Arial', 10))

        self.pwd.pack(padx=5, pady=5)

        self.btn = tk.Button(self.root_login, text="Ingresar", font=(
            'Arial', 12), command=self.ingresar).pack(pady=15)

        self.registrar_btn = tk.Button(self.root_login, text="Registrar", font=(
            'Arial', 12), command=self.registrar).pack(pady=15)

    # Metodo para ingresar
    def ingresar(self):
        email = self.usuario.get("1.0",'end-1c')
        pwd =  self.pwd.get("1.0",'end')
        auth = pwd.encode()
        auth_hash = hl.md5(auth).hexdigest()
        with open('credentials.txt', 'r') as f:
            stored_email, stored_pwd = f.read().splitlines()
        f.close()
        if email == stored_email and auth_hash == stored_pwd:
            self.root_login.withdraw()
            from menu import Menu
            Menu()
            self.root_login.destroy()
        else:
            messagebox.showerror('Python Error', 'Error: This is an Error Message!')
            self.root_login.destroy()

    def registrar(self):
        self.root_login.withdraw()
        from registrar import Registrar
        Registrar()
        self.root_login.destroy()

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_login.destroy()
login = Login()
