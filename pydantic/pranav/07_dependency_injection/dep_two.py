# Database class (dependency)
class Database:
    def connect(self):
        return "Connected to Database"
    
# Service class that depends on a database
class Service:
    # ✅ Constructor Injection:
    # The Database instance is passed in from outside, instead of creating it internally.
    # This decouples Service from Database and allows flexibility.
    def __init__(self, db: Database):
        self.db = db
    
    def get_data(self):
        # Uses the injected Database instance
        return self.db.connect()
    
# Create a Database instance (can be real or fake)
db = Database()

# Inject the dependency into Service
service = Service(db)

# Call the method
print(service.get_data())  # Output: "Connected to Database"
