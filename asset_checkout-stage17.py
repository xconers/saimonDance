# === Stage 17: Добавь группировку записей по категориям ===
# Project: AssetCheckout
def group_records_by_category(records):
    """Группирует записи выдач по категории оборудования."""
    grouped = {}
    for rec in records:
        cat = rec.get('category', 'Неизвестно')
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(rec)
    return grouped
