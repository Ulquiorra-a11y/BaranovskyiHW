# def is_did_prime(n):
#     if n <= 1:
#         return False
#
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# n = int(input("Число: "))
# if is_did_prime(n):
#     print(f"Число {n} является простым")
# else:
#     print(f"Число {n} не является простым")



# def filter_numbers(filtered, *args):
#     if filtered == 'odd':
#         return [x for x in args if x % 2 != 0]
#     elif filtered == 'even':
#         return [x for x in args if x % 2 == 0]
#     else:
#         return 'Некорректный фильтр'
#
# print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
# print(filter_numbers("odd", 10, 15, 20, 25))
# print(filter_numbers("prime", 2, 3, 5, 7))


def merge_dicts(*dict_args):
    result = {}

    for dictionary in dict_args:
        result.update(dictionary)
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
print(merge_dicts(dict1, dict2, dict3))