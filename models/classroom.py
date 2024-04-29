from pydantic import BaseModel, Field
from typing import List, Optional

class Classroom(BaseModel):
    classroomId: Optional[str] = None
    name: Optional[str] = None
    capacity: Optional[str] = None
    description: Optional[str] = None
    teacherObjectId: Optional[str] = None
    students: List[Optional[str]] = Field(default_factory=list)

    