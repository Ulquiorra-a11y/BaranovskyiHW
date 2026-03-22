# orders = [
#     {"product": "Laptop", "price": 1200},
#     {"product": "Mouse", "price": 50},
#     {"product": "Keyboard", "price": 100},
#     {"product": "Monitor", "price": 300},
#     {"product": "Chair", "price": 800},
#     {"product": "Desk", "price": 400}
#
# ]
# def expensive_products(orders):
#     expensive_product = filter(lambda order: order["price"] > 500, orders)
#     name = map(lambda order: order["product"], expensive_product)
#     return sorted(name)
# print(expensive_products(orders))

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

earning = {name: quantity * price for name, quantity, price in sales}
result = dict(sorted(earning.items(), key=lambda x: x[1], reverse=True))

print(result)