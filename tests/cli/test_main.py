from unittest import TestCase
from unittest.mock import MagicMock, patch
from src.cli.main import main

class MainCLITest(TestCase):
    @patch('fire.Fire')
    @patch('src.cli.main.douga')
    def test_cli_douga(self, mock_douga, mock_fire):
        main()

        mock_fire.assert_called_once()
        (arg_dict,), kwargs = mock_fire.call_args
        self.assertIn("douga", arg_dict)
        self.assertEqual(arg_dict["douga"], mock_douga)
        self.assertEqual(kwargs, {})
