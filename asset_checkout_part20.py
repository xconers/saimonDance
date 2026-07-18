# === Stage 20: Добавь восстановление записей из архива ===
# Project: AssetCheckout
def restore_from_archive(archive_path, record_type):
    """Восстановить записи из JSON-архива обратно в список."""
    if not os.path.exists(archive_path):
        print(f"Архив не найден: {archive_path}")
        return []
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            records = [d for d in data if isinstance(d, dict)]
        else:
            records = []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Ошибка чтения архива {archive_path}: {e}")
        return []
    print(f"Восстановлено записей из архива: {len(records)}")
    return records
