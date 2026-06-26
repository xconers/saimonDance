# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: AssetCheckout
def sort_records(records, key='date', reverse=False):
    if not records: return []
    def get_sort_key(r):
        val = r.get(key)
        if isinstance(val, str): return (0, val.lower())
        if isinstance(val, int): return (1, val)
        return (2, '')
    sorted_records = sorted(records, key=get_sort_key, reverse=reverse)
    return sorted_records

def filter_and_sort_by_date(records, date_field='date'):
    filtered = [r for r in records if r.get(date_field)]
    return sort_records(filtered, key=date_field, reverse=False)

def filter_and_sort_by_priority(records, priority_field='priority', min_val=1):
    filtered = [r for r in records if int(r.get(priority_field, 0)) >= min_val]
    return sort_records(filtered, key=priority_field, reverse=True)

def filter_and_sort_by_name(records, name_field='name'):
    filtered = [r for r in records if r.get(name_field)]
    return sort_records(filtered, key=name_field, reverse=False)
