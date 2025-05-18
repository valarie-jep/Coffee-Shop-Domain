from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_coffee_orders_and_customers():
    Order.all_orders.clear()
    c1 = Customer("Bob")
    c2 = Customer("Sue")
    coffee = Coffee("Cappuccino")

    Order(c1, coffee, 4.5)
    Order(c2, coffee, 5.0)

    assert len(coffee.orders()) == 2
    assert c1 in coffee.customers()
    assert c2 in coffee.customers()

def test_num_orders_and_average_price():
    Order.all_orders.clear()
    c = Customer("Tom")
    coffee = Coffee("Mocha")

    Order(c, coffee, 3.0)
    Order(c, coffee, 6.0)

    assert coffee.num_orders() == 2
    assert coffee.average_price() == 4.5


