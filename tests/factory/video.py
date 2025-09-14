from pathlib import Path
import subprocess
import uuid


class VideoFactory:
    @classmethod
    def create(
        cls,
        directory: str,
        n_frames: int = 10,
        fps: int = 30,
        resolution: str = "640x480"
    ) -> str:
        """
        Create a temporary video file for testing purposes, the name of the video
        will be an uuid4 string and the extension will be .mp4.

        Parameters
        ----------
        directory : str
            The directory where the temporary video file will be created.
        n_frames : int, optional
            The number of frames in the video, by default 10.
        fps : int, optional
            The frames per second of the video, by default 30.
        resolution : str, optional
            The resolution of the video in WIDTHxHEIGHT format, by default "640x480".

        Returns
        -------
        str
            The path to the created temporary video file.
        """

        video_path = Path(directory) / f"{uuid.uuid4()}.mp4"
        command = [
            "ffmpeg",
            "-y",
            "-f", "lavfi",
            "-i", f"testsrc=duration={n_frames/fps}:size={resolution}:rate={fps}",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            str(video_path)
        ]
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return str(video_path)
