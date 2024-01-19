import customtkinter as ctk
from src.models.empleado import Empleado
from src.db.conexion import ConexionDB


class EmpleadoFrame(ctk.CTkFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self, text="Registro de Empleado", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        for i in range(10):
            self.grid_rowconfigure(i, weight=2)

        self.usuario_label = ctk.CTkLabel(self, text="Usuario:")
        self.usuario_entry = ctk.CTkEntry(self)

        self.contrasena_label = ctk.CTkLabel(self, text="Contraseña:")
        self.contrasena_entry = ctk.CTkEntry(self, show="*")

        self.dni_label = ctk.CTkLabel(self, text="DNI:")
        self.dni_entry = ctk.CTkEntry(self)

        self.submit_button = ctk.CTkButton(
            self, text="Submit", command=self.submit)

        self.usuario_label.grid(row=1, column=0)
        self.usuario_entry.grid(row=1, column=1)
        self.contrasena_label.grid(row=2, column=0)
        self.contrasena_entry.grid(row=2, column=1)
        self.dni_label.grid(row=3, column=0)
        self.dni_entry.grid(row=3, column=1)
        self.submit_button.grid(row=4, column=0, columnspan=2, sticky="ew")

    def submit(self):
        usuario = self.usuario_entry.get()
        contrasena = self.contrasena_entry.get()
        dni = self.dni_entry.get()

        conn = ConexionDB()
        conn.insert_empleado(Empleado(
            usuario=usuario, contrasena=contrasena, dni=dni))
    
