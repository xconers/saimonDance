# === Stage 43: Добавь пагинацию длинных списков ===
# Project: AssetCheckout
def paginate(items, page_size=10):
    """Yield slices of items for pagination."""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]
