from ninja import NinjaAPI
from ..blog.models import Category, Post

api = NinjaAPI()

@api.get("")
def hello(request, name: str = "Ninja"):
    return f'Hello {name}'
    