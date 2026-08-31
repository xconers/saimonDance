# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: AssetCheckout
def suggest_next_action(record):
    """
    Returns a text recommendation for the next step based on the current checkout record.
    Works with the same data structure used throughout AssetCheckout.
    """
    status = record.get("status", "unknown")
    due_date = record.get("due_date", "")
    returned = record.get("returned", False)
    notes = record.get("notes", "")
    receiver_name = record.get("receiver", "")

    if returned:
        return "Equipment returned. Verify condition and log any damage in the notes field."

    if status == "returned":
        return "Equipment already marked as returned. Consider closing the record or archiving it."

    if due_date and date.today() > date.fromisoformat(due_date):
        return f"Due date ({due_date}) has passed for receiver {receiver_name}. Send a reminder and request return."

    if not due_date:
        return "No due date set. Add a due_date to track when the equipment should be returned."

    if not notes and status != "active":
        return "Add notes about the condition or any special instructions for the receiver."

    if status == "active" and date.today() < date.fromisoformat(due_date):
        return "Equipment is active and within the due period. Monitor usage and prepare a return reminder before the due date."

    return "All checks passed. The record looks complete."
