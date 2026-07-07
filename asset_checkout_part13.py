# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: AssetCheckout
def search_records(query: str) -> list[dict]:
    """Поиск записей по нескольким полям без учёта регистра."""
    if not query:
        return []
    q = query.strip().lower()
    results = []
    for record in records:
        text = (
            f"{record.get('id', '')} "
            f"{record.get('equipment_name', '')} "
            f"{record.get('recipient_name', '')} "
            f"{record.get('issue_date', '')} "
            f"{record.get('return_date', '')} "
            f"{record.get('status', '')}"
        )
        if q in text.lower():
            results.append(record)
    return results
