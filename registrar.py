import tkinter as tk
import hashlib as hl
from tkinter import messagebox


class Registrar:
    def __init__(self):
        self.root_registrar = tk.Tk()
        self.root_registrar.title("Registrar Usuario")
        self.widgets()

        ancho_ventana = 900
        alto_ventana = 300

        # Proceso para centrar ventana en la pantalla
        x_ventana = self.root_registrar.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = self.root_registrar.winfo_screenheight() // 2 - alto_ventana // 2

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.root_registrar.geometry(posicion)

        self.root_registrar.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.root_registrar.mainloop()

    # Creacion de widgets
    def widgets(self):
        self.label_user = tk.Label(
            self.root_registrar, text="Ingrese el nombre de usuario", font=('Arial', 12)).pack(pady=30)

        self.usuario = tk.Text(self.root_registrar, height=1,
                               width=40, font=('Arial', 10))

        self.usuario.pack(padx=5, pady=5)

        self.label_pwd = tk.Label(
            self.root_registrar, text="Ingrese la contraseña", font=('Arial', 12)).pack(pady=10)

        self.pwd = tk.Text(self.root_registrar, height=1,
                           width=40, font=('Arial', 10))
        self.pwd.pack(padx=5, pady=5)

        self.label_conf_pwd = tk.Label(
            self.root_registrar, text="Ingrese nuevamente la contraseña", font=('Arial', 12)).pack(pady=10)

        self.conf_pwd = tk.Text(self.root_registrar, height=1,
                                width=40, font=('Arial', 10))
        self.conf_pwd.pack(padx=5, pady=5)

        self.btn = tk.Button(self.root_registrar, text="Ingresar", font=(
            'Arial', 12), command=self.registrar).pack(pady=15)

        self.registrar_btn = tk.Button(
            self.root_registrar, text="Registrar", font=('Arial', 12)).pack(pady=15)

    def registrar(self):
        correo = self.usuario.get("1.0",'end-1c')
        pwd = self.pwd.get("1.0",'end')
        conf_pwd = self.conf_pwd.get("1.0",'end')
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hl.md5(enc).hexdigest()
            with open('credentials.txt', 'a') as f:
                f.write('\n' + correo + '\n')
                f.write(hash1)
                f.close()
                print('You have registered successfully!')
        else:
            messagebox.showerror('Python Error', 'Error: Contraseñas no coinciden!')
            self.root_registrar.destroy()

    def cerrar(self):
        if messagebox.askyesno(title="Confirmacion", message="Desea cerrar el sistema?"):
            self.root_registrar.destroy()

    def login(self):
        self.root_registrar.withdraw()
        from login import Login
        Login()
        self.root_registrar.destroy()
registrar = Registrar()
