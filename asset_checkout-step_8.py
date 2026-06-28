# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: AssetCheckout
def show_menu():
    print("\n=== Меню AssetCheckout ===")
    print("1. Выдать оборудование (выбрать из списка)")
    print("2. Вернуть оборудование")
    print("3. Просмотреть историю операций")
    print("4. Выход")
    choice = input("Выберите действие: ").strip()
    return choice
