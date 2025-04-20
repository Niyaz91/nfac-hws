from models import Purchase

class PurchasesRepository:
    def __init__(self):
        self.purchases = []

    def add_purchase(self, user_id: str, flower_id: int):
        self.purchases.append(Purchase(user_id, flower_id))

    def get_user_purchases(self, user_id: str):
        return [p for p in self.purchases if p.user_id == user_id]
