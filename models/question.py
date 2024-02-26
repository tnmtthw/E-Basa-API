from pydantic import BaseModel
from typing import List, Optional

class Hugis(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int

class Kulay(BaseModel):
    question_text: str
    question_image: Optional[str]
    options: Optional[List[str]]
    option_images: Optional[List[str]]
    correct_option_index: int
    
class Numero(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int
    
class Binasa(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int

class Napakinggan(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int
    
class Ponolohiya(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int
    
class Talasalitaan(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int

class Gramatika(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int


