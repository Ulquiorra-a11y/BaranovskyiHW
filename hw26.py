import sys
import os

# path = sys.argv[1]
#
# for item in os.listdir(path):
#     full_path = os.path.join(path, item)
#
#     if os.path.isdir(full_path):
#         print("Папка:", item)
#     else:
#         print("Файл:", item)



import sys
import os

if len(sys.argv) != 3:
    print("Использование: python script.py <путь> <расширение>")
    exit()

path = sys.argv[1]
extension = sys.argv[2]

found_files = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(extension):
            full_path = os.path.join(root, file)
            found_files.append(full_path)

if not found_files:
    print("Файлы не найдены")
    exit()

print("Найденные файлы:")
for f in found_files:
    print(f)

answer = input("Удалить эти файлы? (y/n): ")

if answer.lower() == "y":
    for f in found_files:
        os.remove(f)
    print("Файлы удалены")
if answer.lower() == "n":
    print("Удаление отменено")
else:
    print("Введите запрос по новой")