# def fibonacci() -> int:
#     '''
#     Infinite generator of Fibonacci numbers
#     :yield: Next number in the Fibonacci sequence
#     '''
#     a, b = 0, 1
#     while True:
#         if not isinstance(a, int) or not isinstance(b, int):
#             raise RuntimeError("Fibonacci values must be integers")
#         yield a
#         a, b = b, a + b
#
# item = fibonacci()
#
# for _ in range(12):
#     print(next(item))


data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

def unique_numbers(data: list[int]) -> int:
    '''
    Generator that yields unique elements from the list
    while preserving their original order.
    :param data: list of integers
    :yield:unique elements from the list
    '''

    if not isinstance(data, list):
        raise TypeError("Input must be a list")

    lines = []

    for item in data:
        if item not in lines:
            lines.append(item)
            yield item


num = unique_numbers(data)

for x in num:
    print(x)