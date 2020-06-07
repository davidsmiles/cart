from extensions import db



class Product(db.EmbeddedDocument):

    id = db.StringField() 
    price = db.FloatField()
    quantity = db.IntField()
    total = db.FloatField()


class Carts(db.Document):
    user_id = db.StringField(required=True)
    status = db.StringField(max_length=10)
    products = db.ListField(db.EmbeddedDocumentField(Product), default=list)
    subtotal = db.IntField(default=0)

    meta = {
        'indexes': ['user_id']
    }