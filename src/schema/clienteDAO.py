from oracledb import Connection, Cursor
from models.cliente import Cliente

class ClienteDAO:

    def __init__(self, conn: Connection, cursor: Cursor) -> None:
        self.conn = conn
        self.cursor = cursor
    
    def insert(self, cliente: Cliente):
        if cliente is None:
            raise Exception("Debe indicar el cliente")

        sql = """
        INSERT INTO CLIENTE (
            id_cliente, nombre, apellido, cedula, genero, nacionalidad, fecha_nacimiento,
            email, estadoCivil, proposito, direccion, notificacion, nombreEmpresa,
            cargo, direccionEmpresa, documentoDocumentoIdentidad, documentoPasaporte,
            documentoVisa, documentoOrden
        ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19
        )
        """
        self.cursor.execute(sql, cliente.insertar_cliente())
        self.conn.commit()

    def update(self, cliente: Cliente):

        if cliente is None or cliente.idCliente is None:
            raise Exception("Debe indicar un cliente válido con ID")
        
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
        self.conn.commit()


    def delete(self, idCliente: int):
        sql = "DELETE FROM CLIENTE WHERE IDCLIENTE=:1"
        values = (idCliente,)

        self.cursor.execute(sql, values)
        self.conn.commit()

    def obtener_lista_clientes(self):
        sql = "SELECT id_cliente, nombre, apellido, cedula, genero, nacionalidad, fecha_nacimiento, email, estadoCivil, proposito, direccion, notificacion, nombreEmpresa, cargo, direccionEmpresa, documentoDocumentoIdentidad, documentoPasaporte, documentoVisa, documentoOrden FROM CLIENTE"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

