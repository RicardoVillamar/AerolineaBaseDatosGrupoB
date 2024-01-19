
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class InterfazTabla ():
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.eliminarButton()
        # Título


    def eliminarButton(self):
        self.eliminar_button = ctk.CTkButton(
        self, text="Eliminar", command=self.eliminar)
        self.eliminar_button.grid(row=5, column=0, sticky="ew")
    def eliminar():
        pass 


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTabla(root)
    root.mainloop()