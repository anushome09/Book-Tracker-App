from backend.database import get_connection
from backend.schemas.user import UserCreate
from backend.utils.security import hash_password

# function to create a user
def create_new_user(user: UserCreate):
    
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