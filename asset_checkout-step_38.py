# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: AssetCheckout
def test_error_edge_cases():
    # Тесты на ошибки и пограничные случаи
    assert checkout.is_available("laptop1") == False
    assert checkout.is_available("laptop2") == True
    assert checkout.is_available("nonexistent") == False

    # Пограничные даты: 1 января и 31 декабря
    checkout.checkout("laptop2", "test_user2", "2024-12-31")
    assert checkout.is_available("laptop2") == False
    checkout.checkout("laptop2", "test_user2", "2024-01-01")
    assert checkout.is_available("laptop2") == False

    # Попытка вернуть уже выданное оборудование
    assert checkout.return_item("laptop2") == False
    assert checkout.return_item("laptop2") == False

    # Попытка выдать уже выданное оборудование
    assert checkout.checkout("laptop2", "test_user2", "2024-06-15") == False
    assert checkout.checkout("laptop2", "test_user2", "2024-06-15") == False

    # Проверка состояния оборудования после возврата
    assert checkout.get_status("laptop2") == "available"
    assert checkout.get_status("laptop1") == "issued"
