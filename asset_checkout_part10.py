# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: AssetCheckout
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "assets": [
            {
                "id": a["id"],
                "name": a["name"],
                "status": a["status"],
                "issued_to": a.get("issued_to"),
                "issue_date": a.get("issue_date"),
                "return_date": a.get("return_date")
            } for a in assets_list
        ],
        "receivers": {r["name"]: r["contact"] for r in receivers_list},
        "inventory_count": len(assets_list)
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
