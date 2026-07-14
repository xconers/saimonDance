# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: AssetCheckout
class Tag:
    def __init__(self, name: str):
        self.name = name.lower().strip()

    def __eq__(self, other):
        if isinstance(other, Tag): return self.name == other.name
        if isinstance(other, str): return self.name == other.lower().strip()
        return NotImplemented

    def __hash__(self): return hash(self.name)

class Checkout:
    def add_tag(self, tag_name: str):
        self.tags.add(Tag(tag_name))

    def remove_tag(self, tag_name: str):
        for tag in list(self.tags):
            if tag == tag_name:
                self.tags.remove(tag); return True
        return False
