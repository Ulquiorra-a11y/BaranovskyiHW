# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# res = []
# x = " "
# for item in text_list:
#     if x not in item:
#         res.append(item.lower())
# print(res)

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = 17
print(f"{'Товар':10} {'Старая цена':15} {'Новая цена':10}")
for item in products:
    name, price = item
    new_price = price-discount*price/100
    item.append(new_price)
    print(f"{name:10} {price:>10.2f}$ {new_price:>13.2f}$")
