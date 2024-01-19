-- Tabla cliente
CREATE TABLE CLIENTE (
    ID_CLIENTE INT PRIMARY KEY,
    NOMBRE VARCHAR2(255) NOT NULL,
    APELLIDO VARCHAR2(255) NOT NULL,
    CEDULA VARCHAR2(255) NOT NULL,
    GENERO VARCHAR2(255) NOT NULL,
    NACIONALIDAD VARCHAR2(255) NOT NULL,
    FECHA_NACIMIENTO VARCHAR2(255) NOT NULL,
    EMAIL VARCHAR2(255) NOT NULL,
    ESTADOCIVIL VARCHAR2(255) NOT NULL,
    PROPOSITO VARCHAR2(255) NOT NULL,
    DIRECCION VARCHAR2(255) NOT NULL,
    NOMBREEMPRESA VARCHAR2(255),
    CARGO VARCHAR2(255),
    DIRECCIONEMPRESA VARCHAR2(255),
    DOCUMENTODOCUMENTOIDENTIDAD VARCHAR2(255),
    DOCUMENTOPASAPORTE BLOB,
    DOCUMENTOVISA BLOB,
    DOCUMENTOORDEN BLOB
);

-- Tabla empleado
CREATE TABLE EMPLEADO (
    ID INT PRIMARY KEY,
    USUARIO VARCHAR2(50),
    CONTRASENA VARCHAR2(50),
    DNI VARCHAR2(20)
);

-- Tabla vuelo
CREATE TABLE VUELO (
    ID NUMBER PRIMARY KEY,
    NUMEROVUELO VARCHAR2(50),
    FECHASALIDA VARCHAR(50),
    HORASALIDA VARCHAR2(50),
    ORIGEN VARCHAR2(50),
    DESTINO VARCHAR2(50),
    DURACION VARCHAR2(50),
    ESCALAS VARCHAR2(50),
    CLASE VARCHAR2(50),
    PRECIO VARCHAR2(50)
);

-- Tabla itinerario
CREATE TABLE ITINERARIO (
    ID NUMBER PRIMARY KEY,
    DESCRIPCION VARCHAR2(100),
    DURACION VARCHAR2(50),
    PAISORIGEN VARCHAR2(50),
    CIUDADORIGEN VARCHAR2(50),
    PAISDESTINO VARCHAR2(50),
    CIUDADDESTINO VARCHAR2(50)
);

-- Tabla tarifa
CREATE TABLE TARIFA (
    ID NUMBER PRIMARY KEY,
    NOMBRE VARCHAR2(50),
    MONTO VARCHAR2(50),
    RESTRICCIONES VARCHAR2(100),
    VUELO_ID NUMBER,
    CONSTRAINT FK_TARIFA_VUELO FOREIGN KEY (VUELO_ID) REFERENCES VUELO(ID)
);

-- Tabla factura
CREATE TABLE FACTURA (
    ID NUMBER PRIMARY KEY,
    FECHAFACTURA VARCHAR2(50),
    MONTOTOTAL VARCHAR2(50),
    METODOPAGO VARCHAR2(50),
    ESTADOPAGO VARCHAR2(50),
    RESERVA_ID NUMBER,
    CONSTRAINT FK_FACTURA_RESERVA FOREIGN KEY (RESERVA_ID) REFERENCES RESERVA(ID)
);


-- Inserting 30 fictitious data entries into the VUELO table
BEGIN
    FOR i IN 1..30 LOOP
        INSERT INTO VUELO (
            ID,
            NUMEROVUELO,
            FECHASALIDA,
            HORASALIDA,
            ORIGEN,
            DESTINO,
            DURACION,
            ESCALAS,
            CLASE,
            PRECIO
        ) VALUES (
            i,
            'VUELO' || LPAD(i, 3, '0'),
            TO_CHAR(SYSDATE + i, 'DD-MON-YYYY'),
            TO_CHAR(SYSDATE + i, 'HH24:MI:SS'),
            'City' || DBMS_RANDOM.STRING('U', 3),
            'City' || DBMS_RANDOM.STRING('U', 3),
            DBMS_RANDOM.VALUE(1, 10) || 'h',
            TO_CHAR(DBMS_RANDOM.VALUE(0, 5)),
            CASE WHEN DBMS_RANDOM.VALUE < 0.5 THEN 'Economy' ELSE 'Business' END,
            TO_CHAR(DBMS_RANDOM.VALUE(100, 1000), '999.99')
        );
    END LOOP;
    COMMIT;
END;
/
