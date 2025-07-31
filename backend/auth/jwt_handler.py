from jose import JWTError, jwt
from datetime import datetime, timedelta

import os
from dotenv import load_dotenv

# for environment variable
load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Function to create an access token
def create_access_token(data: dict): # Data will contain user-related information like email ID and username
    
    # creating a shallow copy of the data
    to_encode = data.copy()
    
    # calculatiing the expiry time for the token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # adding the expiration field into the payload dictionary
    to_encode.update({"exp":expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Function to verify the token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None