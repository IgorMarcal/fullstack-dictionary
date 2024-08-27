from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/items/")
def read_items():
    return [{"item_id": "Foo"}, {"item_id": "Bar"}]
