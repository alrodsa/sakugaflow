import pyfiglet
from wcwidth import wcswidth
from src.constants.app import APP_NAME, ARGS_MAP
from importlib.metadata import version, PackageNotFoundError


def get_version() -> str:
    """
    Get the version of the application.

    Returns
    -------
    str
        The version of the application.
    """
    try:
        return version(APP_NAME)
    except PackageNotFoundError:
        return "dev"


def visual_len(text: str) -> int:
    """
    Return the visual width of a string (handles kanji, emojis, etc.).

    Parameters
    ----------
    text : str
        The string to measure.

    Returns
    -------
    int
        The visual width of the string.
    """
    return wcswidth(text)


def banner() -> str:
    """
    Generate a banner with the application name and version, formatted in ASCII art.
    The banner includes the app name, version, and a tagline, all framed in a box.
    """
    ascii_lines = pyfiglet.figlet_format("Sakugaflow", font="slant").splitlines()
    width_ascii = len(max(ascii_lines, key=len))

    info_lines = [
        f"🌀 SakugaFlow v{get_version()}",
        "「動画をもっと滑らかに」",
        "Make your videos smoother ✨"
    ]
    width_info = max(visual_len(line) for line in info_lines)
    width = max(width_ascii, width_info)
    border = "=" * (width + 8)
    output = [border]

    for line in ascii_lines:
        output.append(f"||  {line.ljust(width)}  ||")
    output.append(border)

    for line in info_lines:
        pad = width - visual_len(line)
        left = pad // 2
        right = pad - left
        output.append(f"||  {' ' * left}{line}{' ' * right}  ||")

    output.append(border)

    return "\n".join(output)


def execution_args(title: str = "Parameters", **kwargs) -> str:
    """
    Pretty-print execution arguments inside a framed box with emojis and aligned columns.
    """
    labels = []
    values = []
    for key, value in kwargs.items():
        arg_info = ARGS_MAP.get(key, {"emoji": "🔹", "label": key})
        emoji = arg_info["emoji"]
        label = arg_info["label"]
        labels.append(f"{emoji} {label}")
        values.append(str(value))

    left_width = max(visual_len(lbl) for lbl in labels)

    lines = [title, ""]
    for lbl, val in zip(labels, values):
        pad = left_width - visual_len(lbl)
        lines.append(f"{lbl}{' ' * pad}: {val}")

    width = max(visual_len(line) for line in lines)
    border = "=" * (width + 8)

    output = [border]
    for line in lines:
        pad = width - visual_len(line)
        output.append(f"||  {line}{' ' * pad}  ||")
    output.append(border)

    return "\n".join(output)
