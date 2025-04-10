# 1. import and install mysql connectior
import mysql.connector as sql


# 2. create MYSQL connection
try:
    connection = sql.connect(
    host = "localhost" , 
    user = "Mira" ,
    password = "Mira@1406" , 
    database = "student"
    )
    cursor = connection.cursor() #  create  cursor :  it helps to execute all queries
    print("connection established")
except:
    print("Connection error")                                            


# 3. create database
# cursor.execute("CREATE DATABASE MY_DB")       
connection.commit()               # commit changes to database         
              

# show all databases in console
# for i in cursor:
#     print(i)
# print(cursor)


# PERFORM CRUD OPERATIONS

# 4. create table in database
# cursor.execute("CREATE TABLE studentinfo(id INT PRIMARY KEY , name VARCHAR(20) , age INT)")
# connection.commit()
# print("table is created")


# Insert records in table 
# cursor.execute(
#     """
#     INSERT INTO studentinfo VALUES
#     (6 , 'mahi' , 20), 
#     (9 , 'palak' , 21), 
#     (12 , 'raj' , 19), 
#     (44, 'aeshva' , 18), 
#     (51, 'krstle' , 15) 
#     """
# )
# connection.commit()
# print("Inserted successfully")


# 5. Read : select data from the table 
cursor.execute("SELECT * FROM studentinfo")
res = cursor.fetchall()    # to fatch all rows
print(res)


# read perticular column here name column
for i in res:
    print(i[1])


# 6 Update : Update data in the table 
cursor.execute("UPDATE studentinfo SET  name = 'mahek' WHERE id = 1")
connection.commit()
print("updated successfully")


# 7 Delete : delete data from the table 
cursor.execute("DELETE FROM studentinfo WHERE id = 2")
connection.commit()
print("Deleted successfully")




# read / show list of aa databases
cursor.execute("SHOW DATABASES")
res = cursor.fetchall()
print(res)

# read / show list of all tables 
cursor.execute("SHOW TABLES")
res = cursor.fetchall()
print(res)

# drop database
# cursor.execute("DROP DATABASE m_db")
# connection.commit()
# print("drop database successfully")

# drop table
# cursor.execute("DROP TABLE TABLE_NAME")
# connection.commit()
# print("drop table successfully")














