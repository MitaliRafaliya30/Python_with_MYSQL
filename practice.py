import mysql.connector as sql

connection = sql.connect(
    host = "localhost" ,
    user = "Mira",
    password = "Mira@1406" , 
    database = "m_db"
    
)

cursor = connection.cursor()

cursor.execute("SHOW DATABASES")