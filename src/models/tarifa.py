
import random


class Tarifa:
    def __init__(self, nombre=None, monto=None, restricciones=None, vuelo_id=None):
        self._id = self.generar_id()
        self._nombre = nombre
        self._monto = monto
        self._restricciones = restricciones


    def __str__(self):
        return f'Tarifa(id={self.id}, nombre={self.nombre}, monto={self.monto}, restricciones={self.restricciones})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monto(self):
        return self._monto

    @monto.setter
    def monto(self, monto):
        self._monto = monto

    @property
    def restricciones(self):
        return self._restricciones

    @restricciones.setter
    def restricciones(self, restricciones):
        self._restricciones = restricciones


    def insertar_tarifa(self):
        return (self._id, self._nombre, self._monto, self._restricciones)
