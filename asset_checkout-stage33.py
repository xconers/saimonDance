# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: AssetCheckout
import json, random
from datetime import date, timedelta

def rollback_last_checkout():
    """Откат последнего чек-аута: возвращает оборудование, обновляет статусы и логирует действие."""
    with open("asset_checkout_state.json", "r") as f:
        state = json.load(f)

    if not state["checkouts"]:
        print("Нет активных чек-аутов для отката.")
        return

    checkout = state["checkouts"][-1]
    receiver_id = checkout["receiver_id"]
    asset_id = checkout["asset_id"]
    checkout_date = checkout["checkout_date"]
    checkout_user = checkout.get("user", "system")

    # Обновляем статус оборудования
    for asset in state["assets"]:
        if asset["asset_id"] == asset_id:
            asset["status"] = "available"
            asset["checkout_date"] = None
            asset["checkout_user"] = None
            break

    # Возвращаем статус получателя
    for receiver in state["receivers"]:
        if receiver["id"] == receiver_id:
            receiver["status"] = "idle"
            break

    # Удаляем запись о чек-ауте
    state["checkouts"] = state["checkouts"][:-1]

    # Логируем откат
    state["history"].append({
        "action": "rollback_checkout",
        "asset_id": asset_id,
        "receiver_id": receiver_id,
        "checkout_date": checkout_date,
        "user": checkout_user,
        "timestamp": date.today().isoformat()
    })

    with open("asset_checkout_state.json", "w") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    print(f"Откат чек-аута: оборудование {asset_id} возвращено получателю {receiver_id} от {checkout_date}.")
