from pydantic import BaseModel
from typing import List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons

class Lesson(BaseModel):
    lesson_id: int
    topic: str

class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]

class Course(BaseModel):
    course_id: int
    name: str
    modules: List[Module]

## as we have no forward referencing, we dont need model_rebuild