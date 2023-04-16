import pyodbc
#Creando conexion y cursor para ejecutar acciones en DB
conn = pyodbc.connect("DRIVER={Oracle in OraDB19Home1};DBQ=ORCL;UID=HR;PWD=Oracle2023")
cur = conn.cursor()
cur.execute("SELECT * FROM EMPLOYEES;")
#Acomodando los datos
row = cur.fetchone()
rows = cur.fetchall()
for i in rows:
	print(i)
#Cerrando conexion despues de usarla
cur.close()
conn.close()