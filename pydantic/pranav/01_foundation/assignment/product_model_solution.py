from pydantic import BaseModel

# TODO: Create Product model with id, name, price, in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True # default value

# prod = {'id': 1234, 'name': 'Cristiano Louboutin', 'price': 32000, 'in_stock': True}
prod = {'id': 1234, 'name': 'Cristiano Louboutin', 'price': 32000}

shoe1 = Product(**prod)

print(type(shoe1))
print(shoe1)