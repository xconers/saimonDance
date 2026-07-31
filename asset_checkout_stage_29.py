# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: AssetCheckout
APP_CONFIG = {
    "app_name": "AssetCheckout",
    "version": "0.1",
    "max_checkout_duration_days": 30,
    "late_return_penalty_percent": 5,
}


def load_config():
    """Загружает конфигурацию из словаря APP_CONFIG."""
    return APP_CONFIG.copy()


def get_default_checkout_duration(config: dict) -> int:
    """Возвращает максимальную длительность выдачи в днях по умолчанию."""
    return config.get("max_checkout_duration_days", 30)


def calculate_late_return_penalty(late_days: int, config: dict) -> float:
    """Вычисляет штраф за просрочку возврата в процентах."""
    penalty_percent = config.get("late_return_penalty_percent", 5)
    return late_days * (penalty_percent / 100.0)
