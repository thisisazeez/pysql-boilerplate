import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    database="emp",
    user="root",
    password="",
)



mycursor = mydb.cursor()
mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS customers(
        name VARCHAR(255),
        address VARCHAr(255)
    )
    
    """
)

mycursor.execute(
    """ ALTER TABLE customers ADD IF NOT EXISTS(
        age INT
    );
    
    """
)

sql = "INSERT INTO customers(name, address, age) VALUES(%s, %s, %s)"

val = ('john', 'bwari', 90)
mycursor.execute(sql, val)
mydb.commit()