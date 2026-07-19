# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: AssetCheckout
def remind_due(checkouts, today=None):
    if today is None:
        today = datetime.date.today()
    overdue = []
    for c in checkouts:
        if c['due'] and c['due'].date() <= today:
            overdue.append((c['id'], c['due'].strftime("%Y-%m-%d"), c['recipient']))
    return overdue

def remind_pending(checkouts, days_ahead=30):
    from datetime import timedelta
    if today is None:
        today = datetime.date.today()
    upcoming = []
    for c in checkouts:
        if c.get('due') and (today + timedelta(days=days_ahead)) >= c['due'].date():
            upcoming.append((c['id'], c['due'].strftime("%Y-%m-%d"), c['recipient']))
    return upcoming

def show_reminders(checkouts, today=None):
    overdue = remind_due(checkouts, today)
    pending = remind_pending(checkouts, 30) if today else []
    if not overdue and not pending:
        print("Все чек-ауты в порядке.")
        return
    print(f"СРОЧНО ({len(overdue)}):")
    for item in overdue:
        print(f"  #{item[0]} до {item[1]} — {item[2]}")
    if pending:
        print(f"\nПлановые ({len(pending)}):")
        for item in pending:
            print(f"  #{item[0]} до {item[1]} — {item[2]}")

def add_reminder_to_checkout(checkouts, checkout_id, days_ahead=30):
    from datetime import timedelta
    today = datetime.date.today()
    target_date = today + timedelta(days=days_ahead)
    for c in checkouts:
        if c['id'] == checkout_id:
            c['due'] = target_date
            return {"status": "ok", "message": f"Напоминание установлено до {target_date.strftime('%Y-%m-%d')}"}
    return {"status": "error", "message": "Чек-аут не найден"}

if __name__ == "__main__":
    # Пример использования:
    checkouts = [
        {"id": 1, "recipient": "Иванов И.И.", "item": "Ноутбук", "status": "active", "due": datetime.date(2025, 7, 1)},
        {"id": 2, "recipient": "Петров П.П.", "item": "Монитор", "status": "active", "due": None},
    ]
    print(show_reminders(checkouts))
