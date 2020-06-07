from flask_restful import HTTPException
from libs.strings import gettext

class UserCartEmpty(HTTPException):
    pass

class ProductNotInCart(HTTPException):
    pass


class QueryInvalidError(HTTPException):
    pass


class InternalServerError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


errors = {
    "UserCartEmpty": {
        "message": gettext('user_cart_is_empty'),
        "status": 204
    },
    "ProductNotInCart": {
        "message": gettext('product_not_in_cart'),
        "status": 400
    },
    "QueryInvalidError": {
        "message": gettext('unexpected_user_data'),
        "status": 500
    },
    "InternalServerError": {
        "message": "Oops, something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    }
}