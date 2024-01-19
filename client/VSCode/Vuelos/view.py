import os
import customtkinter as ctk
from tkinter import ttk
from registrar_vuelo import RegistrarVueloFrame
from modificar_vuelo import ModificarVueloFrame
import oracledb

class VueloFrame(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Buscar vuelo")
        self.geometry("900x600")

        self.label_origen = ctk.CTkLabel(self, text="Origen")
        self.label_origen.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.label_destino = ctk.CTkLabel(self, text="Destino")
        self.label_destino.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.combo_origen = ctk.CTkComboBox(self, values=self.get_ciudades())
        self.combo_origen.grid(row=0, column=1, padx=10, pady=5)

        self.combo_destino = ctk.CTkComboBox(self, values=self.get_ciudades())
        self.combo_destino.grid(row=1, column=1, padx=10, pady=5)

        self.label_criterio_busqueda = ctk.CTkLabel(self, text="Criterio de búsqueda")
        self.label_criterio_busqueda.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        self.combo_criterio_busqueda = ctk.CTkComboBox(self, values=["ID", "DESCRIPCION", "DURACION", "PAISORIGEN", "CIUDADORIGEN", "PAISDESTINO", "CIUDADDESTINO"])
        self.combo_criterio_busqueda.grid(row=2, column=1, padx=10, pady=5)

        self.entry_busqueda = ctk.CTkEntry(self)
        self.entry_busqueda.grid(row=3, column=1, padx=10, pady=5)

        self.button_buscar = ctk.CTkButton(self, text="Buscar vuelos", command=self.buscar_vuelos)
        self.button_buscar.grid(row=4, column=1, pady=10)

        self.button_cargar_tabla = ctk.CTkButton(self, text="Cargar tabla", command=self.cargar_tabla)
        self.button_cargar_tabla.grid(row=4, column=0, pady=10)

        self.button_registrar_vuelo = ctk.CTkButton(self, text="Registrar vuelo", command=self.abrir_registrar_vuelo)
        self.button_registrar_vuelo.grid(row=5, column=0, pady=10)

        self.button_modificar_vuelo = ctk.CTkButton(self, text="Modificar vuelo", command=self.abrir_modificar_vuelo)
        self.button_modificar_vuelo.grid(row=5, column=1, pady=10)

        self.tree = ttk.Treeview(self, columns=["ID", "DESCRIPCION", "DURACION", "PAISORIGEN", "CIUDADORIGEN", "PAISDESTINO", "CIUDADDESTINO"])
        self.tree.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        for col in ["ID", "DESCRIPCION", "DURACION", "PAISORIGEN", "CIUDADORIGEN", "PAISDESTINO", "CIUDADDESTINO"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

    def get_ciudades(self):
        try:
            os.environ["TNS_ADMIN"] = "ruta/al/directorio"  # Reemplaza con la ruta real
            cnx = oracledb.connect(
                user="C##MICKAELL_MORAN",
                password="C##MICKAELL_MORAN",
                dsn="localhost:1521/xe"
            )
            cursor = cnx.cursor()
            cursor.execute("SELECT DISTINCT CIUDADDESTINO FROM ITINERARIO")
            ciudades = [row[0] for row in cursor.fetchall()]
            cursor.close()
            cnx.close()
            return ["Seleccionar"] + ciudades
        except oracledb.Error as e:
            print(f"Error en la conexión a la base de datos: {e}")
            return ["Seleccionar"]

    def buscar_vuelos(self):
        # Obtener criterio de búsqueda y valor opcional
        selected_criterio = self.combo_criterio_busqueda.get()
        optional_value = self.entry_busqueda.get()

        # Limpiar datos actuales en la tabla
        self.tree.delete(*self.tree.get_children())

        try:
            os.environ["TNS_ADMIN"] = "ruta/al/directorio"  # Reemplaza con la ruta real
            cnx = oracledb.connect(
                user="C##MICKAELL_MORAN",
                password="C##MICKAELL_MORAN",
                dsn="localhost:1521/xe"
            )
            cursor = cnx.cursor()
            query = f"SELECT * FROM ITINERARIO WHERE {selected_criterio} = :value"
            cursor.execute(query, value=optional_value)
            rows = cursor.fetchall()

            for row in rows:
                self.tree.insert("", "end", values=row)

            cursor.close()
            cnx.close()

        except oracledb.Error as e:
            print(f"Error en la conexión a la base de datos: {e}")

    def cargar_tabla(self):
        # Limpiar datos actuales en la tabla
        self.tree.delete(*self.tree.get_children())

        try:
            os.environ["TNS_ADMIN"] = "ruta/al/directorio"  # Reemplaza con la ruta real
            cnx = oracledb.connect(
                user="C##MICKAELL_MORAN",
                password="C##MICKAELL_MORAN",
                dsn="localhost:1521/xe"
            )
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM ITINERARIO")
            rows = cursor.fetchall()

            for row in rows:
                self.tree.insert("", "end", values=row)

            cursor.close()
            cnx.close()

        except oracledb.Error as e:
            print(f"Error en la conexión a la base de datos: {e}")

    def abrir_registrar_vuelo(self):
        registrar_vuelo_frame = RegistrarVueloFrame(self)
        self.iconify()  # Ocultar la ventana principal
        registrar_vuelo_frame.mainloop()

    def abrir_modificar_vuelo(self):
        modificar_vuelo_frame = ModificarVueloFrame(self)
        self.iconify()  # Ocultar la ventana principal
        modificar_vuelo_frame.mainloop()

if __name__ == "__main__":
    app = VueloFrame()
    app.mainloop()
