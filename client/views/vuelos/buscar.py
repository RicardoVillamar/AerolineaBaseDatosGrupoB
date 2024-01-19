import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from src.models.vuelo import Vuelo
from src.db.conexion import ConexionDB
from .edicion import ModificarVueloFrame
# from src.db.conexion import ConexionDB


class BuscarFrame(ctk.CTkFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(1, weight=1)

        self.title = ctk.CTkLabel(
            self, text="Busquedas de vuelo", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        
        for i in range(6):
            self.grid_rowconfigure(i, weight=2)

        self.buscar_button = ctk.CTkButton(
            self, text="buscar", command=self.submit)
        
        self.modificar_button = ctk.CTkButton(
            self, text="Modificar", command=self.abrir_modificar_vuelo)

        self.box_buscar = ctk.CTkEntry(self)

        # Crear tabla
        
        self.tabla = ttk.Treeview(self, columns=('ID', 'NumeroVuelo', 'Fecha', 'Origen', 'Destino' ,'Duracion'))
         # Configurar columnas
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NumeroVuelo')
        self.tabla.heading('#2', text='Fecha')
        self.tabla.heading('#3', text='Origen')
        self.tabla.heading('#4', text='Destino')
        self.tabla.heading('#5', text='Duracion')

        self.box_buscar.grid(row=1, column=0,sticky="e")
        self.buscar_button.grid(row=1, column=1,sticky="w")
        self.modificar_button.grid(row=2, column=1,sticky="w")
        self.tabla.grid(row=3, column=0,columnspan=2,sticky="nsew")
          
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_vuelo)
        
    #BUSCAR POR FECHA SALIDA
    def submit(self):
        
        obtener_vuelos = ConexionDB()

        # Limpia la tabla antes de agregar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        try:
            # Obtiene vuelos según el término de búsqueda (clase)
            dato_busqueda = self.box_buscar.get()
            vuelos = obtener_vuelos.obtener_vuelo(condicion_clase=dato_busqueda)

            # Agrega los resultados a la tabla
            for vuelo in vuelos:
                self.tabla.insert('', 'end', values=(
                    vuelo[0], vuelo[1], vuelo[2], vuelo[3], vuelo[4], vuelo[5]))

        except Exception as e:
         # Maneja las excepciones, por ejemplo, muestra un mensaje de error
            print(f"Error al buscar vuelos: {e}")
   
        

    def abrir_modificar_vuelo(self):
    # Obtener el ítem seleccionado en la tabla
        selected_item = self.tabla.selection()

        if selected_item:
            # Obtener los valores de la fila seleccionada
            values = self.tabla.item(selected_item, 'values')
            print("Datos seleccionados:", values)

            # Desempaquetar los valores y pasarlos como argumentos
            id_vuelo, numero_vuelo, fecha_salida, origen, destino, duracion = values
            modificar_vuelo_frame = ModificarVueloFrame(
                self, id_vuelo, numero_vuelo, fecha_salida, origen, destino, duracion)
            modificar_vuelo_frame.mainloop()


    def seleccionar_vuelo(self, event):
        # Puedes utilizar este método si prefieres obtener la selección al hacer clic
        selected_item = self.tabla.selection()
        if selected_item:
            # Obtener los valores de la fila seleccionada
            values = self.tabla.item(selected_item, 'values')
            print("Datos seleccionados:", values)




    #BUSCAR GENERAL // CARGAR TABLA

    # def submit(self):
    #     obtener_vuelos = ConexionDB()

    # # Limpia la tabla antes de agregar nuevos datos
    #     for item in self.tabla.get_children():
    #         self.tabla.delete(item)

    #     try:
    #         # Obtiene vuelos según el término de búsqueda (clase)
    #         clase_busqueda = self.box_buscar.get()
    #         vuelos = obtener_vuelos.obtener_vuelo(condicion_clase=clase_busqueda)

    #         # Agrega los resultados a la tabla
    #         for vuelo in vuelos:
    #             self.tabla.insert('', 'end', values=(
    #             vuelo, vuelo, vuelo, vuelo, vuelo, vuelo))

    #     except Exception as e:
    #     # Maneja las excepciones, por ejemplo, muestra un mensaje de error
    #         print(f"Error al buscar vuelos: {e}")
    