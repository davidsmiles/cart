from resources.cart import Cart


def initialize_routes(api):
    api.add_resource(Cart, '/cart')
