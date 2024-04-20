from pydantic import BaseModel
from typing import List, Optional

class Result(BaseModel):
    exam_name: Optional[str]
    score: Optional[float]
    
class User(BaseModel):
    userId: Optional[str] = None
    status: str
    userType: str
    test: int
    avatar: str
    firstName: str
    lastName: str
    middleName: str
    username: str
    gender: str
    birthdate: str
    houseNumber: str
    street: str
    sps: str
    barangay: str
    municipality: str
    fatherName: str
    fatherNumber: str
    motherName: str
    motherNumber: str
    guardianName: str
    guardianNumber: str
    email: str
    pretest_results: List[Result] = []
    posttest_results: List[Result] = []

class LoginRequest(BaseModel):
    username: str
