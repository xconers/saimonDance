# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: AssetCheckout
class AssetCheckoutError(Exception): pass

def validate_user_input(name: str, asset_id: int, date_str: str) -> dict:
    if not name or len(name.strip()) < 2:
        raise AssetCheckoutError("Имя получателя должно быть не пустым и содержать минимум 2 символа.")
    try:
        asset_int = int(asset_id)
        if asset_int <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        raise AssetCheckoutError(f"ID оборудования должен быть положительным целым числом, получено: {asset_id}")

    from datetime import datetime
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date > datetime.now():
            raise ValueError()
    except (ValueError, TypeError):
        raise AssetCheckoutError(f"Дата '{date_str}' должна быть в формате 'YYYY-MM-DD' и не может быть в будущем.")

    return {"name": name.strip(), "asset_id": asset_int, "checkout_date": date}
