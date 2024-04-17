from pydantic import BaseModel
from typing import List, Optional

class Teacher(BaseModel):
    teacherObjectId: Optional[str] = None
    userType: str
    avatar: str
    firstName: str
    lastName: str
    middleName: str
    teacherId: str
    gender: str
    username: str
    password: str
    
class LoginRequest(BaseModel):
    username: str
    password: str
