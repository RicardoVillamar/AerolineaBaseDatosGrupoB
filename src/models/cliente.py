
import random


class Cliente:

    def __init__(self, nombre, apellido, cedula, genero, nacionalidad, fecha_nacimiento, email, estadoCivil, proposito, direccion, nombreEmpresa, cargo, direccionEmpresa, documentoDocumentoIdentidad, documentoPasaporte, documentoVisa, documentoOrden):
        self._idCliente = self.generar_id()
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._genero = genero
        self._nacionalidad = nacionalidad
        self._fecha_nacimiento = fecha_nacimiento
        self._email = email
        self._estadoCivil = estadoCivil
        self._proposito = proposito
        self._direccion = direccion
        self._nombreEmpresa = nombreEmpresa
        self._cargo = cargo
        self._direccionEmpresa = direccionEmpresa
        self._documentoDocumentoIdentidad = documentoDocumentoIdentidad
        self._documentoPasaporte = documentoPasaporte
        self._documentoVisa = documentoVisa
        self._documentoOrden = documentoOrden

    def __str__(self):
        return f"{self._idCliente} {self._nombre} {self._apellido} {self._cedula} {self._genero} {self._nacionalidad} {self._fecha_nacimiento} {self._email} {self._estadoCivil} {self._proposito} {self._direccion} {self._notificacion} {self._nombreEmpresa} {self._cargo} {self._direccionEmpresa} {self._documentoDocumentoIdentidad} {self._documentoPasaporte} {self._documentoVisa} {self._documentoOrden}"

    @property
    def idCliente(self):
        return self._idCliente

    @idCliente.setter
    def idCliente(self, id_cliente):
        self._idCliente = id_cliente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def estadoCivil(self):
        return self._estadoCivil

    @estadoCivil.setter
    def estadoCivil(self, estadoCivil):
        self._estadoCivil = estadoCivil

    @property
    def proposito(self):
        return self._proposito

    @proposito.setter
    def proposito(self, proposito):
        self._proposito = proposito

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def notificacion(self):
        return self._notificacion

    @notificacion.setter
    def notificacion(self, notificacion):
        self._notificacion = notificacion

    @property
    def nombreEmpresa(self):
        return self._nombreEmpresa

    @nombreEmpresa.setter
    def nombreEmpresa(self, nombreEmpresa):
        self._nombreEmpresa = nombreEmpresa

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def direccionEmpresa(self):
        return self._direccionEmpresa

    @direccionEmpresa.setter
    def direccionEmpresa(self, direccionEmpresa):
        self._direccionEmpresa = direccionEmpresa

    @property
    def documentoDocumentoIdentidad(self):
        return self._documentoDocumentoIdentidad

    @documentoDocumentoIdentidad.setter
    def documentoDocumentoIdentidad(self, documentoDocumentoIdentidad):
        self._documentoDocumentoIdentidad = documentoDocumentoIdentidad

    @property
    def documentoPasaporte(self):
        return self._documentoPasaporte

    @documentoPasaporte.setter
    def documentoPasaporte(self, documentoPasaporte):
        self._documentoPasaporte = documentoPasaporte

    @property
    def documentoVisa(self):
        return self._documentoVisa

    @documentoVisa.setter
    def documentoVisa(self, documentoVisa):
        self._documentoVisa = documentoVisa

    @property
    def documentoOrden(self):
        return self._documentoOrden

    @documentoOrden.setter
    def documentoOrden(self, documentoOrden):
        self._documentoOrden = documentoOrden

    def generar_id(self):
        return random.randint(1, 1000000000)

    # Meodos
    def insertar_cliente(self):
        return (self._idCliente, self._nombre, self._apellido, self._cedula, self._genero, self._nacionalidad, self._fecha_nacimiento, self._email, self._estadoCivil, self._proposito, self._direccion, self._nombreEmpresa, self._cargo, self._direccionEmpresa, self._documentoDocumentoIdentidad, self._documentoPasaporte, self._documentoVisa, self._documentoOrden)
