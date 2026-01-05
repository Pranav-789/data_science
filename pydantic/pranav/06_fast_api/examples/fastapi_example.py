from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignUp(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "ProZero App"
    admin_email: str = 'admin@chai.com'

## We want to use setttings class as dependency

def get_settings():
    return Settings() ## Creates a new Settings object and return it

@app.post('/signup')
def signup(user: UserSignUp):
    return {'message': f'User {user.username} signed up successfully'}

@app.get('/settings')
def get_settings_endpoint(settings: Settings):
    return settings
## here fastapi(“Okay, the client must send a Settings object.”) treats settings as reequest data not internal config

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings

## Here fastapi sees settings as not a user input but calls get_settings and inject the result
## So even if the user sends a Settings object, FastAPI will IGNORE it when Depends() is used.

# Without Depends → user fills the form

# With Depends → server fills the form