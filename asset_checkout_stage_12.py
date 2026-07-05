# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: AssetCheckout
import json, os, sys

def load_data(file_path):
    if not os.path.exists(file_path):
        print(f"Ошибка: файл {file_path} не найден.")
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            print(f"Загружено {len(data)} записей из {file_path}.")
            return data
        else:
            raise ValueError("Неверный формат JSON: ожидается массив.")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []

if __name__ == "__main__":
    file = sys.argv[1] if len(sys.argv) > 1 else "assets.json"
    records = load_data(file)
