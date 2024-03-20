from pydantic import BaseModel
from typing import List, Optional

class Result(BaseModel):
    exam_name: Optional[str]
    score: Optional[float]
    
class User(BaseModel):
    user_id: str
    user_type: str
    test: int
    username: str
    firstname: str
    lastname: str
    middle_initial: str
    age: int
    email: str
    gender: str
    school: str
    password: str
    pretest_results: List[Result] = []
    posttest_results: List[Result] = []
    
class UserUpdate(BaseModel):
    username: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    middle_initial: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    school: Optional[str] = None
    password: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str
