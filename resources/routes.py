from resources.cart import Cart
from resources.carts import AllCarts


def initialize_routes(api):
    api.add_resource(Cart, '/cart')
    api.add_resource(AllCarts, '/carts')