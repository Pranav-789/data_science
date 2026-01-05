from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = {datetime: lambda v: v.strftime('%d-%m-%Y %H:%M;%S')}
    )

# create a user instance

user = User(
    id = 1,
    name='pranav',
    email='pranav@email.com',
    createdAt=datetime(2024, 3, 15, 14, 30),
    address=Address(
        street = 'something 1234',
        city = 'varangoan',
        zip_code = '425305'
    ),
    is_active=True,
    tags=['premium', 'subscriber'],
)


# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict, end='\n\n')

# Using model_dump_json() -> json str

json_str = user.model_dump_json()
print(json_str)