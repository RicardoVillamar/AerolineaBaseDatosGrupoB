import customtkinter as ctk
from src.models.tarifa import Tarifa
from src.db.conexion import ConexionDB


class TarifaFrame(ctk.CTkFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self, text="Registro de Tarifa de clientes", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        for i in range(12):
            self.grid_rowconfigure(i, weight=2)

        # Campos de la tabla

        self.nombre_label = ctk.CTkLabel(self, text="Nombre")
        self.nombre_entry = ctk.CTkEntry(self)

        self.monto_label = ctk.CTkLabel(self, text="Monto")

        self.monto_entry = ctk.CTkEntry(self)

        self.restricciones_label = ctk.CTkLabel(self, text="Restricciones")

        self.restricciones_entry = ctk.CTkEntry(self)



        # Botones

        self.registrar_button = ctk.CTkButton(
            self, text="Registrar", command=self.registrar)
        self.registrar_button.grid(row=5, column=0, sticky="ew")

        # Posicionamiento de los campos
        self.nombre_label.grid(row=1, column=0)
        self.nombre_entry.grid(row=1, column=1)

        self.monto_label.grid(row=2, column=0)
        self.monto_entry.grid(row=2, column=1)

        self.restricciones_label.grid(row=3, column=0)
        self.restricciones_entry.grid(row=3, column=1)

        # self.origen_label.grid(row=5, column=0)

    def registrar(self):
        try:
            nombre = self.nombre_entry.get()
            monto = self.monto_entry.get()
            restricciones = self.restricciones_entry.get()

            print(f"Nombre: {nombre}, Monto: {monto}, Restricciones: {restricciones}")

            conn = ConexionDB()
            conn.insertar_tarifa(Tarifa(
            nombre=nombre,
            monto=monto,
            restricciones=restricciones,
            ))
            print("Tarifa registrada exitosamente")
        except Exception as e:
            print(f"Error al registrar tarifa: {e}")

    
    
