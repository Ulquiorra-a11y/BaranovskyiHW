# def sum_digits(n: int) -> int:
#     """
#     Calculates the sum of all digits in a number.
#
#     :param n: An integer number
#     :return: The sum of the digits
#     """
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits(n // 10)
#
#
# num = 43197
# print(sum_digits(num))



def sum_digits_in_dict(numbers: list) -> int:
    '''
    Calculates the sum of all numbers in a nested list.
    :param numbers: A list that may contain integers or other lists
    :return:The total sum of all integers
    '''
    total = 0

    for item in numbers:
        if isinstance(item, list):
            total += sum_digits_in_dict(item)
        else:
            total += item

    return total


nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
print(sum_digits_in_dict(nested_numbers))
