import uuid
import datetime


class Expense:
    def __init__(self, date: datetime, category: str, description: str, amount: float) -> None:
        self.id = str(uuid.uuid4())
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return (f"Expense: {self.id} = Date: {self.date}, "
                f"Amount: {self.amount}, Category: {self.category}, Description: {self.description}")
