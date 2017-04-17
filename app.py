from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 19.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    pass

@app.route('/store/<string:name>')
def get_store(name):
    pass

@app.route('/store')
def get_stores(name):
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

@app.route('/store/<string:name>/item', methods=['POST'])
def get_items_in_store(name):
    pass

app.run(port=5000)
