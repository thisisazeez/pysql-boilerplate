import mysql.connector




mydb = mysql.connector.connect(
    host="localhost",
    database="lincoln_express",
    user="root",
    password="",
)

mycursor = mydb.cursor()
mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS passengers(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        address VARCHAr(255),
        age INT,
        PRIMARY KEY(ID)
    )
    
    """
)

mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS plane(
        ID INT NOT NULL AUTO_INCREMENT,
        seat VARCHAR(255),
        PRIMARY KEY(ID)
    )
    
    """
)

mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS booking(
        BOOKING_ID INT NOT NULL AUTO_INCREMENT,
        ffrom VARCHAR(255),
        tto VARCHAR(255),
        PRIMARY KEY(BOOKING_ID),
        seat VARCHAR(255) REFRENCES plane(seat)
    )
    
    """
)

# mycursor.execute(
#     """ CREATE TABLE IF NOT EXISTS ticket(
#         TICKET_ID INT NOT NULL AUTO_INCREMENT,
#         date DATE,
#         address VARCHAR(255),
#         user
#         PRIMARY KEY(ID)
#     )
    
#     """
# )