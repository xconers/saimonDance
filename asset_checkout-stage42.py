# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: AssetCheckout
import sys

def color_off():
    """Disables color output."""
    global _color_enabled
    _color_enabled = False

def color_on():
    """Enables color output."""
    global _color_enabled
    _color_enabled = True

def color(text, fg=None, bg=None, bold=False):
    """Returns ANSI-colored text. If _color_enabled is False, returns plain text."""
    if not _color_enabled:
        return text
    codes = []
    if bold:
        codes.append("1")
    if fg:
        codes.append(f"38;5;{fg}")
    if bg:
        codes.append(f"48;5;{bg}")
    codes.append("0")
    return f"\033[{','.join(codes)}m{text}\033[0m"

_color_enabled = True

if __name__ == "__main__":
    _color_enabled = True
    print(color("AssetCheckout v42", fg=51, bold=True))
    print(color("Type 'color_off' to disable colors.", fg=244))
    color_off()
    print(color("AssetCheckout v42", fg=51, bold=True))
    color_on()
    print(color("Type 'color_off' to disable colors.", fg=244))
