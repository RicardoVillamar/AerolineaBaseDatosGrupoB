
import random


class Empleado:
    def __init__(self, usuario=None, contrasena=None, dni=None):
        self._id = self.generar_id()
        self._usuario = usuario
        self._contrasena = contrasena
        self._dni = dni

    def __str__(self):
        return f'Empleado(id={self.id}, usuario={self.usuario}, contrasena={self.contrasena}, dni={self.dni})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    def insertar_empleado(self):
        return (self._id, self._usuario, self._contrasena, self._dni)
