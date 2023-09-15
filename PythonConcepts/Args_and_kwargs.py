def order_pizza(size, *toppings, **details):
    print(f"ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print(details)

order_pizza("large", "pepperoni", "olives", delivery=True, tip=5)
