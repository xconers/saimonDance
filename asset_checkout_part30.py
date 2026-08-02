# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: AssetCheckout
class AssetProfile:
    """User profile defining checkout limits and roles."""

    def __init__(self, name: str = "default", max_assets: int | None = None):
        self.name = name
        self.max_assets = max_assets

    @property
    def is_admin(self) -> bool:
        return self.name == "admin"


profiles = {
    "admin": AssetProfile(name="admin", max_assets=None),
}
