import os
import customtkinter as ctk
from src.models.vuelo import Vuelo
from src.db.conexion import ConexionDB

class ModificarVueloFrame(ctk.CTk):
    def __init__(self, main_frame, id_vuelo, numero_vuelo, fecha_salida, origen, destino, duracion):
        super().__init__()

        self.title("Modificar vuelo")
        self.geometry("500x400")
        self.grid_anchor("center")


        self.label_numero_vuelo = ctk.CTkLabel(self, text="Nuevo número de vuelo")
        self.label_numero_vuelo.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.entry_numero_vuelo = ctk.CTkEntry(self)
        self.entry_numero_vuelo.grid(row=1, column=1, padx=10, pady=5)

        self.label_fecha_salida = ctk.CTkLabel(self, text="Nueva fecha de salida")
        self.label_fecha_salida.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.entry_fecha_salida = ctk.CTkEntry(self)
        self.entry_fecha_salida.grid(row=2, column=1, padx=10, pady=5)

        self.label_origen = ctk.CTkLabel(self, text="Nuevo origen")
        self.label_origen.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.entry_origen = ctk.CTkEntry(self)
        self.entry_origen.grid(row=3, column=1, padx=10, pady=5)

        self.label_destino = ctk.CTkLabel(self, text="Nuevo destino")
        self.label_destino.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.entry_destino = ctk.CTkEntry(self)
        self.entry_destino.grid(row=4, column=1, padx=10, pady=5)

        self.label_duracion = ctk.CTkLabel(self, text="Nueva duración")
        self.label_duracion.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        self.entry_duracion = ctk.CTkEntry(self)
        self.entry_duracion.grid(row=5, column=1, padx=10, pady=5)

        self.button_modificar = ctk.CTkButton(self, text="Modificar vuelo", command=self.modificar_vuelo)
        self.button_modificar.grid(row=9, column=1, pady=10)

        self.button_retroceder = ctk.CTkButton(self, text="Retroceder", command=self.volver)
        self.button_retroceder.grid(row=9, column=0, pady=10)

        self.entry_numero_vuelo.insert(0, numero_vuelo)
        self.entry_fecha_salida.insert(0, fecha_salida)
        self.entry_origen.insert(0, origen)
        self.entry_destino.insert(0, destino)
        self.entry_duracion.insert(0, duracion)

        self.main_frame = main_frame

        # Crear el objeto Vuelo
        self.vuelo = Vuelo(numero_vuelo, fecha_salida, origen, destino, duracion)

    def modificar_vuelo(self):
    # Obtener los nuevos datos de la entrada de texto
        numerovuelo = self.entry_numero_vuelo.get()
        fechasalida = self.entry_fecha_salida.get()
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()
        duracion = self.entry_duracion.get()

   
        if not numerovuelo or not fechasalida or not origen or not destino or not duracion:
            print("Por favor, complete todos los campos.")
            return

        
        flight_id = self.vuelo.id


        self.vuelo.numeroVuelo = numerovuelo
        self.vuelo.fechasalida = fechasalida
        self.vuelo.origen = origen
        self.vuelo.destino = destino
        self.vuelo.duracion = duracion

  
        conn = ConexionDB()
        success = conn.modificar_vuelo(self.vuelo)

        if success:
            print("¡Vuelo modificado exitosamente!")
        else:
            print("Error al modificar el vuelo. Verifique los datos e inténtelo nuevamente.")



    def volver(self):
        self.main_frame.deiconify()
        self.destroy()

if __name__ == "__main__":
    app = ModificarVueloFrame()
    app.mainloop()
