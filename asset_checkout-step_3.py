# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: AssetCheckout
class AssetCheckout:
    def __init__(self):
        self.records = []
    
    def add_checkout(self, receiver_name, asset_type, quantity, status="active"):
        record = {
            "id": len(self.records) + 1,
            "receiver": receiver_name,
            "asset": asset_type,
            "quantity": quantity,
            "status": status,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.records.append(record)
        return record

    def add_return(self, checkout_id):
        for i, rec in enumerate(self.records):
            if rec["id"] == checkout_id:
                if rec["status"] != "active":
                    raise ValueError("Запись не активна для возврата")
                rec["status"] = "returned"
                return True
        return False

    def get_records(self, status=None):
        if status is None:
            return self.records.copy()
        return [r for r in self.records if r["status"] == status]
