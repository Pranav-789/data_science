from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        # v is  value to be evauated
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
    # field_validator runs before pydantic

class SignUpData(BaseModel):
    password: str
    confirmPassword: str

    @model_validator(mode='after') #runs after all validation are executed(field_validators)
    def password_match(cls, values): # values here act as self
        if values.password != values.confirmPassword:
            raise ValueError('Passwords do not match')
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self)->float:
        return self.price*self.quantity # a new property will be added