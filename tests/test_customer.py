import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("ThisNameIsWayTooLongToBeValid")
    with pytest.raises(ValueError):
        Customer(123)

def test_create_order_and_relationships():
    Order.all_orders.clear()
    c = Customer("Alice")
    coffee = Coffee("Espresso")
    order = c.create_order(coffee, 3.5)

    assert order.customer is c
    assert order.coffee is coffee
    assert order in c.orders()
    assert coffee in c.coffees()

def test_most_aficionado():
    Order.all_orders.clear()
    c1 = Customer("Bob")
    c2 = Customer("Sue")
    coffee = Coffee("Latte")

    c1.create_order(coffee, 5)
    c1.create_order(coffee, 10)
    c2.create_order(coffee, 8)

    assert Customer.most_aficionado(coffee) is c1

