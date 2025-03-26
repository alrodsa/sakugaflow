from libs.base.conf.app import configure
from src.conf.conf import SakugaflowConf
from src.constants.app import APP_NAME, ROOT_DIR


def booster() -> None:
    """
    Booster function for the CLI. It will configure the application
    and run the booster.
    """
    conf = configure(APP_NAME, ROOT_DIR, SakugaflowConf)
