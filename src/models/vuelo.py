# -- Tabla vuelo
# CREATE TABLE vuelo (
#   id NUMBER PRIMARY KEY,
#   numerovuelo VARCHAR2(50),
#   fechasalida DATE,
#   horasalida TIMESTAMP,
#   origen VARCHAR2(50),
#   destino VARCHAR2(50),
#   duracion INT,
#   escalas INT,
#   clase VARCHAR2(50),
#   precio DECIMAL(10, 2)
# );

import random
from datetime import datetime


class Vuelo:
    def __init__(self, numerovuelo=None, fechasalida=None, horasalida=None, origen=None, destino=None, duracion=None, escalas=None, clase=None, precio=None):
        self._id = self.generar_id()
        self._numerovuelo = numerovuelo
        self._fechasalida = fechasalida
        self._horasalida = horasalida
        self._origen = origen
        self._destino = destino
        self._duracion = duracion
        self._escalas = escalas
        self._clase = clase
        self._precio = precio

    def __str__(self):
        return f'Vuelo(id={self.id}, numerovuelo={self.numerovuelo}, fechasalida={self.fechasalida}, horasalida={self.horasalida}, origen={self.origen}, destino={self.destino}, duracion={self.duracion}, escalas={self.escalas}, clase={self.clase}, precio={self.precio})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def numerovuelo(self):
        return self._numerovuelo

    @numerovuelo.setter
    def numerovuelo(self, numerovuelo):
        self._numerovuelo = numerovuelo

    @property
    def fechasalida(self):
        return self._fechasalida

    @fechasalida.setter
    def fechasalida(self, fechasalida):
        self._fechasalida = fechasalida

    @property
    def horasalida(self):
        return self._horasalida

    @horasalida.setter
    def horasalida(self, horasalida):
        self._horasalida = horasalida

    @property
    def origen(self):
        return self._origen

    @origen.setter
    def origen(self, origen):
        self._origen = origen

    @property
    def destino(self):
        return self._destino

    @destino.setter
    def destino(self, destino):
        self._destino = destino

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def escalas(self):
        return self._escalas

    @escalas.setter
    def escalas(self, escalas):
        self._escalas = escalas

    @property
    def clase(self):
        return self._clase

    @clase.setter
    def clase(self, clase):
        self._clase = clase

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def insertar_vuelo(self):
        return (self._id, self._numerovuelo, self._fechasalida, self._horasalida, self._origen, self._destino, self._duracion, self._escalas, self._clase, self._precio)
