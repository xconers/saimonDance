# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: AssetCheckout
def delete_record(record_id, record_type):
    if not isinstance(record_id, int) or record_id <= 0:
        raise ValueError("ID должен быть положительным целым числом")
    
    try:
        if record_type == "borrower":
            del borrowers[record_id]
        elif record_type == "equipment":
            del equipment[record_id]
        elif record_type == "transaction":
            del transactions[record_id]
        else:
            raise ValueError(f"Неизвестный тип записи: {record_type}")
    except KeyError:
        print(f"Запись с ID {record_id} не найдена.")
