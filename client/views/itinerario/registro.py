import os
import customtkinter as ctk
import oracledb

class RegistrarVueloFrame(ctk.CTk):
    def __init__(self, main_frame):
        super().__init__()

        self.title("Registrar vuelo")
        self.geometry("400x300")
        self.grid_anchor("center")

        self.label_descripcion = ctk.CTkLabel(self, text="Descripción")
        self.label_descripcion.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.label_duracion = ctk.CTkLabel(self, text="Duración")
        self.label_duracion.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.label_pais_origen = ctk.CTkLabel(self, text="País de origen")
        self.label_pais_origen.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.label_ciudad_origen = ctk.CTkLabel(self, text="Ciudad de origen")
        self.label_ciudad_origen.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.label_pais_destino = ctk.CTkLabel(self, text="País de destino")
        self.label_pais_destino.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.label_ciudad_destino = ctk.CTkLabel(self, text="Ciudad de destino")
        self.label_ciudad_destino.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        self.entry_descripcion = ctk.CTkEntry(self)
        self.entry_descripcion.grid(row=0, column=1, padx=10, pady=5)

        self.entry_duracion = ctk.CTkEntry(self)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=5)

        self.entry_pais_origen = ctk.CTkEntry(self)
        self.entry_pais_origen.grid(row=2, column=1, padx=10, pady=5)

        self.entry_ciudad_origen = ctk.CTkEntry(self)
        self.entry_ciudad_origen.grid(row=3, column=1, padx=10, pady=5)

        self.entry_pais_destino = ctk.CTkEntry(self)
        self.entry_pais_destino.grid(row=4, column=1, padx=10, pady=5)

        self.entry_ciudad_destino = ctk.CTkEntry(self)
        self.entry_ciudad_destino.grid(row=5, column=1, padx=10, pady=5)

        self.button_registrar = ctk.CTkButton(self, text="Registrar vuelo", command=self.registrar_vuelo)
        self.button_registrar.grid(row=6, column=1, pady=10)

        self.button_retroceder = ctk.CTkButton(self, text="Retroceder", command=self.volver)
        self.button_retroceder.grid(row=6, column=0, pady=10)

        self.main_frame = main_frame

    def registrar_vuelo(self):
        try:
            os.environ["TNS_ADMIN"] = "ruta/al/directorio"  
            cnx = oracledb.connect(
                user="C##MICKAELL_MORAN",
                password="C##MICKAELL_MORAN",
                dsn="localhost:1521/xe"
            )
            cursor = cnx.cursor()

   
            descripcion = self.entry_descripcion.get()
            duracion = self.entry_duracion.get()
            pais_origen = self.entry_pais_origen.get()
            ciudad_origen = self.entry_ciudad_origen.get()
            pais_destino = self.entry_pais_destino.get()
            ciudad_destino = self.entry_ciudad_destino.get()

            cursor.execute("INSERT INTO ITINERARIO (DESCRIPCION, DURACION, PAISORIGEN, CIUDADORIGEN, PAISDESTINO, CIUDADDESTINO) "
                           "VALUES (:descripcion, :duracion, :pais_origen, :ciudad_origen, :pais_destino, :ciudad_destino)",
                           descripcion=descripcion, duracion=duracion, pais_origen=pais_origen,
                           ciudad_origen=ciudad_origen, pais_destino=pais_destino, ciudad_destino=ciudad_destino)

            cnx.commit()
            cursor.close()
            cnx.close()

            self.entry_descripcion.delete(0, ctk.END)
            self.entry_duracion.delete(0, ctk.END)
            self.entry_pais_origen.delete(0, ctk.END)
            self.entry_ciudad_origen.delete(0, ctk.END)
            self.entry_pais_destino.delete(0, ctk.END)
            self.entry_ciudad_destino.delete(0, ctk.END)

            print("Vuelo registrado exitosamente!")

        except oracledb.Error as e:
            print(f"Error al registrar vuelo: {e}")

    def volver(self):
        self.main_frame.deiconify()
        self.destroy()

if __name__ == "__main__":
    app = RegistrarVueloFrame()
    app.mainloop()
