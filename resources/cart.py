from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from database.models import Carts, Product
from libs.errors import *


class Cart(Resource):

    @classmethod
    @jwt_required
    def get(cls):

        user_id = get_jwt_identity()
        data = request.get_json()

        user_cart = Carts.objects(user_id=user_id).first()

        if not user_cart:
            raise UserCartEmpty

        return jsonify(user_cart)


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

        product = user_cart(products__id=data['id'])
        if product:         # Product already exists
            index = 0
            for each in user_cart.first().products:
                if each.id == data['id']:
                    break
                index += 0

            user_cart.update_one(**{f'set__products__{index}': Product(**data)})
            return {}, 200
        
        user_cart.update_one(push__products=data)
        return {}, 200


    @classmethod
    @jwt_required
    def delete(cls):
        
        user_id = get_jwt_identity()
        product_id = request.args['product-id']
        
        user_cart = Carts.objects(user_id=user_id)

        exists = user_cart(products__id=product_id)
        if exists:
            products =  user_cart.first().products

            found = [product for product in products if product.id == product_id][0]

            user_cart.update_one(pull__products=found)

            return {}, 200
        
        raise ProductNotInCart