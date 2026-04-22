# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# item = fibonacci()
#
# for _ in range(12):
#     print(next(item))


data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

def unique_numbers(data):
    lines = []

    for item in data:
        if item not in lines:
            lines.append(item)
            yield item


num = unique_numbers(data)

for x in num:
    print(x)