class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        store.name = store.name + " - franchise"
        return store

    @staticmethod
    def store_details(store):
        return '{}, total_stock_price: {}'.format(store.name, store.stock_price())


store = Store("Test")
amazon = Store("Amazon")
amazon.add_item("Keyboard", 160)

store_franchise = Store.franchise(store)
amazon_franchise = Store.franchise(amazon)

print(Store.store_details(amazon))
