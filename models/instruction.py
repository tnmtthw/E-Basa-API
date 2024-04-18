from pydantic import BaseModel
from typing import List, Optional

class PretestInstruction(BaseModel):
    instructionId: Optional[str] = None
    title: str
    body: str
    
class UpdatePretestInstruction(BaseModel):
    title: str
    body: str
    
