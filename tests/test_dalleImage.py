import unittest
from unittest.mock import patch, Mock
import openai
import os
import sys

# Add the root folder to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ..dalleImage import dalleImage

class TestDalleImage(unittest.TestCase):
    def setUp(self):
        self.api_key = 'api_key'
        self.dalle = dalleImage(self.api_key)

    def test_generate_image(self):
        # Unit test of the generate_image method
        # Using the mocking technique, the actual OpenAI API call is not made ergo real credentials are not used

        prompt = "Generate an image"
        n = 2
        size = "256x256"
        expected_response = {"image": "generated_image.png"}

        # Mock the OpenAI API call
        mock_image_create = Mock(return_value=expected_response)
        with patch.object(openai.Image, "create", mock_image_create):
            # Call the generate_image method
            response = self.dalle.generate_image(prompt, n, size)

        # Check if the API call was made with the correct arguments
        mock_image_create.assert_called_once_with(prompt=prompt, n=n, size=size)

        # Check if the response matches the expected response
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
