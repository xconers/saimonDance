# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: AssetCheckout
def backup_data_file(path: str, backup_dir: str = "backups") -> str:
    """Сохраняет копию файла данных с временной меткой в backup_dir/ и возвращает путь к копии."""
    import os, shutil
    os.makedirs(backup_dir, exist_ok=True)
    filename = os.path.basename(path)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{filename}.backup_{timestamp}")
    shutil.copy2(path, backup_path)
    return backup_path
