
import random


class Itinerario:
    def __init__(self, descripcion=None, duracion=None, paisorigen=None, ciudadorigen=None, paisdestino=None, ciudaddestino=None):
        self._id = self.generar_id()
        self._descripcion = descripcion
        self._duracion = duracion
        self._paisorigen = paisorigen
        self._ciudadorigen = ciudadorigen
        self._paisdestino = paisdestino
        self._ciudaddestino = ciudaddestino

    def __str__(self):
        return f'Itinerario(id={self.id}, descripcion={self.descripcion}, duracion={self.duracion}, paisorigen={self.paisorigen}, ciudadorigen={self.ciudadorigen}, paisdestino={self.paisdestino}, ciudaddestino={self.ciudaddestino})'

    def generar_id(self):
        return random.randint(1, 1000000000)

    # getters y setters

    @property
    def id(self):
        return self._id

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, duracion):
        self._duracion = duracion

    @property
    def paisorigen(self):
        return self._paisorigen

    @paisorigen.setter
    def paisorigen(self, paisorigen):
        self._paisorigen = paisorigen

    @property
    def ciudadorigen(self):
        return self._ciudadorigen

    @ciudadorigen.setter
    def ciudadorigen(self, ciudadorigen):
        self._ciudadorigen = ciudadorigen

    @property
    def paisdestino(self):
        return self._paisdestino

    @paisdestino.setter
    def paisdestino(self, paisdestino):
        self._paisdestino = paisdestino

    @property
    def ciudaddestino(self):
        return self._ciudaddestino

    @ciudaddestino.setter
    def ciudaddestino(self, ciudaddestino):
        self._ciudaddestino = ciudaddestino

    def insertar_itinero(self):
        return (self._id, self._descripcion, self._duracion, self._paisorigen, self._ciudadorigen, self._paisdestino, self._ciudaddestino)
