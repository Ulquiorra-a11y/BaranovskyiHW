# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
# print(set1.issuperset(set2))
# print(set1 >= set2)

# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
# result = True
# for x in set2:
#     if x not in set1:
#         result = False
#         break
# print(result)

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}
if set2.issubset(set1):
    print("Подмножество:", True)
    print("Разница:", set1 - set2)
elif set2.issubset(set1):
    print("Подмножество:", True)
    print("Разница:", set2 - set1)
else:
    print("Подмножество:", False)