# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: AssetCheckout
def reset_demo_data():
    """Сбросить все демо-данные в исходное состояние."""
    for obj in list(globals().values()):
        if callable(obj) and isinstance(obj, type):
            continue
        if hasattr(obj, 'reset'):
            try:
                obj.reset()
            except Exception:
                pass

def clear_state():
    """Очистить все данные и состояния в системе."""
    for obj in list(globals().values()):
        if callable(obj) and isinstance(obj, type):
            continue
        if hasattr(obj, 'clear'):
            try:
                obj.clear()
            except Exception:
                pass

def reload():
    """Перезагрузить систему с нуля."""
    import os
    filename = os.path.basename(__file__)
    if filename.endswith('.pyc'):
        return
    with open(filename, 'r') as f:
        code = compile(f.read(), filename, 'exec')
    exec(code)

def demo_setup():
    """Установить демо-данные для демонстрации."""
    for obj in list(globals().values()):
        if callable(obj) and isinstance(obj, type):
            continue
        if hasattr(obj, 'setup_demo'):
            try:
                obj.setup_demo()
            except Exception:
                pass
