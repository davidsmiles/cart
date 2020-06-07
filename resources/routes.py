from resources.carts import AddToCart, AllCarts


def initialize_routes(api):
    api.add_resource(AddToCart, '/cart')
    api.add_resource(AllCarts, '/carts')