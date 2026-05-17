from datetime import datetime
from functools import total_ordering
#
#
# @total_ordering
# class Email:
#     def __init__(self, sender: str, recipient: str, subject: str, body: str, date: datetime):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body
#         self.date = date
#
#     def __str__(self):
#         return (
#             f"From: {self.sender}\n"
#             f"To: {self.recipient}\n"
#             f"Subject: {self.subject}\n"
#             f"- {self.body} -"
#         )
#
#     def __len__(self):
#         return len(self.body)
#
#     def __bool__(self):
#         return bool(self.body.strip())
#
#     def __eq__(self, other):
#         return self.date == other.date
#
#     def __lt__(self, other):
#         return self.date < other.date
#
#
#
# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e1)
# print(e2)
# print("Length:", len(e1))
# print("Has text:", bool(e1))
# print("Is newer:", e2 > e1)


class Money:
    def __init__(self, amount: float):
        self.amount = amount

    def __str__(self):
        return f"${self.amount}"

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        result = self.amount - other.amount
        return Money(max(0, result))

money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)