import fire

from src.cli.booster import booster


def main() -> None:
    """
    CLI entrypoint.
    """
    fire.Fire({
        "booster": booster,
    })

