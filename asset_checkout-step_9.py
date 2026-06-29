# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: AssetCheckout
import json, sys, os
from datetime import datetime

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив записей.")
        
        records = []
        for item in data:
            rec_id = item.get('id') or len(records) + 1
            recipient_name = item.get('recipient', {}).get('name', 'Unknown')
            
            record = {
                "id": rec_id,
                "equipment_type": item.get("type", "General"),
                "issue_date": datetime.fromisoformat(item["issue_date"]),
                "return_date": None if not item.get("returned") else datetime.fromisoformat(item["return_date"]),
                "status": "issued" if not item.get("returned") else "returned",
                "condition": item.get("condition", "Good"),
                "recipient_name": recipient_name,
                "notes": item.get("notes", ""),
            }
            records.append(record)
        
        print(f"[INFO] Загружено {len(records)} записей из JSON.")
        return {"records": records}
    except json.JSONDecodeError as e:
        sys.stderr.write(f"[ERROR] Неверный формат JSON: {e}\n")
        raise
