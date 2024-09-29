"""dalleImage class tests."""
import unittest
from unittest.mock import patch, Mock
import openai
import os
import sys

# Add the root folder to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the DALL·E Image Generator class from dalleImage.py
from dalleImage import dalleImage

class TestDalleImage(unittest.TestCase):
    def setUp(self):
        """Set up the DALL·E Image Generator instance."""
        self.api_key = 'mock_api_key'
        self.dalle = dalleImage(self.api_key)

    @patch("openai.images.generate")  # Mock the correct API call
    def test_generate_image(self, mock_image_generate):
        """
        Test the generate_image method of the DALL·E Image Generator.

        This test focuses on the generate_image method and uses mocking to avoid real API calls.
        """
        model="dall-e-3"
        quality="standard"
        prompt = "Generate an image"
        n = 1
        size = "1024x1024"
        expected_response = {"image": "generated_image.png"}

        # Mock the OpenAI API response
        mock_image_generate.return_value = expected_response

        # Call the generate_image method
        response = self.dalle.generate_image(prompt, n, size)

        # Check if the API call was made with the correct arguments
        mock_image_generate.assert_called_once_with(model=model, quality=quality, prompt=prompt, n=n, size=size)

        # Check if the response matches the expected response
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
