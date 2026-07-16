# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: AssetCheckout
def archive_records(records, keep_days=365):
    """Archive records older than keep_days or with completed status."""
    import datetime as dt
    cutoff = dt.datetime.now() - dt.timedelta(days=keep_days)
    archived = []
    for rec in records:
        if isinstance(rec['date'], str):
            d = dt.datetime.strptime(rec['date'], "%Y-%m-%d")
        else:
            d = rec['date']
        is_old = d < cutoff
        is_done = rec.get('status') in ('Returned', 'Cancelled', 'Expired')
        if is_old or is_done:
            archived.append(rec)
    return archived, records[:len(records)-len(archived)]
