from pydantic import BaseModel
from typing import List, Optional

class PreTest(BaseModel):
    category: str
    question_text: str
    question_image: Optional[str]
    options: Optional[List[str]]
    option_images: Optional[List[str]]
    correct_option_index: int
    
