from flask import request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from database.models import Carts


class AddToCart(Resource):
    
    @classmethod
    @jwt_required
    def post(cls):
        
        user_id = get_jwt_identity()
        data = request.get_json()

        user_cart = Carts.objects(user_id=user_id)

        if not user_cart:
            # Create new Cart
            cart = Carts(user_id=user_id)
            cart.save()

            return "created"

        user_cart.update_one(push__products=data)

        return "aDDED"


class AllCarts(Resource):

    @classmethod
    def get(cls):
        carts = Carts.objects().to_json()
        return Response(carts, content_type='application/json', status=200)