# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: AssetCheckout
def print_receipt(checkout: dict) -> None:
    """Выводит одну запись выдачи в компактном формате."""
    rec = checkout.get("record", {})
    if not rec:
        return
    person = rec.get("person", {}) or {}
    asset = rec.get("asset", {}) or {}
    print(f"--- Выдача #{rec.get('id', '?')} ---")
    print(f"  Получатель: {person.get('name', '???')} ({person.get('phone', '')})")
    print(f"  Оборудование: {asset.get('model', '???')}, сер.№ {asset.get('serial', '')}")
    print(f"  Дата выдачи: {rec.get('checkout_date', '-')}")
    status = rec.get("status", "unknown")
    print(f"  Статус: {'В выдаче' if status == 'issued' else 'На руках' if status == 'returned' else status}")
    notes = rec.get("notes", "")
    if notes:
        print(f"  Примечание: {notes}")
