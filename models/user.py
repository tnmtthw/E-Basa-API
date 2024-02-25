from pydantic import BaseModel
from typing import List, Optional

class Result(BaseModel):
    exam_name: Optional[str]
    score: Optional[float]
    date_taken: Optional[str]

class User(BaseModel):
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

class LoginRequest(BaseModel):
    username: str
    password: str
