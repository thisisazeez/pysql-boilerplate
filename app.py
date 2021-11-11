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
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        address VARCHAR(255),
        age INT,
        PRIMARY KEY(ID)
    )
    
    """
)

mycursor.execute(
    """ ALTER TABLE customers ADD IF NOT EXISTS(
        age INT
    );
    
    """
)

mycursor.execute(
    "SELECT * FROM customers LIMIT5"
)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

sql = "INSERT INTO customers(name, address, age) VALUES(%s, %s, %s)"

val = ('john', 'bwari', 90)
mycursor.execute(sql, val)


mydb.commit()