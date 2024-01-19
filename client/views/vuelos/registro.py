import customtkinter as ctk
from src.models.vuelo import Vuelo
from src.db.conexion import ConexionDB

# -- Tabla vuelo
# CREATE TABLE vuelo (
#   id NUMBER PRIMARY KEY,
#   numerovuelo VARCHAR2(50),
#   fechasalida DATE,
#   horasalida TIMESTAMP,
#   origen VARCHAR2(50),
#   destino VARCHAR2(50),
#   duracion INT,
#   escalas INT,
#   clase VARCHAR2(50),
#   precio DECIMAL(10, 2)
# );


class VueloFrame(ctk.CTkFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(0, weight=1)

        self.title = ctk.CTkLabel(
            self, text="Registro de Vuelos", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        for i in range(12):
            self.grid_rowconfigure(i, weight=2)

         # Campos de la tabla
        self.numerovuelo_label = ctk.CTkLabel(self, text="Numero de Vuelo")
        self.numerovuelo_entry = ctk.CTkEntry(self)

        self.fechasalida_label = ctk.CTkLabel(self, text="Fecha de Salida")
        self.fechasalida_entry = ctk.CTkEntry(self)

        self.horasalida_label = ctk.CTkLabel(self, text="Hora de Salida")
        self.horasalida_entry = ctk.CTkEntry(self)

        self.origen_label = ctk.CTkLabel(self, text="Origen")
        self.origen_entry = ctk.CTkEntry(self)

        self.destino_label = ctk.CTkLabel(self, text="Destino")
        self.destino_entry = ctk.CTkEntry(self)

        self.duracion_label = ctk.CTkLabel(self, text="Duracion")
        self.duracion_entry = ctk.CTkEntry(self)

        self.escalas_label = ctk.CTkLabel(self, text="Escalas")
        self.escalas_entry = ctk.CTkEntry(self)

        self.clase_label = ctk.CTkLabel(self, text="Clase")
        self.clase_entry = ctk.CTkEntry(self)

        self.precio_label = ctk.CTkLabel(self, text="Precio")
        self.precio_entry = ctk.CTkEntry(self)

        # Colocar los campos en la grilla
        self.numerovuelo_label.grid(row=1, column=0)
        self.numerovuelo_entry.grid(row=1, column=1)

        self.fechasalida_label.grid(row=2, column=0)
        self.fechasalida_entry.grid(row=2, column=1)

        self.horasalida_label.grid(row=3, column=0)
        self.horasalida_entry.grid(row=3, column=1)

        self.origen_label.grid(row=4, column=0)
        self.origen_entry.grid(row=4, column=1)

        self.destino_label.grid(row=5, column=0)
        self.destino_entry.grid(row=5, column=1)

        self.duracion_label.grid(row=6, column=0)
        self.duracion_entry.grid(row=6, column=1)

        self.escalas_label.grid(row=7, column=0)
        self.escalas_entry.grid(row=7, column=1)

        self.clase_label.grid(row=8, column=0)
        self.clase_entry.grid(row=8, column=1)

        self.precio_label.grid(row=9, column=0)
        self.precio_entry.grid(row=9, column=1)

        self.submit_button = ctk.CTkButton(
            self, text="Submit", command=self.submit)

        self.submit_button.grid(row=10, column=0, columnspan=2, sticky="ew")

    def submit(self):
       
        numerovuelo = self.numerovuelo_entry.get()
        fechasalida = self.fechasalida_entry.get()
        horasalida = self.horasalida_entry.get()
        origen = self.origen_entry.get()
        destino = self.destino_entry.get()
        duracion = self.duracion_entry.get()
        escalas = self.escalas_entry.get()
        clase = self.clase_entry.get()
        precio = self.precio_entry.get()
      

        conn = ConexionDB()
        conn.insertar_vuelo(Vuelo(
            numerovuelo=numerovuelo, fechasalida=fechasalida, horasalida=horasalida, origen=origen, destino=destino, duracion=duracion, escalas=escalas, clase=clase, precio=precio
        ))
    
        self.numerovuelo_entry.delete(0, ctk.END)
        self.fechasalida_entry.delete(0, ctk.END)
        self.horasalida_entry.delete(0, ctk.END)
        self.origen_entry.delete(0, ctk.END)
        self.destino_entry.delete(0, ctk.END)
        self.duracion_entry.delete(0, ctk.END)
        self.escalas_entry.delete(0, ctk.END)
        self.clase_entry.delete(0, ctk.END)
        self.precio_entry.delete(0, ctk.END)