from pydantic import BaseModel
from typing import List, Optional

class Pretest(BaseModel):
    pretest_id: str
    category: str
    question_text: Optional[str]
    question_image: Optional[str]
    question_sound: Optional[str]
    options: Optional[List[str]]
    option_images: Optional[List[str]]
    correct_option_index: int
    
class PretestUpdate(BaseModel):
    question_text: Optional[str] = None
    question_image: Optional[str] = None
    question_sound: Optional[str] = None
    options: Optional[List[str]] = []
    option_images: Optional[List[str]] = []