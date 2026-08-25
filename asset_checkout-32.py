# === Stage 32: Добавь журнал действий пользователя ===
# Project: AssetCheckout
class ActionLog:
    def __init__(self):
        self._entries = []

    def record(self, action: str, user: str, target_id: str, timestamp: str = None):
        if timestamp is None:
            from datetime import datetime, timezone
            timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
        self._entries.append({
            'id': len(self._entries) + 1,
            'action': action,
            'user': user,
            'target_id': target_id,
            'timestamp': timestamp,
        })

    def log_checkout(self, user, target_id):
        self.record('CHECKOUT', user, target_id)

    def log_return(self, user, target_id):
        self.record('RETURN', user, target_id)

    def log_status_change(self, user, target_id, new_status):
        self.record('STATUS_CHANGE', user, target_id, f'-> {new_status}')

    def get_log(self):
        return list(self._entries)

    def clear(self):
        self._entries.clear()

    def __len__(self):
        return len(self._entries)

    def __repr__(self):
        return f'<ActionLog: {len(self._entries)} entries>'
