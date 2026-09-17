# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: AssetCheckout
def migrate_v1():
    """Миграция: добавляем поле version в структуру данных."""
    if 'data' not in globals():
        data = {}
    if 'version' not in data:
        data['version'] = 1
    return data
