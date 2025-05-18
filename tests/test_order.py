from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_order_properties():
    Order.all_orders.clear()
    c = Customer("Ann")
    coffee = Coffee("Americano")
    order = Order(c, coffee, 4.25)

    assert order.customer is c
    assert order.coffee is coffee
    assert order.price == 4.25
