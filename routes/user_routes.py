from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models.user import Result, User, LoginRequest
from database.connection import users_collection, authenticate_user
from bson import ObjectId
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# POST
@router.post("/register/")
def register_post(user: User):
    user_exist = users_collection.find_one({"username": user.username})
    if user_exist:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user_data = user.dict()
    users_collection.insert_one(user_data)
    return {"username": user.username, "email": user.email, "user_type": user.user_type}

@router.post("/login/")
def login_post(login_data: LoginRequest):
    user = authenticate_user(login_data.username, login_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    
    test_value = user.get("test")
    user_id_value = str(user.get("_id"))

    return {"access_token": user['username'], "token_type": "bearer", "test": test_value, "user_id": user_id_value}

@router.post("/users/{user_id}/pretest", response_model=User)
async def add_pretest_result(user_id: str, result: Result):
    user_object_id = ObjectId(user_id)
    users_collection.update_one({"_id": user_object_id}, {"$push": {"pretest_results": result.dict()}})
    return JSONResponse(content={"message": "Pretest result added successfully"})

@router.post("/users/{user_id}/posttest", response_model=User)
async def add_posttest_result(user_id: str, result: Result):
    user_object_id = ObjectId(user_id)
    users_collection.update_one({"_id": user_object_id}, {"$push": {"posttest_results": result.dict()}})
    return JSONResponse(content={"message": "Posttest result added successfully"})

# GET

@router.get("/users/", response_model=List[User])
async def get_users():
    users = []
    for user in users_collection.find({}):
        user['_id'] = str(user['_id'])  # Convert _id to string
        user['user_id'] = user.pop('_id')  # Rename _id to user_id
        users.append(user)
    return users

@router.get("/users/{id}", response_model=User)
async def get_user(id: str):
    object_id = ObjectId(id)
    user = users_collection.find_one({"_id": object_id})
    if user:
        user['_id'] = str(user['_id'])  # Convert _id to string
        user['user_id'] = user.pop('_id')  # Rename _id to user_id
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    object_id = ObjectId(user_id)
    deletion_result = users_collection.delete_one({"_id": object_id})
    if deletion_result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")