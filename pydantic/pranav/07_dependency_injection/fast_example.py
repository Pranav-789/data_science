# Import FastAPI framework and Depends function for dependency injection
from fastapi import FastAPI, Depends

# Create a FastAPI application instance
app = FastAPI()

# Define a mock Database class to simulate a database connection
class Database:
    def connect(self):
        # Simulate connecting to a database
        return 'Connected to database'
    
    def disconnect(self):
        # Simulate disconnecting from the database
        return 'Disconnected from database'

# Define a dependency function to manage Database instances
def get_database():
    # Create a new Database object (setup)
    db = Database()

    try:
        # Yield the Database object to the route function
        # Everything before yield runs **before** the route is executed
        yield db
    finally:
        # Cleanup code runs **after** the route has finished
        # Ensures database disconnect is called after request
        db.disconnect()

# Define a GET route at "/chai"
@app.get("/chai")
# Inject the Database dependency using Depends
# FastAPI automatically calls get_database(), injects db, and handles cleanup
def read_chai(db = Depends(get_database)):
    # Use the Database object inside the route
    # Here we simulate a database connection and return a response
    return {'message': db.connect()}
