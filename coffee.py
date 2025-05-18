class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Coffee name must be a string")
        self.name = name

    def orders(self):
        from coffee_shop.order import Order
        return [order for order in Order.all_orders if order.coffee is self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

