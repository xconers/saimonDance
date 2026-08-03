# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: AssetCheckout
class ProfileSwitcher:
    """Переключение активного пользовательского профиля."""

    def __init__(self, profiles):
        self.profiles = profiles
        self._active_index = 0
        if not profiles:
            raise ValueError("Список профилей пуст")

    @property
    def active_profile(self):
        return self.profiles[self._active_index]

    @property
    def profile_names(self):
        return [p.name for p in self.profiles]

    @property
    def current_name(self):
        return self.active_profile.name

    def switch_to(self, name_or_index):
        if isinstance(name_or_index, int):
            idx = name_or_index % len(self.profiles)
        else:
            target = next((p for p in self.profiles if p.name == name_or_index), None)
            if target is None:
                raise ValueError(f"Профиль '{name_or_index}' не найден")
            idx = self.profiles.index(target)
        return self._active_index, idx

    def next(self):
        new_idx = (self._active_index + 1) % len(self.profiles)
        return self.switch_to(new_idx)

    def previous(self):
        new_idx = (self._active_index - 1) % len(self.profiles)
        return self.switch_to(new_idx)

    def __repr__(self):
        return f"ProfileSwitcher(active={self.current_name})"
