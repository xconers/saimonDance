# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: AssetCheckout
def parse_date(date_str):
    """Парсит дату в формате DD.MM.YYYY, возвращает datetime или None."""
    if not date_str or len(date_str) != 10:
        return None
    try:
        d, m, y = date_str.split('.')
        day, month, year = int(d), int(m), int(y)
        if month < 1 or month > 12 or day < 1 or day > 31:
            return None
        import datetime as dt
        dt.datetime(year=year, month=month, day=day)
        return dt.date(year, month, day)
    except Exception:
        return None
