import os
from dotenv import find_dotenv, load_dotenv
import mysql.connector

# for environment variable
dotenv_path = find_dotenv()

# load up the environment variables
load_dotenv(dotenv_path)


# creating global variable for connection 
__connection = None

# Function to create Database connection
def get_connection():
    
    global __connection
    
    if __connection is None or not __connection.is_connected():
        __connection = mysql.connector.connect(
            user= os.getenv("USER"),
            password= os.getenv("DATABASE_PASSWORD"),
            host= os.getenv("HOST"),
            database= os.getenv("DATABASE_NAME")
        )
    
    print("Connection Establish Successfully")
    return __connection

