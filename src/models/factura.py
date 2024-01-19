
# -- Tabla factura
# CREATE TABLE factura (
#   id NUMBER PRIMARY KEY,
#   fechafactura DATE,
#   montototal DECIMAL(10, 2),
#   metodopago VARCHAR2(50),
#   estadopago VARCHAR2(50),
#   reserva_id NUMBER,
#   CONSTRAINT fk_factura_reserva FOREIGN KEY (reserva_id) REFERENCES reserva(id)
# );

import random


class Factura:
    def __init__(self, fechafactura=None, montototal=None, metodopago=None, estadopago=None, reserva_id=None):
        self._id = self.generar_id()
        self._fechafactura = fechafactura
        self._montototal = montototal
        self._metodopago = metodopago
        self._estadopago = estadopago
        self._reserva_id = reserva_id

    def __str__(self):
        return f'Factura(id={self.id}, fechafactura={self.fechafactura}, montototal={self.montototal}, metodopago={self.metodopago}, estadopago={self.estadopago}, reserva_id={self.reserva_id})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def fechafactura(self):
        return self._fechafactura

    @fechafactura.setter
    def fechafactura(self, fechafactura):
        self._fechafactura = fechafactura

    @property
    def montototal(self):
        return self._montototal

    @montototal.setter
    def montototal(self, montototal):
        self._montototal = montototal

    @property
    def metodopago(self):
        return self._metodopago

    @metodopago.setter
    def metodopago(self, metodopago):
        self._metodopago = metodopago

    @property
    def estadopago(self):
        return self._estadopago

    @estadopago.setter
    def estadopago(self, estadopago):
        self._estadopago = estadopago

    @property
    def reserva_id(self):
        return self._reserva_id

    @reserva_id.setter
    def reserva_id(self, reserva_id):
        self._reserva_id = reserva_id

    def insertar_factura(self):
        return (self._id, self._fechafactura, self._montototal, self._metodopago, self._estadopago, self._reserva_id)
