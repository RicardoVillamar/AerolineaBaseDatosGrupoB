import customtkinter

# login frame


class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de usuario
        self.lbl_username = customtkinter.CTkLabel(self, text="Usuario:")
        self.lbl_username.pack()

        # Entrada de usuario
        self.entry_username = customtkinter.CTkEntry(self)
        self.entry_username.pack()

        # Etiqueta de contraseña
        self.lbl_password = customtkinter.CTkLabel(self, text="Contraseña:")
        self.lbl_password.pack()

        # Entrada de contraseña
        self.entry_password = customtkinter.CTkEntry(self, show="*")
        self.entry_password.pack()

        # Botón de inicio de sesión
        self.btn_login = customtkinter.CTkButton(
            self, text="Iniciar sesión", command=self.login)
        self.btn_login.pack()

    def login(self):

        pass
