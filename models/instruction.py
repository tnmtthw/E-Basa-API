from pydantic import BaseModel
from typing import List, Optional

class PretestInstruction(BaseModel):
    instructionID: Optional[str] = None
    title: str
    body: str
    
