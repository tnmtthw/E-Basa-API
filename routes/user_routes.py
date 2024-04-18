from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer
from models.user import Result, User, UserUpdate, LoginRequest
from database.connection import users_collection, authenticate_user
from bson import ObjectId
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# POST
@router.post("/register")
def register_post(user: User):
    user_exist = users_collection.find_one({"username": user.username})
    if user_exist:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user_data = user.dict()
    users_collection.insert_one(user_data)
    return {"username": user.username, "userType": user.userType}

# @router.post("/login")
# def login_post(login_data: LoginRequest):
#     user = authenticate_user(login_data.username, login_data.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
    
#     test_value = user.get("test")
#     userId_value = str(user.get("_id"))

#     return {"access_token": user['username'], "token_type": "bearer", "test": test_value, "userId": userId_value}
@router.post("/login")
def login_post(login_data: LoginRequest):
    user = authenticate_user(login_data.username)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect LRN")
    
    test_value = user.get("test")
    userId_value = str(user.get("_id"))

    return {"access_token": user['username'], "token_type": "bearer", "test": test_value, "userId": userId_value}

@router.post("/users/{userId}/pretest", response_model=User)
async def add_pretest_result(userId: str, result: Result):
    user_object_id = ObjectId(userId)
    users_collection.update_one({"_id": user_object_id}, {"$push": {"pretest_results": result.dict()}})
    return JSONResponse(content={"message": "Pretest result added successfully"})

@router.post("/users/{userId}/posttest", response_model=User)
async def add_posttest_result(userId: str, result: Result):
    user_object_id = ObjectId(userId)
    users_collection.update_one({"_id": user_object_id}, {"$push": {"posttest_results": result.dict()}})
    return JSONResponse(content={"message": "Posttest result added successfully"})

# GET
@router.get("/users", response_model=List[User])
async def get_users():
    users = []
    for user in users_collection.find({}):
        user['_id'] = str(user['_id'])
        user['userId'] = user.pop('_id')
        users.append(user)
    return users

@router.get("/users/{id}", response_model=User)
async def get_user(id: str):
    object_id = ObjectId(id)
    user = users_collection.find_one({"_id": object_id})
    if user:
        user['_id'] = str(user['_id'])
        user['userId'] = user.pop('_id')
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{userId}")
async def delete_user(userId: str):
    object_id = ObjectId(userId)
    deletion_result = users_collection.delete_one({"_id": object_id})
    if deletion_result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
# PUT
@router.put("/users/{userId}")
async def update_user(userId: str, updated_user_data: User):
    object_id = ObjectId(userId)
    user_exist = users_collection.find_one({"_id": object_id})
    if user_exist:
        updated_user_dict = updated_user_data.model_dump(exclude_unset=True)
        users_collection.update_one({"_id": object_id}, {"$set": updated_user_dict})
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")