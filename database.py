import mysql.connector
from mysql.connector import Error


# A function to connect to our MySQL Server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print("Error: '{err}'")

    return connection


def pw(args):
    pass


connection = create_server_connection("localhost", "root", pw)


# code bellow is for creating the database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print("Error: '{err}'")


create_database_query = "Create Database college"
create_database(connection, create_database_query)


# code regarding connecting to the database and implementing a database name
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print("Error: '{err}'")

    return connection


# this is a database query execution function
# (This is going to take our SQL queries,
# stored in Python as strings, and pass them to the cursor.execute()
# method to execute them on the server.)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print("Error: '{err}'")


create_college_table = """
CREATE TABLE College (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """

connection = create_db_connection("localhost", "root", pw, db)  # Connect to the Database
execute_query(connection, create_teacher_table)  # Execute our defined query
