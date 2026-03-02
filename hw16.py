# grades = [5, 3, 4, 2, 1, 5, 3]
# res = [[grade, 'отлично' if grade == 5 else 'хорошо' if grade >= 3 else 'неудовлетворительно'] for grade in grades]
# print(res)

string = "([({}()){}])"
stack = []
valid = True
for i in string:
    if i in "({[":
        stack.append(i)
    elif i in ")}]":
        if not stack:
            valid = False
            break
        res = stack.pop()
        if (res == '(' and i != ')') or (res == '[' and i != ']') or (res == '{' and i != '}'):
            valid = False
            break
if stack:
    valid = False
print("Скобки:", string)
print("Валидны:", valid)