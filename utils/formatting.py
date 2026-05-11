"""格式化输出辅助"""


def separator(title: str = "", width: int = 50) -> str:
    """分隔线"""
    if title:
        return f"\n{'=' * width}\n{title}\n{'=' * width}"
    return f"\n{'=' * width}"


def box_title(text: str, width: int = 40) -> str:
    """边框标题"""
    lines = text.split("\n")
    result = "╔" + "═" * width + "╗\n"
    for line in lines:
        padded = line.ljust(width)
        result += "║ " + padded + " ║\n"
    result += "╚" + "═" * width + "╝"
    return result


def progress_bar(value: float, max_value: float = 100, width: int = 20) -> str:
    """进度条"""
    ratio = value / max_value
    filled = int(width * ratio)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {value:.0f}/{max_value:.0f}"
