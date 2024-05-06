from pydantic import BaseModel
from typing import List, Optional

class Result(BaseModel):
    exam_name: Optional[str]
    score: Optional[float]
    
class User(BaseModel):
    userId: Optional[str] = None
    status: Optional[str] = None
    userType: Optional[str] = None
    test: Optional[str] = None
    avatar: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    middleName: Optional[str] = None
    username: Optional[str] = None
    gender: Optional[str] = None
    birthdate: Optional[str] = None
    houseNumber: Optional[str] = None
    street: Optional[str] = None
    sps: Optional[str] = None
    barangay: Optional[str] = None
    municipality: Optional[str] = None
    fatherName: Optional[str] = None
    fatherNumber: Optional[str] = None
    motherName: Optional[str] = None
    motherNumber: Optional[str] = None
    guardianName: Optional[str] = None
    guardianNumber: Optional[str] = None
    email: Optional[str] = None
    pretest_results: List[Result] = []
    posttest_results: List[Result] = []

class LoginRequest(BaseModel):
    username: str
