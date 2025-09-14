from unittest import TestCase
from unittest.mock import patch


class TestPPrint(TestCase):
    def test_get_version(self):
        from src.utils.pprint import get_version

        version = get_version()
        self.assertIsInstance(version, str)
        self.assertGreater(len(version), 0)
        self.assertNotIn("dev", version)

    @patch('src.utils.pprint.version')
    def test_get_version_dev(self, mock_version):
        from src.utils.pprint import get_version
        from importlib.metadata import PackageNotFoundError

        mock_version.side_effect = PackageNotFoundError
        version = get_version()
        self.assertEqual(version, "dev")

    def test_visual_len(self):
        from src.utils.pprint import visual_len

        self.assertEqual(visual_len("hello"), 5)
        self.assertEqual(visual_len("こんにちは"), 10)
        self.assertEqual(visual_len("😊"), 2)
        self.assertEqual(visual_len("a😊b"), 4)

    def test_banner(self):
        from src.utils.pprint import banner

        bnr = banner()
        self.assertIn("SakugaFlow", bnr)
        self.assertIn("v", bnr)
        self.assertIn("動画をもっと滑らかに", bnr)
        self.assertIn("Make your videos smoother", bnr)
        self.assertTrue(bnr.startswith("="))
        self.assertTrue(bnr.endswith("="))
        
