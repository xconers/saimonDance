# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: AssetCheckout
def monthly_stats(records):
    from collections import defaultdict, Counter
    stats = {}
    for r in records:
        date_str = r["date"]
        month = date_str[:7]  # "YYYY-MM"
        if month not in stats:
            stats[month] = {"issued": [], "returned": []}
        status = r.get("status", "")
        if status == "active":
            stats[month]["issued"].append(r)
        elif status == "returned":
            stats[month]["returned"].append(r)
    return {m: Counter(d["asset"] for d in s["issued"]) + Counter(d["asset"] for d in s["returned"]) for m, s in stats.items()}
