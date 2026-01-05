# A simple database class
class DataBase:
    def connect(self):
        return 'Connected to Database'
    

# Service class that depends on a database
class Service:
    def __init__(self):
        # ❌ Tight Coupling:
        # The Service class is creating its own instance of DataBase.
        # This means Service is now **tightly bound to this specific DataBase implementation**.
        # Problems with tight coupling:
        # 1. Hard to test: we cannot easily replace DataBase with a fake or mock for testing.
        # 2. Hard to maintain: changing DataBase may require editing Service class.
        # 3. Hard to extend: swapping with a different database implementation is difficult.
        self.db = DataBase()  # tight coupling

    def get_data(self):
        # Uses the database instance created inside the class
        return self.db.connect()
    
# Creating Service instance
service = Service()

# Calling method
print(service.get_data())  # Output: 'Connected to Database'


# Tight coupling = a class creates or depends directly on a specific implementation of another class.