import fire

from src.cli.douga import douga

def main() -> None:
    """
    CLI entrypoint.
    """
    fire.Fire({
        "douga": douga,
    })
