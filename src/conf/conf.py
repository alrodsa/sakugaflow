from functools import partial
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from libs.base.conf.schema import Conf

class FoldersConf(BaseSettings):
    """
    Configuration class for folders.

    Attributes
    ----------
    input : str
        The input folder path.
    output : str
        The output folder path.
    tmp : str
        The temporary folder path.

    """

    input: str
    output: str
    tmp: str

    model_config = SettingsConfigDict(env_prefix="SAKUGAFLOW_FOLDERS_")

class BoosterConf(BaseSettings):
    """
    Configuration class for booster.

    Attributes
    ----------
    model : str
        The model to use for processing the video. Defaults to "rife-anime".
    fps_multiplier : int
        The multiplier for the frames per second (fps) of the output video.
        Defaults to 2. Minimum value is 2 and maximum value is 4.

    """

    model: str = "rife-anime"
    fps_multiplier: int = 2

    model_config = SettingsConfigDict(env_prefix="SAKUGAFLOW_BOOSTER_")

class SakugaflowConf(Conf, BaseSettings):
    """
    Configuration class for Sakugaflow.

    Attributes
    ----------
    folders : FoldersConf
        The folders configuration.
    booster : BoosterConf
        The booster configuration.

    """

    folders: FoldersConf
    booster: BoosterConf

    model_config = SettingsConfigDict(env_prefix="SAKUGAFLOW_")



