# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: AssetCheckout
def weekly_stats(records):
    """Расчёт недельной статистики: количество выдач, возвратов и активных за неделю."""
    week_key = lambda r: (r['date'] - datetime.date(2024, 1, 1)).isocalendar()[:2]
    stats = {}
    for rec in records:
        key = week_key(rec)
        if key not in stats:
            stats[key] = {'issued': 0, 'returned': 0}
        if rec['status'] == 'issued':
            stats[key]['issued'] += 1
        elif rec['status'] == 'returned':
            stats[key]['returned'] += 1
    return stats
