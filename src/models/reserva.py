# -- Tabla reserva
# CREATE TABLE reserva (
#   id NUMBER PRIMARY KEY,
#   fechareserva DATE,
#   asientos INT,
#   asientosclaseeconomica INT,
#   asientosclaseejecutiva INT,
#   asientosprimeraclase INT,
#   vuelo_id NUMBER,
#   cliente_id NUMBER,
#   CONSTRAINT fk_reserva_vuelo FOREIGN KEY (vuelo_id) REFERENCES vuelo(id),
#   CONSTRAINT fk_reserva_cliente FOREIGN KEY (cliente_id) REFERENCES cliente(id_cliente)
# );

import random


class Reserva:
    def __init__(self, fechareserva=None, asientos=None, asientosclaseeconomica=None, asientosclaseejecutiva=None, asientosprimeraclase=None, vuelo_id=None, cliente_id=None):
        self._id = self.generar_id()
        self._fechareserva = fechareserva
        self._asientos = asientos
        self._asientosclaseeconomica = asientosclaseeconomica
        self._asientosclaseejecutiva = asientosclaseejecutiva
        self._asientosprimeraclase = asientosprimeraclase
        self._vuelo_id = vuelo_id
        self._cliente_id = cliente_id

    def __str__(self):
        return f'Reserva(id={self.id}, fechareserva={self.fechareserva}, asientos={self.asientos}, asientosclaseeconomica={self.asientosclaseeconomica}, asientosclaseejecutiva={self.asientosclaseejecutiva}, asientosprimeraclase={self.asientosprimeraclase}, vuelo_id={self.vuelo_id}, cliente_id={self.cliente_id})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def fechareserva(self):
        return self._fechareserva

    @fechareserva.setter
    def fechareserva(self, fechareserva):
        self._fechareserva = fechareserva

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, asientos):
        self._asientos = asientos

    @property
    def asientosclaseeconomica(self):
        return self._asientosclaseeconomica

    @asientosclaseeconomica.setter
    def asientosclaseeconomica(self, asientosclaseeconomica):
        self._asientosclaseeconomica = asientosclaseeconomica

    @property
    def asientosclaseejecutiva(self):
        return self._asientosclaseejecutiva

    @asientosclaseejecutiva.setter
    def asientosclaseejecutiva(self, asientosclaseejecutiva):
        self._asientosclaseejecutiva = asientosclaseejecutiva

    @property
    def asientosprimeraclase(self):
        return self._asientosprimeraclase

    @asientosprimeraclase.setter
    def asientosprimeraclase(self, asientosprimeraclase):
        self._asientosprimeraclase = asientosprimeraclase

    @property
    def vuelo_id(self):
        return self._vuelo_id

    @vuelo_id.setter
    def vuelo_id(self, vuelo_id):
        self._vuelo_id = vuelo_id

    @property
    def cliente_id(self):
        return self._cliente_id

    @cliente_id.setter
    def cliente_id(self, cliente_id):
        self._cliente_id = cliente_id

    def insertar_reserva(self):
        return (self._id, self._fechareserva, self._asientos, self._asientosclaseeconomica, self._asientosclaseejecutiva, self._asientosprimeraclase, self._vuelo_id, self._cliente_id)
