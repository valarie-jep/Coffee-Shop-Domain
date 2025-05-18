class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from coffee_shop.customer import Customer
        from coffee_shop.coffee import Coffee
        if not isinstance(customer, Customer):
            raise ValueError("Order must have a Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("Order must have a Coffee instance")
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a number")
        self._customer = customer
        self._coffee = coffee
        self.price = price
        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee


