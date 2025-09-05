import math
from pathlib import Path

from src.utils.pprint import execution_args
from src.constants.video import VIDEO_EXTENSIONS

from tqdm import tqdm

from saibyo.conf.conf import SaibyoConf, InterpolatorConf
from saibyo.core.interpolation.rife import RifeInterpolator as Interpolator


def media_from_directory(directory: str) -> list:
    """
    Function to retrieve media files from a specified directory.

    Parameters
    ----------
    directory : str
        The directory from which to retrieve media files.

    Returns
    -------
    list
        A list of media file paths found in the directory.
    """

    if not Path(directory).exists():
        raise FileNotFoundError(f"Input '{directory}' does not exist.")

    if Path(directory).is_dir():
        media_files = list(Path(directory).glob('*.*'))
        return [
            str(file) for file in media_files
            if file.suffix.lower() in VIDEO_EXTENSIONS
        ]

    return [directory] if Path(directory).suffix.lower() in VIDEO_EXTENSIONS else []

def check_fps_multiplier(fps_multiplier: int) -> None:
    """
    Check if the fps_multiplier is a power of two and greater than or equal to 2.
    At the moment, only 2, 4 and 8 are supported.

    Parameters
    ----------
    fps_multiplier : int
        The fps multiplier to check.

    Returns
    -------
    None
        Raises a ValueError if the fps_multiplier is not valid.
    """
    if fps_multiplier not in [2 ** i for i in range(1, 4)]:
        raise ValueError(
            "Error on `fps_multiplier` parameter. Only 2, 4 and 8 are supported."
        )

def douga(input_directory: str, output_directory: str, fps_multiplier: int) -> None:
    """
    Function to handle the 'douga' command in the CLI. It will get the video or
    videos from the input directory, and boosting the fps up them one by one,
    applying the specified FPS multiplier. The processed videos will be saved in
    the output directory.

    Parameters
    ----------
    input_directory : str
        The directory containing the input video files.
    output_directory : str
        The directory where the processed video files will be saved.
    fps_multiplier : int
        The multiplier for the frames per second (FPS) of the videos.
    """
    check_fps_multiplier(fps_multiplier)

    print(
        execution_args(
            input_directory=input_directory,
            output_directory=output_directory,
            fps_multiplier=f"x{str(fps_multiplier)}"
        )
    )

    media_files = media_from_directory(input_directory)
    print(f"[🎥] Media found: {media_files}")
    print(f"Exponential: {int(math.log2(fps_multiplier))}")

    config = SaibyoConf(
        interpolator=InterpolatorConf(
            exponential=int(math.log2(fps_multiplier)),
        )
    )
    print(f"[⚙️] Configuration loaded: {config}")

    for media_file in tqdm(
        media_files,
        desc="Processing media",
        unit="🎬",
        ncols=80,
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]",
        colour="green"
    ):
        print(f"[🎬] Boosting up FPS from {media_file}")
        Interpolator(config).run(
            input_path=media_file,
            output_folder=output_directory,
        )
        print(f"[✅] Processed {media_file} and saved to {output_directory}")

# python main.py douga /workspaces/sakugaflow/data-sakugaflow/input /workspaces/sakugaflow/data-sakugaflow/output 4
