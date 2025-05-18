class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Customer name must be a string")
        if len(name) > 15:
            raise ValueError("Customer name cannot exceed 15 characters")
        self.name = name

    def orders(self):
        from coffee_shop.order import Order
        return [order for order in Order.all_orders if order.customer is self]

    def coffees(self):
        from coffee_shop.order import Order
        coffees = {order.coffee for order in self.orders()}
        return list(coffees)

    def create_order(self, coffee, price):
        from coffee_shop.order import Order
        from coffee_shop.coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("create_order expects a Coffee instance")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee_shop.order import Order
        if not hasattr(coffee, "name"):
            raise ValueError("Argument must be a Coffee instance")
        spending = {}
        for order in Order.all_orders:
            if order.coffee is coffee:
                spending[order.customer] = spending.get(order.customer, 0) + order.price
        if not spending:
            return None
        return max(spending, key=spending.get)


