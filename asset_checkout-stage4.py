# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: AssetCheckout
def edit_checkout_record(record_id, new_data):
    if not isinstance(new_data, dict) or 'receiver' not in new_data:
        raise ValueError("new_data must contain at least 'receiver'")
    
    for i, record in enumerate(checkout_history):
        if record['id'] == record_id:
            checkout_history[i] = {**record, **new_data}
            print(f"Record #{record_id} updated successfully.")
            return True
    
    print(f"No record found with ID: {record_id}")
    return False
