# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: AssetCheckout
import json, os

DATA_FILE = "assets_data.json"

def save_to_json(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Не удалось сохранить данные в {DATA_FILE}: {e}")
        return False

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return {"receivers": [], "assets": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстанавливаем структуру по умолчанию, если файл повреждён или пустой
        if not isinstance(data, dict):
            return {"receivers": [], "assets": []}
        return {
            "receivers": data.get("receivers", []),
            "assets": data.get("assets", [])
        }
    except Exception:
        return {"receivers": [], "assets": []}

def init_data_store():
    existing = load_from_json()
    # Сохраняем текущее состояние в файл при старте, если это первый запуск или данные изменились
    save_to_json(existing)
