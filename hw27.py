import os

# filename = "system_log.txt"
# keyword = "error"
#
# if os.path.exists(filename):
#     lines = []
#     with open(filename, "r", encoding="utf=8") as f:
#         for l in f:
#             if keyword.lower() in l.lower():
#                 lines.append(l)
#
#     if lines:
#         new_filename = f"{keyword.lower()}_{filename}"
#         with open(new_filename, "w", encoding="utf-8") as new_f:
#             new_f.write("\n".join(lines))
#         print(f"Lines, with '{keyword}', saved in {new_filename}.")
#     else:
#         print("Keyword not found.")
#
# else:
#     print("File not exist.")


filename = "movies_to_watch.txt"

if os.path.exists(filename):
    unique_lines = []
    with open(filename, "r", encoding="utf=8") as f:
        for line in f:
            if line not in unique_lines:
                unique_lines.append(line)

    new_filename = "unique_movies_to_watch.txt"
    with open(new_filename, "w", encoding="utf-8") as new_f:
        new_f.write("".join(unique_lines))
    print(F"Dublicate delited. Unique film saved in {new_filename}")
else:
    print("file not exist")

