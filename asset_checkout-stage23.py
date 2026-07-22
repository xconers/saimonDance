# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: AssetCheckout
def print_table(headers, rows):
    """Форматированный вывод данных в консоль."""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if len(str(val)) > col_widths[i]:
                col_widths[i] = len(str(val))

    lines = []
    sep = "─" * sum(col_widths) + "│"
    header_line = " │ ".join(h.ljust(w) for h, w in zip(headers, col_widths))
    lines.append(header_line)
    lines.append(sep)
    for row in rows:
        line = " │ ".join(str(v).ljust(w) for v, w in zip(row, col_widths))
        lines.append(line)
    print("\n".join(lines))

# Пример использования после инициализации checkout:
checkout.init()
print_table(["ID", "Получатель", "Дата выдачи", "Состояние"],
             [(i, c.name, c.date_str(), c.status_str()) for i, c in enumerate(checkout.assets)])
