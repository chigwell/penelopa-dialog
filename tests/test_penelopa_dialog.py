import unittest
from unittest.mock import patch
from penelopa_dialog import PenelopaDialog


class TestPenelopaDialog(unittest.TestCase):
    def setUp(self):
        self.prompt_message = "Enter your name: "
        self.dialog = PenelopaDialog(self.prompt_message)

    def test_initialization(self):
        """Test that the object is initialized with the correct prompt message."""
        self.assertEqual(self.dialog.prompt_message, self.prompt_message)

    @patch('builtins.input', return_value='John')
    def test_run_with_user_input(self, mocked_input):
        """Test the run method with a mocked input."""
        response = self.dialog.run()
        self.assertEqual(response, 'John')
        mocked_input.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
