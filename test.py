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
        full_name VARCHAR(255),
        password VARCHAR(255) NOT NULL,
        address VARCHAr(255),
        age INT,
        PRIMARY KEY(ID)
    )
    
    """
)


mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS booking(
        BOOKING_ID INT NOT NULL AUTO_INCREMENT,
        Address VARCHAR(255) references passengers(address),
        destination VARCHAR(255),
        UNIQUE(BOOKING_ID)
    )
    
    """
)

mycursor.execute(
    """ ALTER TABLE booking ADD IF NOT EXISTS(
        seat INT references plane(seat, PLANE_ID)
    );
    
    """
)

mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS plane(
        PLANE_ID INT NOT NULL AUTO_INCREMENT,
        seat VARCHAR(255),
        User VARCHAR(255) references passengers(full_name, address, ID),
        UNIQUE(PLANE_ID)
    )
    
    """
)

mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS ticket(
        TICKET_ID INT NOT NULL AUTO_INCREMENT,
        date_given DATE,
        QrCode VARCHAR(255) NOT NULL,
        address VARCHAR(255),
        user VARCHAR(255) references passengers(full_name, address, ID),
        UNIQUE(TICKET_ID),
        booking_id VARCHAR(255) NOT NULL references booking(BOOKING_ID)
    )
    
    """
)

mycursor.execute(
    """ CREATE TABLE IF NOT EXISTS admin(
        User INT(255) references passengers(ID),
        Ticket INT(255) references ticket(ID),
        Plane INT(255) references plane(PLANE_ID),
        Bookings INT(255) references plane(BOOKING_ID)

    )
    
    """
)

# mycursor.execute(
#     """ ALTER TABLE passengers ADD IF NOT EXISTS(
#         booking INT references booking(BOOKING_ID)
#     );
    
#     """
# )