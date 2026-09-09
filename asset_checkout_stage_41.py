# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: AssetCheckout
class DryRunMode:
    def __init__(self):
        self._state = 'idle'
        self._logs = []

    def enable(self):
        self._state = 'dry_run'
        self._logs = []

    def disable(self):
        self._state = 'idle'
        self._logs.clear()

    def log(self, msg):
        if self._state == 'dry_run':
            self._logs.append(msg)
            return msg
        return None

    def is_active(self):
        return self._state == 'dry_run'

    def get_logs(self):
        return list(self._logs)

    def __enter__(self):
        self.enable()
        return self

    def __exit__(self, *args):
        self.disable()
