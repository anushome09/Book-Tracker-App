from backend.database import get_connection
from backend.schemas.user import UserCreate
from backend.utils.security import hash_password

# function to get user using email ID
def get_user_by_email_or_username(email: str, username: str):
    
    # Getting the database connection
    db_connection = get_connection()
    cursor = db_connection.cursor(dictionary=True)
    
    # Executing the search query
    query = """
                SELECT * FROM users WHERE email = %s OR username = %s
            """
    cursor.execute(query, (email, username))
    user = cursor.fetchone()
    
    db_connection.close()
    return user

# function to create a user
def create_new_user(user: UserCreate):
    
    # Checking if the email or username is already present
    exisitng_user = get_user_by_email_or_username(user.email, user.username)
    if exisitng_user['email'] == user.email:
        raise ValueError("Email is already registered")
    elif exisitng_user['username'] == user.username:
        raise ValueError("Username is already taken")
    
    
    # Getting the database connection
    db_connection = get_connection()
    cursor = db_connection.cursor()
    
    # Encrypting the password
    hashed_pw = hash_password(user.password)
    
    # Inserting a new user
    query = """
                INSERT INTO users (username, email, password, full_name, profile_picture)
                VALUES (%s, %s, %s, %s, %s)
            """
    cursor.execute(query, (user.username, user.email, hashed_pw, user.full_name, user.profile_picture))
    db_connection.commit()
    
    # Getting the new user id
    user_id = cursor.lastrowid
    db_connection.close()
    
    return user_id