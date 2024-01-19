import os
import customtkinter as ctk
import oracledb

class ModificarVueloFrame(ctk.CTk):
    def __init__(self, main_frame):
        super().__init__()

        self.title("Modificar vuelo")
        self.geometry("400x300")

        self.label_id = ctk.CTkLabel(self, text="ID del vuelo a modificar")
        self.label_id.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.entry_id = ctk.CTkEntry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        self.label_descripcion = ctk.CTkLabel(self, text="Nueva descripción")
        self.label_descripcion.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.label_duracion = ctk.CTkLabel(self, text="Nueva duración")
        self.label_duracion.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.label_pais_origen = ctk.CTkLabel(self, text="Nuevo país de origen")
        self.label_pais_origen.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.label_ciudad_origen = ctk.CTkLabel(self, text="Nueva ciudad de origen")
        self.label_ciudad_origen.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.label_pais_destino = ctk.CTkLabel(self, text="Nuevo país de destino")
        self.label_pais_destino.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        self.label_ciudad_destino = ctk.CTkLabel(self, text="Nueva ciudad de destino")
        self.label_ciudad_destino.grid(row=6, column=0, padx=10, pady=5, sticky="e")

        self.entry_descripcion = ctk.CTkEntry(self)
        self.entry_descripcion.grid(row=1, column=1, padx=10, pady=5)

        self.entry_duracion = ctk.CTkEntry(self)
        self.entry_duracion.grid(row=2, column=1, padx=10, pady=5)

        self.entry_pais_origen = ctk.CTkEntry(self)
        self.entry_pais_origen.grid(row=3, column=1, padx=10, pady=5)

        self.entry_ciudad_origen = ctk.CTkEntry(self)
        self.entry_ciudad_origen.grid(row=4, column=1, padx=10, pady=5)

        self.entry_pais_destino = ctk.CTkEntry(self)
        self.entry_pais_destino.grid(row=5, column=1, padx=10, pady=5)

        self.entry_ciudad_destino = ctk.CTkEntry(self)
        self.entry_ciudad_destino.grid(row=6, column=1, padx=10, pady=5)

        self.button_modificar = ctk.CTkButton(self, text="Modificar vuelo", command=self.modificar_vuelo)
        self.button_modificar.grid(row=7, column=1, pady=10)

        self.button_retroceder = ctk.CTkButton(self, text="Retroceder", command=self.volver)
        self.button_retroceder.grid(row=7, column=0, pady=10)

        self.main_frame = main_frame

    def modificar_vuelo(self):
        try:
              # Reemplaza con la ruta real
            cnx = oracledb.connect(
                user="C##MICKAELL_MORAN",
                password="C##MICKAELL_MORAN",
                dsn="localhost:1521/xe"
            )
            cursor = cnx.cursor()

            # Obtener valores de los campos
            id_vuelo = self.entry_id.get()
            nueva_descripcion = self.entry_descripcion.get()
            nueva_duracion = self.entry_duracion.get()
            nuevo_pais_origen = self.entry_pais_origen.get()
            nueva_ciudad_origen = self.entry_ciudad_origen.get()
            nuevo_pais_destino = self.entry_pais_destino.get()
            nueva_ciudad_destino = self.entry_ciudad_destino.get()

            # Modificar registro en la base de datos
            cursor.execute("UPDATE ITINERARIO SET DESCRIPCION=:nueva_descripcion, DURACION=:nueva_duracion, "
                           "PAISORIGEN=:nuevo_pais_origen, CIUDADORIGEN=:nueva_ciudad_origen, "
                           "PAISDESTINO=:nuevo_pais_destino, CIUDADDESTINO=:nueva_ciudad_destino "
                           "WHERE ID=:id_vuelo",
                           nueva_descripcion=nueva_descripcion, nueva_duracion=nueva_duracion,
                           nuevo_pais_origen=nuevo_pais_origen, nueva_ciudad_origen=nueva_ciudad_origen,
                           nuevo_pais_destino=nuevo_pais_destino, nueva_ciudad_destino=nueva_ciudad_destino,
                           id_vuelo=id_vuelo)

            cnx.commit()
            cursor.close()
            cnx.close()

            # Limpiar campos después de modificar
            self.entry_id.delete(0, ctk.END)
            self.entry_descripcion.delete(0, ctk.END)
            self.entry_duracion.delete(0, ctk.END)
            self.entry_pais_origen.delete(0, ctk.END)
            self.entry_ciudad_origen.delete(0, ctk.END)
            self.entry_pais_destino.delete(0, ctk.END)
            self.entry_ciudad_destino.delete(0, ctk.END)

            print("Vuelo modificado exitosamente!")

        except oracledb.Error as e:
            print(f"Error al modificar vuelo: {e}")

    def volver(self):
        self.main_frame.deiconify()
        self.destroy()

if __name__ == "__main__":
    app = ModificarVueloFrame()
    app.mainloop()
