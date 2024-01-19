import oracledb

# python -m pip install oracledb

cnx = oracledb.connect(
    user="C##MICKAELL_MORAN",
    password="C##MICKAELL_MORAN",
    dsn="localhost:1521/xe"
)

cursor = cnx.cursor()