# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: AssetCheckout
def generate_summary():
    """Generate a concise summary of current asset checkout data."""
    if not all_data:
        print("No data available.")
        return
    
    today = datetime.now().date()
    
    active_checkouts = [item for item in all_data if item['status'] == 'active' and (today - item.get('checkout_date', today)).days <= 30]
    overdue_checkouts = [item for item in active_checkouts if (today - item.get('checkout_date', today)).days > 30]
    
    print(f"Total items: {len(all_data)}")
    print(f"Active checkouts: {len(active_checkouts)}")
    print(f"Overdue checkouts: {len(overdue_checkouts)}")
    
    if active_checkouts:
        most_used = max(set(item['equipment'] for item in all_data), key=list(all_data).count)
        print(f"Most frequently checked out equipment: {most_used}")
    
    return

generate_summary()
