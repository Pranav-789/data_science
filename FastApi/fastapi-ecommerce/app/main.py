from fastapi import FastAPI, HTTPException, Query
from service.products import get_all_products
from pydantic import BaseModel

app = FastAPI()


## static route
@app.get('/')
def root():
    return {'message': 'Welcome to FastApi'}


## dynamic route
# @app.get('/products/{id}')
# def get_products(id: int):
#     products = ['Brush', 'Laptop', 'Mouse', 'Monitor']
#     if id < 0 or id >= len(products):
#         raise HTTPException(
#             status_code=404,
#             detail="Product not found"
#         )
#     return {'product': products[id]}

# @app.get('/products')
# def get_products():
#     return get_all_products()

@app.get('/products')
def list_products(
    name: str = Query(
        default=None,
        min_length=1,
        max_length=50,
        description="Search by product name (case insensitive)"
    ),
    sort_by_price:bool = Query(
        default=False,
        description="Sort products by price"
    ),
    order: str = Query(default="asc", description="Sort order when sort_by_price=true (asc, desc)"),
    limit: int = Query(
        default=5,
        ge=1,
        le=100,
        description="Number of items to return"
    )
):
    products = get_all_products()

    if name:
        needle = name.strip().lower()
        prods = [p for p in products if needle in p.get('name', "").lower()]

        if not prods:
            raise HTTPException(
                status_code=404,
                detail=f"No product found matchin name: {name}"
            )
        
        if sort_by_price:
            reverse = order == "desc"
            prods = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)
        total = len(prods)
        prods = prods[0:limit]
        return {
            "total": total,
            "limit": limit,
            "items": prods
        }
    return {'message': 'Parameter is required for search'}
#http://localhost:8000/products?name=Xiomi


# @app.get("/products")
# def list_products(
#     name: Optional[str] = Query(
#         default=None,
#         min_length=1,
#         max_length=50,
#         description="Search by product name (case insensitive)"
#     )
# ):
#     products = get_all_products()

#     # No filter → return all products
#     if not name:
#         return {
#             "total": len(products),
#             "items": products
#         }

#     needle = name.strip().lower()
#     filtered = [
#         p for p in products
#         if needle in p.get("name", "").lower()
#     ]

#     if not filtered:
#         raise HTTPException(
#             status_code=404,
#             detail=f"No product found matching name: {name}"
#         )

#     return {
#         "total": len(filtered),
#         "items": filtered
#     }


class User(BaseModel):
    username: str
    password: str

@app.post('/user/me', response_model=User)
def return_user(user: User):
    return user