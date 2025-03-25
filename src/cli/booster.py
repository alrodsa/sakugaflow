from libs.base.conf.app import configure
from src.conf.conf import SakugaflowConf
from src.constants.app import APP_NAME, ROOT_DIR


def booster() -> None:
    """
    Booster function
    """
    conf = configure(APP_NAME, ROOT_DIR, SakugaflowConf)
    #print(conf)
