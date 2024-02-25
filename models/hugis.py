from pydantic import BaseModel
from typing import List

class Hugis(BaseModel):
    question_text: str
    options: List[str]
    correct_option_index: int
