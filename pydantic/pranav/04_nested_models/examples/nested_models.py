from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None ## this is forward referencing
    ## Replies are comments in themselves


Comment.model_rebuild() ## necessary for forward referencing

address = Address(
    street='123 something',
    city= 'Varangaon',
    postal_code='4253005'
)

user = User(
    id = 1,
    name = 'Pranav',
    address = address
)

comment = Comment(
    id = 1,
    content = 'First Comment',
    replies=[
        Comment(id=2, content="reply1"),
        Comment(id=3, content="reply2"),
    ]
)