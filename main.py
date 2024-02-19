from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()

# Allow all origins, allow credentials, allow specific headers, allow specific methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, replace * with specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, replace * with specific methods if needed
    allow_headers=["*"],  # Allows all headers, replace * with specific headers if needed
)

# Initialize MongoDB connection
client = MongoClient('mongodb+srv://admin:admin@cluster0.fosjyo8.mongodb.net/?retryWrites=true&w=majority')
db = client['e-basa_db']
users_collection = db['users']

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User model
class User(BaseModel):
    user_type: str
    test: str
    username: str
    firstname: str
    lastname: str
    middle_initial: str
    age: int
    email: str
    gender: str
    school: str
    password: str

# UserInDB model
class UserInDB(User):
    pass

# Register route
@app.post("/register/")
def register_user(user: User):
    user_exist = users_collection.find_one({"username": user.username})
    if user_exist:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user_data = user.dict()
    users_collection.insert_one(user_data)
    return {"username": user.username, "email": user.email, "user_type": user.user_type}

# Authenticate user
def authenticate_user(username: str, password: str):
    user = users_collection.find_one({"username": username})
    if not user:
        return False
    if user['password'] != password:  # Compare plain text passwords
        return False
    return user

# Get current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Code for OAuth2 validation can be added here
    user = users_collection.find_one({"username": token})
    return user

# Login route
class LoginRequest(BaseModel):
    username: str
    password: str

# @app.post("/login/")
# def login(login_data: LoginRequest):
#     user = authenticate_user(login_data.username, login_data.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     return {"access_token": user['username'], "token_type": "bearer"}
    
@app.post("/login/")
def login(login_data: LoginRequest):
    user = authenticate_user(login_data.username, login_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    test_value = user.get("test")  # Get the value of 'test' field from the user, default to 0 if not found
    
    return {"access_token": user['username'], "token_type": "bearer", "test": test_value}
