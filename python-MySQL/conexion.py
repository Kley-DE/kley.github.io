import mysql.connector
conexion = mysql.connector.connect(
    user="root", password="", 
    host="localhost", 
    database="mueblessa" ,
    port="3306"
)
if(conexion):
    print("Se conecto")
else:
    print("NO se conceto")