from extensions import db


 class Carts(db.Document):

     _users_id = db.String(required=True)
     status = db.String(max_length=10)
     products = db.ListField()
     sub_total = db.IntField(default=0)
