import re


# text = 'The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022'
# pattern = r"\b\d{2}[./-]\d{2}[./-]\d{4}\b"
# dates = re.findall(pattern, text)
#
# for date in dates:
#     print(date)

tag_input = 'python, data_science / machine-learning; AI neural-network'
pattern = r"[;,/]"
tag = re.sub(pattern, " ", tag_input)
tags = tag.split()
print(tags)
