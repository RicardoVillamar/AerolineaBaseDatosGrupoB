import customtkinter as ctk


class EditFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(0, weight=1)

        # title

        self.title = ctk.CTkLabel(
            self, text="Editar Cliente", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, sticky="ew")

        for i in range(17):
            self.grid_rowconfigure(i, weight=2)

        self.labelNombre = ctk.CTkLabel(self, text="nombre")
        self.labelNombre.grid(row=1, column=0, sticky="ew")

        self.entryNombre = ctk.CTkEntry(self)
        self.entryNombre.grid(row=1, column=1)

        self.labelApellido = ctk.CTkLabel(self, text="apellido")
        self.labelApellido.grid(row=2, column=0)

        self.entryApellido = ctk.CTkEntry(self)
        self.entryApellido.grid(row=2, column=1)

        self.labelCedula = ctk.CTkLabel(self, text="cedula")
        self.labelCedula.grid(row=3, column=0)

        self.entryCedula = ctk.CTkEntry(self)
        self.entryCedula.grid(row=3, column=1)

        self.labelGenero = ctk.CTkLabel(self, text="genero")
        self.labelGenero.grid(row=4, column=0)

        self.entryGenero = ctk.CTkEntry(self)
        self.entryGenero.grid(row=4, column=1)

        self.labelNacionalidad = ctk.CTkLabel(
            self, text="nacionalidad")
        self.labelNacionalidad.grid(row=5, column=0)

        self.entryNacionalidad = ctk.CTkEntry(self)
        self.entryNacionalidad.grid(row=5, column=1)

        self.labelFecha_nacimiento = ctk.CTkLabel(
            self, text="fecha_nacimiento")
        self.labelFecha_nacimiento.grid(row=6, column=0)

        self.entryFecha_nacimiento = ctk.CTkEntry(self)
        self.entryFecha_nacimiento.grid(row=6, column=1)

        self.labelEmail = ctk.CTkLabel(self, text="email ")
        self.labelEmail.grid(row=7, column=0)

        self.entryEmail = ctk.CTkEntry(self)
        self.entryEmail.grid(row=7, column=1)

        self.labelEstadoCivil = ctk.CTkLabel(
            self, text="Estado Civil ")

        self.labelEstadoCivil.grid(row=8, column=0)

        self.entryEstadoCivil = ctk.CTkEntry(self)
        self.entryEstadoCivil.grid(row=8, column=1)

        self.labelDireccion = ctk.CTkLabel(self, text="Direccion ")
        self.labelDireccion.grid(row=9, column=0)

        self.entryDireccion = ctk.CTkEntry(self)
        self.entryDireccion.grid(row=9, column=1)

        self.labelNombreEmpresa = ctk.CTkLabel(
            self, text="Nombre Empresa ")
        self.labelNombreEmpresa.grid(row=10, column=0)

        self.entryNombreEmpresa = ctk.CTkEntry(self)
        self.entryNombreEmpresa.grid(row=10, column=1)

        self.labelCargo = ctk.CTkLabel(
            self, text="Nombre Empresa ")
        self.labelCargo.grid(row=11, column=0)

        self.entryCargo = ctk.CTkEntry(self)
        self.entryCargo.grid(row=11, column=1)

        # direccion empresa

        self.labelDireccionEmpresa = ctk.CTkLabel(
            self, text="Direccion Empresa ")
        self.labelDireccionEmpresa.grid(row=12, column=0)

        self.entryDireccionEmpresa = ctk.CTkEntry(self)
        self.entryDireccionEmpresa.grid(row=12, column=1)

        # Documentos

        self.labelDocumento = ctk.CTkLabel(
            self, text="Documento de Identidad")

        self.labelDocumento.grid(row=13, column=0)

        self.entryDocumento = ctk.CTkButton(
            self, text="Cargar Documento", command=self.load_file)

        self.entryDocumento.grid(row=13, column=1)

        # pasaporte

        self.labelPasaporte = ctk.CTkLabel(
            self, text="Pasaporte")

        self.labelPasaporte.grid(row=14, column=0)

        self.entryPasaporte = ctk.CTkButton(
            self, text="Cargar Pasaporte", command=self.load_file)

        self.entryPasaporte.grid(row=14, column=1)

        # visa

        self.labelVisa = ctk.CTkLabel(
            self, text="Visa")

        self.labelVisa.grid(row=15, column=0)

        self.entryVisa = ctk.CTkButton(
            self, text="Cargar Visa", command=self.load_file)

        self.entryVisa.grid(row=15, column=1)

        # orden de trabajo

        self.labelOrdenTrabajo = ctk.CTkLabel(
            self, text="Orden de Trabajo")

        self.labelOrdenTrabajo.grid(row=16, column=0)

        self.entryOrdenTrabajo = ctk.CTkButton(
            self, text="Cargar Orden de Trabajo",
            command=self.load_file)

        self.entryOrdenTrabajo.grid(row=16, column=1)

        # enviar

        self.enviar = ctk.CTkButton(
            self, text="Enviar", command=self.send_data, width=20, height=2, )

        self.enviar.grid(row=17, column=0, columnspan=2,
                         sticky="ew")

        #

    def send_data(self):
        pass

    def load_file(self):
        filename = None
        while not filename:
            filename = ctk.filedialog.askopenfilename()

        with open(filename, 'rb') as file:
            binary_content = file.read()

        return binary_content
