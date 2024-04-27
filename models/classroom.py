from pydantic import BaseModel
from typing import List, Optional

class Classroom(BaseModel):
    classroomId: Optional[str] = None
    name: str
    capacity: str
    description: str
    teacherObjectId: str
    students: List[Optional[str]] = [] 