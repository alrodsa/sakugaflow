from pathlib import Path
import shutil
import tempfile
from typing import override
from unittest import TestCase
from unittest.mock import patch

from tests.factory.video import VideoFactory


class TestDougaCLI(TestCase):
    @override
    def setUp(self):
        super().setUp()
        self.temporal_folder = tempfile.TemporaryDirectory()
        self.input_directory = Path(self.temporal_folder.name) / "input"
        self.output_directory = Path(self.temporal_folder.name) / "output"
        self.input_directory.mkdir(parents=True, exist_ok=True)
        self.output_directory.mkdir(parents=True, exist_ok=True)
        self.test_video_path = self.input_directory / "test_video.mp4"
        self.test_video_path.touch()

    @override
    def tearDown(self):
        super().tearDown()
        self.temporal_folder.cleanup()

    def test_media_from_directory(self):
        from src.cli.douga import media_from_directory

        media_files = media_from_directory(str(self.input_directory))
        self.assertIn(str(self.test_video_path), media_files)
        self.assertEqual(len(media_files), 1)

    def test_media_from_nonexistent_directory(self):
        from src.cli.douga import media_from_directory

        with self.assertRaises(FileNotFoundError):
            media_from_directory("nonexistent_directory")

    def test_media_from_file(self):
        from src.cli.douga import media_from_directory

        media_files = media_from_directory(str(self.test_video_path))
        self.assertIn(str(self.test_video_path), media_files)
        self.assertEqual(len(media_files), 1)

    def test_check_fps_multiplier_valid(self):
        from src.cli.douga import check_fps_multiplier

        try:
            check_fps_multiplier(2)
            check_fps_multiplier(4)
            check_fps_multiplier(8)
        except ValueError:
            self.fail("check_fps_multiplier raised ValueError unexpectedly!")

    def test_check_fps_multiplier_invalid(self):
        from src.cli.douga import check_fps_multiplier

        with self.assertRaises(ValueError):
            check_fps_multiplier(3)
        with self.assertRaises(ValueError):
            check_fps_multiplier(5)
        with self.assertRaises(ValueError):
            check_fps_multiplier(1)

    @patch("src.cli.douga.Interpolator")
    def test_douga(self, mock_interpolator):
        from src.cli.douga import douga

        mock_interpolator.return_value.run.side_effect = \
                lambda input_path, output_folder: shutil.move(
                    input_path, Path(output_folder) / Path(input_path).name
                )

        VideoFactory.create(directory=str(self.input_directory))

        try:
            douga(str(self.input_directory), str(self.output_directory), 2)
        except Exception as e:
            self.fail(f"douga raised an exception unexpectedly: {e}")

        output_files = list(self.output_directory.glob("*.mp4"))
        self.assertTrue(len(output_files) > 0, "No output files were created.")

