# === Stage 45: Добавь восстановление из резервной копии ===
# Project: AssetCheckout
def restore_from_backup(backup_path: str) -> None:
        """Восстанавливает данные из резервной копии.
        
        Резервная копия — это JSON-файл, созданный функцией backup_to_file.
        Функция перезаписывает текущее состояние данных из файла.
        """
        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            data['items'] = data.get('items', [])
            data['users'] = data.get('users', [])
            data['transactions'] = data.get('transactions', [])
            data['settings'] = data.get('settings', {})
        except FileNotFoundError:
            print(f"Резервная копия не найдена: {backup_path}")
            return
        except json.JSONDecodeError:
            print("Резервная копия повреждена или не является корректным JSON-файлом")
            return
        print(f"Резервная копия успешно восстановлена из {backup_path}")
