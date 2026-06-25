# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: AssetCheckout
def filter_assets(status=None, category=None, tags=None):
    filtered = []
    for record in assets:
        match_status = status is None or record['status'] == status
        match_category = category is None or record.get('category') == category
        match_tags = tags is None or any(tag in record.get('tags', []) for tag in tags)
        if match_status and match_category and match_tags:
            filtered.append(record)
    return filtered
