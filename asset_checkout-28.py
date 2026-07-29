# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: AssetCheckout
def print_metrics(records):
    if not records:
        print("Нет данных.")
        return
    total = len(records)
    active = sum(1 for r in records if r['status'] == 'active')
    returned = sum(1 for r in records if r['status'] == 'returned')
    overdue = 0
    now = datetime.now()
    for r in records:
        if r['status'] == 'active' and r.get('issue_date'):
            try:
                due = datetime.strptime(r['issue_date'], '%Y-%m-%d %H:%M').replace(microsecond=0)
                if now > due:
                    overdue += 1
            except ValueError:
                pass
    avg_days = sum((r.get('issue_date') and r.get('return_date')) and (
        datetime.strptime(r['return_date'], '%Y-%m-%d %H:%M').replace(microsecond=0) -
        datetime.strptime(r['issue_date'], '%Y-%m-%d %H:%M').replace(microsecond=0)).days
        for r in records if r.get('issue_date') and r.get('return_date')) / returned if returned else 0
    print(f"Общий: {total} | Активны: {active} | Возвращены: {returned} | Просрочено: {overdue}")
    if avg_days > 0:
        print(f"Среднее время использования: {avg_days:.1f} дн.")
