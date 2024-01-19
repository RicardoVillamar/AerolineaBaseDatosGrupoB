
# -- Tabla informe
# CREATE TABLE informe (
#   id NUMBER PRIMARY KEY,
#   fechainforme DATE,
#   contenido VARCHAR2(255),
#   tipoinforme VARCHAR2(50),
#   responsable VARCHAR2(50),
#   reserva_id NUMBER,
#   CONSTRAINT fk_informe_reserva FOREIGN KEY (reserva_id) REFERENCES reserva(id)
# );

import random


class Informe:
    def __init__(self, fechainforme=None, contenido=None, tipoinforme=None, responsable=None, reserva_id=None):
        self._id = self.generar_id()
        self._fechainforme = fechainforme
        self._contenido = contenido
        self._tipoinforme = tipoinforme
        self._responsable = responsable
        self._reserva_id = reserva_id

    def __str__(self):
        return f'Informe(id={self.id}, fechainforme={self.fechainforme}, contenido={self.contenido}, tipoinforme={self.tipoinforme}, responsable={self.responsable}, reserva_id={self.reserva_id})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def fechainforme(self):
        return self._fechainforme

    @fechainforme.setter
    def fechainforme(self, fechainforme):
        self._fechainforme = fechainforme

    @property
    def contenido(self):
        return self._contenido

    @contenido.setter
    def contenido(self, contenido):
        self._contenido = contenido

    @property
    def tipoinforme(self):
        return self._tipoinforme

    @tipoinforme.setter
    def tipoinforme(self, tipoinforme):
        self._tipoinforme = tipoinforme

    @property
    def responsable(self):
        return self._responsable

    @responsable.setter
    def responsable(self, responsable):
        self._responsable = responsable

    @property
    def reserva_id(self):
        return self._reserva_id

    @reserva_id.setter
    def reserva_id(self, reserva_id):
        self._reserva_id = reserva_id

    def insertar_informe(self):
        return (self._id, self._fechainforme, self._contenido, self._tipoinforme, self._responsable, self._reserva_id)
