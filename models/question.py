from pydantic import BaseModel
from typing import List, Optional

class Pretest(BaseModel):
    pretest_id: Optional[str] = None
    category: Optional[str] = None
    question_text: Optional[str] = None
    question_image: Optional[str] = None
    question_sound: Optional[str] = None
    options: Optional[List[str]] = None
    option_images: Optional[List[str]] = None
    correct_option_index: Optional[int] = None
    
class PretestUpdate(BaseModel):
    question_text: Optional[str] = None
    question_image: Optional[str] = None
    question_sound: Optional[str] = None
    options: Optional[List[str]] = []
    option_images: Optional[List[str]] = []
    
class Posttest(BaseModel):
    posttest_id: Optional[str] = None
    category: Optional[str] = None
    question_text: Optional[str] = None
    question_image: Optional[str] = None
    question_sound: Optional[str] = None
    options: Optional[List[str]] = None
    option_images: Optional[List[str]] = None
    correct_option_index: Optional[int] = None
    
class PosttestUpdate(BaseModel):
    question_text: Optional[str] = None
    question_image: Optional[str] = None
    question_sound: Optional[str] = None
    options: Optional[List[str]] = []
    option_images: Optional[List[str]] = []