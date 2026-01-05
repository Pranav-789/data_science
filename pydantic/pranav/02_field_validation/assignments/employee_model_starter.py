from pydantic import BaseModel, Field
from typing import Optional


# TODO: Create Employee model
# Fields:
# - id: int
# - name: str (min 3 chars)
# - department: optional str (default 'General')
# - salary: float (must be >= 10000)


class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=50, description="Employee name", examples='Pranav Zambare') # ... is a required field
    department: Optional[str] = 'General'
    salary: float = Field(..., ge=10000) # ge is a comparator which take value and validate that the incoming val should be greater tham value