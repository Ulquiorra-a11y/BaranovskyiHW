# def stringify_data(data: list) -> str:
#     '''
#     Takes a list of data and returns its string representation, concatenated with " | "
#     :param data:List of elements of any type
#     :return:A string with elements joined by " | "
#     '''
#     return " | ".join(str(item) for item in data)
#
#
# data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
#
# print(stringify_data(data))



def total_score(data: list[dict[str, list[int]]]) -> int:
    '''
    Calculates the total sum of all scores from a list of user
    :param data:A list of dictionaries with user data and their scores
    :return:The total sum of all scores
    '''
    total = 0
    for user in data:
        total += sum(user["scores"])

    return total


data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

print(total_score(data))