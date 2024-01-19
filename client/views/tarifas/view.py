import customtkinter as ctk
from tkinter import ttk
from src.db.conexion import ConexionDB


class TarifaAerolineaFrame(ctk.CTkFrame):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(1, weight=1)

        self.title = ctk.CTkLabel(
            self, text="Busquedas de Tarifa", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        
        for i in range(6):
            
             self.grid_rowconfigure(i, weight=2)
        
        self.eliminarButton = ctk.CTkButton(
        self, text="eliminar", command=self.eliminar_tarifa)

        self.buscar_button = ctk.CTkButton(
        self, text="Buscar", command=self.mostrar)

        self.box_buscar = ctk.CTkEntry(self)




        # Crear tabla
        
        self.tabla = ttk.Treeview(self, columns=('ID', 'Nombre', 'Monto', 'Restricciones'))
         # Configurar columnas
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Monto')
        self.tabla.heading('#3', text='Restricciones')

        self.box_buscar.grid(row=1, column=0,sticky="e")
        self.buscar_button.grid(row=1, column=1,sticky="w")
        self.eliminarButton.grid(row=3, column=1,sticky="w")
        self.tabla.grid(row=2, column=0,columnspan=2,sticky="nsew")




        self.eliminar_button = ctk.CTkButton(
            self, text="Eliminar", command=self.eliminar_tarifa)
        self.eliminar_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Asociar la función de selección a la tabla
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_tarifa)

    def mostrar(self):
        obtener_tarifa = ConexionDB()

        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        try:
            dato_busqueda = self.box_buscar.get()
            tarifas = obtener_tarifa.obtener_tarifa(condicion_clase=dato_busqueda)

            for tarifa in tarifas:
                self.tabla.insert('', 'end', values=(
                    tarifa[0], tarifa[1], tarifa[2], tarifa[3]))
        except Exception as e:
            print(f"Error al buscar vuelos: {e}")

    
    def seleccionar_tarifa(self, event):
        selected_item = self.tabla.selection()
        if selected_item:
            # Obtener los valores de la fila seleccionada
            values = self.tabla.item(selected_item, 'values')
            # Hacer lo que necesites con los valores (puede mostrarlos en un messagebox)

    def eliminar_tarifa(self):
        selected_item = self.tabla.selection()
        if selected_item:
            # Obtener el ID de la fila seleccionada
            tarifa_id = self.tabla.item(selected_item, 'values')[0]

            # Llamar a la función de eliminación en la base de datos
            # Asegúrate de tener una instancia de ConexionDB
            conexion_db = ConexionDB()
            conexion_db.delete_tarifa(tarifa_id)

            # Eliminar la fila seleccionada de la tabla
            self.tabla.delete(selected_item)
        else:
            print("Selecciona una tarifa antes de intentar eliminar.")

if __name__ == "__main__":
    # Ejemplo de uso
    root = ctk.CTkRoot()
    app = TarifaAerolineaFrame(root)
    root.mainloop()

