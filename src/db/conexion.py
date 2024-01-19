import oracledb
from decouple import config
from ..models.cliente import Cliente
from ..models.empleado import Empleado
from ..models.factura import Factura
from ..models.itinerario import Itinerario
from ..models.reserva import Reserva
from ..models.tarifa import Tarifa
from ..models.vuelo import Vuelo


class ConexionDB:
    def __init__(self):
        self.connection = oracledb.connect(
            user=config('DATABASE_USER'),
            password=config('DATABASE_PASSWORD'),
            dsn=f"{config('DATABASE_HOST')}:{config('DATABASE_PORT')}/{config('DATABASE_NAME')}"
        )

        self.cursor = self.connection.cursor()

        print(self.connection.version)


    #* MODELO CLIENTE
    def insert_cliente(self, cliente: Cliente):
        sql = """
        INSERT INTO CLIENTE (
            id_cliente, nombre, apellido, cedula, genero, nacionalidad, fecha_nacimiento,
            email, estadoCivil, proposito, direccion, nombreEmpresa,
            cargo, direccionEmpresa, documentoDocumentoIdentidad, documentoPasaporte,
            documentoVisa, documentoOrden
        ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18
        )
        """
        self.cursor.execute(sql, cliente.insertar_cliente())
        self.connection.commit()

    def update_cliente(self, cliente: Cliente):
        sql = """
            UPDATE CLIENTE
            SET NOMBRE=:1, APELLIDO=:2, CEDULA=:3, GENERO=:4, NACIONALIDAD=:5,
            FECHA_NACIMIENTO=:6, EMAIL=:7, ESTADO_CIVIL=:8, PROPOSITO=:9,
            DIRECCION=:10, NOTIFICACION=:11, NOMBRE_EMPRESA=:12, CARGO=:13,
            DIRECCION_EMPRESA=:14, DOCUMENTO_DOCUMENTO_IDENTIDAD=:15,
            DOCUMENTO_PASAPORTE=:16, DOCUMENTO_VISA=:17, DOCUMENTO_ORDEN=:18
            WHERE ID_CLIENTE=:19
            """
        values = (
            cliente.nombre, cliente.apellido, cliente.cedula, cliente.genero,
            cliente.nacionalidad, cliente.fecha_nacimiento, cliente.email,
            cliente.estadoCivil, cliente.proposito, cliente.direccion,
            cliente.notificacion, cliente.nombreEmpresa, cliente.cargo,
            cliente.direccionEmpresa, cliente.documentoDocumentoIdentidad,
            cliente.documentoPasaporte, cliente.documentoVisa,
            cliente.documentoOrden, cliente.idCliente
        )
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete_cliente(self, idCliente: int):
        sql = "DELETE FROM CLIENTE WHERE IDCLIENTE=:1"
        values = (idCliente,)

        self.cursor.execute(sql, values)
        self.connection.commit()

    def obtener_lista_clientes(self):
        sql = "SELECT id_cliente, nombre, apellido, cedula, genero, nacionalidad, fecha_nacimiento, email, estadoCivil, proposito, direccion, notificacion, nombreEmpresa, cargo, direccionEmpresa, documentoDocumentoIdentidad, documentoPasaporte, documentoVisa, documentoOrden FROM CLIENTE"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtener_cliente(self, idCliente: int):
        sql = "SELECT id_cliente, nombre, apellido, cedula, genero, nacionalidad, fecha_nacimiento, email, estadoCivil, proposito, direccion, notificacion, nombreEmpresa, cargo, direccionEmpresa, documentoDocumentoIdentidad, documentoPasaporte, documentoVisa, documentoOrden FROM CLIENTE WHERE id_cliente=:1"
        values = (idCliente,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

    # MODELO EMPLEADO

    def insert_empleado(self, empleado: Empleado):
        sql = """
        INSERT INTO EMPLEADO (
            ID, USUARIO, CONTRASENA, DNI
        ) VALUES (
            :1, :2, :3, :4
        )
        """
        self.cursor.execute(sql, empleado.insertar_empleado())
        self.connection.commit()

    def update_empleado(self, empleado: Empleado):
        sql = """
            UPDATE EMPLEADO
            SET USUARIO=:1, CONTRASENA=:2, DNI=:3
            WHERE ID=:4
        """
        values = (
            empleado.usuario, empleado.contrasena, empleado.dni, empleado.id
        )
        self.cursor.execute(sql, values)
        self.connection.commit()

    def delete_empleado(self, id: int):
        sql = "DELETE FROM EMPLEADO WHERE ID=:1"
        values = (id,)

        self.cursor.execute(sql, values)
        self.connection.commit()

    def obtener_lista_empleados(self):
        sql = "SELECT ID, USUARIO, CONTRASENA, DNI FROM EMPLEADO"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def obtener_empleado(self, id: int):
        sql = "SELECT ID, USUARIO, CONTRASENA, DNI FROM EMPLEADO WHERE ID=:1"
        values = (id,)
        self.cursor.execute(sql, values)
        return self.cursor.fetchone()

  
    # MODELO ITINERARIO

    def insertar_itinerario(self, itinerario: Itinerario):
        sql = """
        INSERT INTO ITINERARIO (
            ID, DESCRIPCION, DURACION, PAISORIGEN, PAISDESTINO, CIUDADDESTINO
        ) VALUES (
            :1, :2, :3, :4, :5, :6
        )
        """
        self.cursor.execute(sql, itinerario.insertar_itinerario())
        self.connection.commit()

    def delete_itinerario(self, id: int):
        sql = "DELETE FROM ITINERARIO WHERE ID=:1"
        values = (id,)

        self.cursor.execute(sql, values)
        self.connection.commit()

    def modificar_itinerario(self, itinerario: Itinerario):
        sql = """
            UPDATE ITINERARIO
            SET DESCRIPCION=:1, DURACION=:2, PAISORIGEN=:3, PAISDESTINO=:4, CIUDADDESTINO=:5
            WHERE ID=:6
        """
        values = (
            itinerario.descripcion, itinerario.duracion, itinerario.paisOrigen, itinerario.paisDestino, itinerario.ciudadDestino, itinerario.id
        )
        self.cursor.execute(sql, values)
        self.connection.commit()

    def obtener_itinerario(self):
        sql = "SELECT * FROM ITINERARIO"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #* MODELO TARIFA
    def insertar_tarifa(self, tarifa: Tarifa):
        sql = """
        INSERT INTO TARIFA (
            ID, NOMBRE, MONTO, RESTRICCIONES
        ) VALUES (
            :1, :2, :3, :4
        )
        """
        self.cursor.execute(sql, tarifa.insertar_tarifa())
        self.connection.commit()

    def delete_tarifa(self, id: int):
        sql = "DELETE FROM TARIFA WHERE ID=:1"
        values = (id,)

        self.cursor.execute(sql, values)
        self.connection.commit()


    def obtener_tarifa(self, condicion_clase = None):
        if condicion_clase:
            sql = "SELECT * FROM TARIFA WHERE NOMBRE=:1"
            values = (condicion_clase,)
            self.cursor.execute(sql, values)
        else:
            sql = "SELECT * FROM TARIFA"
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    #* MODELO VUELO
    def insertar_vuelo(self, vuelo: Vuelo):
        sql = """
        INSERT INTO VUELO (
            ID, NUMEROVUELO, FECHASALIDA, HORASALIDA, ORIGEN, DESTINO, DURACION, ESCALAS, CLASE, PRECIO
        ) VALUES (
            :1, :2, :3, :4, :5, :6, :7, :8, :9, :10
        )
        """
        self.cursor.execute(sql, vuelo.insertar_vuelo())
        self.connection.commit()

    def delete_vuelo(self, id: int):
        sql = "DELETE FROM VUELO WHERE ID=:1"
        values = (id,)

        self.cursor.execute(sql, values)
        self.connection.commit()

    def modificar_vuelo(self, vuelo: Vuelo):
        try:
            sql = """
                UPDATE VUELO
                SET NUMEROVUELO=:numerovuelo, FECHASALIDA=:fechasalida, ORIGEN=:origen, DESTINO=:destino, DURACION=:duracion
                WHERE ID=:id
            """
            values = {
                'id': int(vuelo.id),
                'numerovuelo': vuelo.numerovuelo,
                'fechasalida': vuelo.fechasalida,
                'origen': vuelo.origen,
                'destino': vuelo.destino,
                'duracion': vuelo.duracion,
            }
            self.cursor.execute(sql, values)

            self.connection.commit()
            print("Vuelo modificado exitosamente!")
            return True
        except Exception as e:
            print(f"Error al modificar el vuelo: {e}")
            print("Detalles adicionales:", values)

    # OBTENER UN VUELO POR FECHASALIDA
    def obtener_vuelo(self, condicion_clase=None):
        if condicion_clase:
            sql = "SELECT * FROM VUELO WHERE FECHASALIDA=:1"
            values = (condicion_clase,)
            self.cursor.execute(sql, values)
        else:
            sql = "SELECT * FROM VUELO"
            self.cursor.execute(sql)

        return self.cursor.fetchall()
