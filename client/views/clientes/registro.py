import customtkinter as ctk
from src.db.conexion import ConexionDB
from src.models.cliente import Cliente


class RegistroFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_anchor("center")
        self.grid_rowconfigure(0, weight=1)

        # title

        self.title = ctk.CTkLabel(
            self, text="Registro de Cliente", font=("Arial", 20))
        self.title.grid(row=0, column=1, columnspan=3, sticky="ew")

        for i in range(19):
            self.grid_rowconfigure(i, weight=2)

        self.labelNombre = ctk.CTkLabel(self, text="nombre")
        self.labelNombre.grid(row=1, column=0, sticky="ew")

        self.entryNombre = ctk.CTkEntry(self)
        self.entryNombre.grid(row=1, column=1)

        self.labelApellido = ctk.CTkLabel(self, text="apellido")
        self.labelApellido.grid(row=1, column=3)

        self.entryApellido = ctk.CTkEntry(self)
        self.entryApellido.grid(row=1, column=4)

        self.labelCedula = ctk.CTkLabel(self, text="cedula")
        self.labelCedula.grid(row=2, column=0)

        self.entryCedula = ctk.CTkEntry(self)
        self.entryCedula.grid(row=2, column=1)

        self.labelGenero = ctk.CTkLabel(self, text="genero")
        self.labelGenero.grid(row=2, column=3)

        self.entryGenero = ctk.CTkEntry(self)
        self.entryGenero.grid(row=2, column=4)

        self.labelNacionalidad = ctk.CTkLabel(
            self, text="nacionalidad")
        self.labelNacionalidad.grid(row=3, column=0)

        self.entryNacionalidad = ctk.CTkEntry(self)
        self.entryNacionalidad.grid(row=3, column=1)

        self.labelFecha_nacimiento = ctk.CTkLabel(
            self, text="fecha_nacimiento")
        self.labelFecha_nacimiento.grid(row=3, column=3)

        self.entryFecha_nacimiento = ctk.CTkEntry(self)
        self.entryFecha_nacimiento.grid(row=3, column=4)

        self.labelEmail = ctk.CTkLabel(self, text="email ")
        self.labelEmail.grid(row=4, column=0)

        self.entryEmail = ctk.CTkEntry(self)
        self.entryEmail.grid(row=4, column=1)

        self.labelEstadoCivil = ctk.CTkLabel(
            self, text="Estado Civil ")

        self.labelEstadoCivil.grid(row=4, column=3)

        self.entryEstadoCivil = ctk.CTkEntry(self)
        self.entryEstadoCivil.grid(row=4, column=4)

        self.labelProposito = ctk.CTkLabel(
            self, text="Proposito ")
        self.labelProposito.grid(row=5, column=0)

        self.entryProposito = ctk.CTkEntry(self)
        self.entryProposito.grid(row=5, column=1)

        self.labelDireccion = ctk.CTkLabel(self, text="Direccion ")
        self.labelDireccion.grid(row=5, column=3)

        self.entryDireccion = ctk.CTkEntry(self)
        self.entryDireccion.grid(row=5, column=4)

        self.labelNombreEmpresa = ctk.CTkLabel(
            self, text="Nombre Empresa ")
        self.labelNombreEmpresa.grid(row=6, column=0)

        self.entryNombreEmpresa = ctk.CTkEntry(self)
        self.entryNombreEmpresa.grid(row=6, column=1)

        self.labelCargo = ctk.CTkLabel(
            self, text="Nombre Empresa ")
        self.labelCargo.grid(row=6, column=3)

        self.entryCargo = ctk.CTkEntry(self)
        self.entryCargo.grid(row=6, column=4)

        # direccion empresa

        self.labelDireccionEmpresa = ctk.CTkLabel(
            self, text="Direccion Empresa ")
        self.labelDireccionEmpresa.grid(row=7, column=0)

        self.entryDireccionEmpresa = ctk.CTkEntry(self)
        self.entryDireccionEmpresa.grid(row=7, column=1)

        # Documentos

        self.labelDocumento = ctk.CTkLabel(
            self, text="Documento de Identidad")

        self.labelDocumento.grid(row=8, column=0)

        self.entryDocumento = ctk.CTkButton(
            self, text="Cargar Documento", command=self.load_documento)

        self.entryDocumento.grid(row=8, column=1)

        # pasaporte

        self.labelPasaporte = ctk.CTkLabel(
            self, text="Pasaporte")

        self.labelPasaporte.grid(row=9, column=0)

        self.entryPasaporte = ctk.CTkButton(
            self, text="Cargar Pasaporte", command=self.load_pasaporte)

        self.entryPasaporte.grid(row=9, column=1)

        # visa

        self.labelVisa = ctk.CTkLabel(
            self, text="Visa")

        self.labelVisa.grid(row=9, column=3)

        self.entryVisa = ctk.CTkButton(
            self, text="Cargar Visa", command=self.load_visa)

        self.entryVisa.grid(row=9, column=4)

        # orden de trabajo

        self.labelOrdenTrabajo = ctk.CTkLabel(
            self, text="Orden de Trabajo")

        self.labelOrdenTrabajo.grid(row=8, column=3)

        self.entryOrdenTrabajo = ctk.CTkButton(
            self, text="Cargar Orden de Trabajo", command=self.load_orden_trabajo)

        self.entryOrdenTrabajo.grid(row=8, column=4)

        # enviar

        self.enviar = ctk.CTkButton(
            self, text="Enviar", command=self.send_data, width=20, height=10, )

        self.enviar.grid(row=14, column=1, columnspan=3,
                         sticky="ew")

        #

    def send_data(self):
        nombre = self.entryNombre.get()
        apellido = self.entryApellido.get()
        cedula = self.entryCedula.get()
        genero = self.entryGenero.get()
        nacionalidad = self.entryNacionalidad.get()
        fecha_nacimiento = self.entryFecha_nacimiento.get()
        email = self.entryEmail.get()
        estadoCivil = self.entryEstadoCivil.get()
        proposito = self.entryProposito.get()
        direccion = self.entryDireccion.get()
        nombreEmpresa = self.entryNombreEmpresa.get()
        cargo = self.entryCargo.get()
        direccionEmpresa = self.entryDireccionEmpresa.get()
        documento = self.documento_binario
        pasaporte = self.pasaporte_binario
        visa = self.visa_binario
        ordenTrabajo = self.orden_trabajo_binario

        # insert into database

        conn = ConexionDB()
        conn.insert_cliente(Cliente(

            nombre=nombre, apellido=apellido, cedula=cedula, genero=genero, nacionalidad=nacionalidad, fecha_nacimiento=fecha_nacimiento, email=email, estadoCivil=estadoCivil, proposito=proposito, direccion=direccion, nombreEmpresa=nombreEmpresa, cargo=cargo, direccionEmpresa=direccionEmpresa, documentoDocumentoIdentidad=documento, documentoPasaporte=pasaporte, documentoVisa=visa, documentoOrden=ordenTrabajo
        ))

    def load_file(self):
        filename = None
        while not filename:
            filename = ctk.filedialog.askopenfilename()

        with open(filename, 'rb') as file:
            self.binary_content = file.read()

        return self.binary_content

    def load_documento(self):
        self.documento_binario = self.load_file()

    def load_pasaporte(self):
        self.pasaporte_binario = self.load_file()

    def load_visa(self):
        self.visa_binario = self.load_file()

    def load_orden_trabajo(self):
        self.orden_trabajo_binario = self.load_file()
