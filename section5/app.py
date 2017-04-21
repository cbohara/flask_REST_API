from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'charlie'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    @jwt_required()
    def get(self, name):
        item = [item for item in items if item['name'] == name]
        return {'item': item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if [item for item in items if item['name'] == name]:
            return {'message': "An item with name " + name + " already exists"}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    @jwt_required()
    def delete(self, name):
        global items
        items = [item for item in items if item['name'] != name]
        return {'message': 'item deleted'}

    @jwt_required()
    def put(self, name):
        global items

        data = Item.parser.parse_args()

        item = [item for item in items if item['name'] == name]

        if not item:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            items = [item for item in items if item['name'] != name]
            item = {'name': name, 'price': data['price']}
            items.append(item)

        return item


class ItemList(Resource):
    def get(self):
        return items


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


app.run(port=5000, debug=True)
