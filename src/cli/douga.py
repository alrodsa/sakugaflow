from pathlib import Path

from src.utils.pprint import execution_args

from src.constants.video import VIDEO_EXTENSIONS


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
        print("IS DIRECTORY")
        return [
            str(file) for file in media_files
            if file.suffix.lower() in VIDEO_EXTENSIONS
        ]

    return [directory] if Path(directory).suffix.lower() in VIDEO_EXTENSIONS else []


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
    print(
        execution_args(
            input_directory=input_directory,
            output_directory=output_directory,
            fps_multiplier=fps_multiplier
        )
    )
    media_files = media_from_directory(input_directory)
    print(f"Media files found: {media_files}")
