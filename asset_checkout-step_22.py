# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: AssetCheckout
def check_overdue_reminders(checkouts, now=None):
    if now is None:
        now = datetime.now()
    overdue = []
    for checkout in checkouts:
        if checkout['status'] != 'checked_out':
            continue
        due_date = datetime.fromisoformat(checkout['expected_return'])
        if now >= due_date and (now - due_date).days <= 30:
            reminder_text = f"Reminder: {checkout['recipient']} should return '{checkout['asset']}' by {due_date.strftime('%Y-%m-%d')}"
            overdue.append({**checkout, 'reminder': reminder_text})
    return overdue
