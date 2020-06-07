from flask import Response
from flask_restful import Resource


class AllCarts(Resource):

    @classmethod
    def get(cls):
        carts = Carts.objects().to_json()
        return Response(carts, content_type='application/json', status=200)